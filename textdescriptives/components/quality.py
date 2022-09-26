"""Component for calculating quality metrics."""
from collections import Counter, defaultdict
from functools import partial
from typing import Callable, Dict, List, Optional, Tuple, Union

import numpy as np
from spacy.language import Language
from spacy.tokens import Doc, Span

from textdescriptives.components.utils import span_getter_to_doc_getter

DEFAULT_QUALITY_THRESHOLDS = {
    "n_stop_words": (2, None),
    "alpha_ratio": (0.8, None),
    "mean_word_length": (3, 10),
    "doc_length": (10, 100_000),
    "symbol_#_2_word_ratio": (None, 0.1),
    "proportion_ellipsis": (None, 0.3),
    "proportion_bullet_points": (None, 0.8),
    "duplicate_line_chr_fraction": (None, 0.2),
    "duplicate_paragraph_chr_fraction": (None, 0.2),
    "duplicate_5-gram_chr_fraction": (None, 0.15),
    "duplicate_6-gram_chr_fraction": (None, 0.14),
    "duplicate_7-gram_chr_fraction": (None, 0.13),
    "duplicate_8-gram_chr_fraction": (None, 0.12),
    "duplicate_9-gram_chr_fraction": (None, 0.11),
    "duplicate_10-gram_chr_fraction": (None, 0.1),
    "top_2-gram_chr_fraction": (None, 0.20),
    "top_3-gram_chr_fraction": (None, 0.18),
    "top_4-gram_chr_fraction": (None, 0.16),
    "contains_lorem ipsum": False,
}


def n_stop_words(span: Span) -> int:
    """Count the number of stop words in a document.

    Args:
        span (Span): spaCy span object

    Returns:
        int: number of stop words
    """
    return sum(t.is_stop for t in span)


def mean_word_length(span: Span) -> float:
    """Calculate the mean word length of a document.

    Args:
        span (Span): spaCy span object

    Returns:
        float: mean word length
    """
    tokens_lengths = [len(t) for t in span]
    if tokens_lengths:
        return float(np.mean(tokens_lengths))
    return 0.0


def alpha_ratio(span: Span) -> float:
    """The percentage of spacy tokens in this document which contain
    at leat one alphabetic character.

    Args:
        span (Span): spaCy span object

    Returns:
        float: alpha ratio
    """

    def contains_alpha(token):
        for char in token.text:
            if char.isalpha():
                return True
        return False

    token_contains_alpha = [contains_alpha(token) for token in span]
    if token_contains_alpha:
        return float(np.mean(token_contains_alpha))
    return 0.0


def proportion_bullet_points(  # pylint: disable=dangerous-default-value
    span: Span, bullet_point: set = {"-", "*"}
) -> float:
    """Calculate the proportion of lines which start with a bullet points in a span.

    Args:
        span (Span): spaCy span object
        bullet_point (set): set of bullet points

    Returns:
        float: proportion of bullet points
    """
    # check if has extension _lines
    if not hasattr(span._, "lines"):
        lines = span.text.split("\n")
    else:
        lines = span._.lines
    line_starts_with_bullet = [
        line.strip().startswith(tuple(bullet_point)) for line in lines
    ]
    if line_starts_with_bullet:
        return float(np.mean(line_starts_with_bullet))
    return 0.0


def proportion_ellipsis(  # pylint: disable=dangerous-default-value
    span: Span, ellipsis: set = {"…", "..."}
) -> float:
    """Calculate the proportion line which ends with an ellipsis in a span.

    Args:
        span (Span): spaCy span object
        ellipsis (set): set of ellipsis

    Returns:
        float: proportion of ellipsis
    """
    if not hasattr(span._, "lines"):
        lines = span.text.split("\n")
    else:
        lines = span._.lines

    line_ends_with_ellipsis = [line.strip().endswith(tuple(ellipsis)) for line in lines]
    if line_ends_with_ellipsis:
        return float(np.mean(line_ends_with_ellipsis))
    return 0.0


def get_ranges(arr: np.ndarray) -> List[Tuple[int, int]]:
    """Get true ranges from boolean array, i.e.

    Example:
        >>> get_ranges(np.array([0, 1, 1, 0, 0, 1, 1]))
        [(1, 3), (5, 7)]
    """
    ranges = []
    start = None
    for i, val in enumerate(arr):
        if (val and start) is None:
            start = i
        elif not val and start is not None:
            ranges.append((start, i))
            start = None
    if start is not None:
        ranges.append((start, len(arr)))
    return ranges


def duplicate_paragraph_chr_fraction(span: Span) -> float:
    """Calculate the character fraction of duplicate paragraphs.

    Args:
        span (Span): spaCy span object

    Returns:
        float: The fraction of duplicate characters.
    """
    chr_len = len(span.text)
    if chr_len == 0:
        return 0.0

    if not hasattr(span._, "paragraphs"):
        paragraphs = span.text.split("\n\n")
    else:
        paragraphs = span._.paragraphs
    paragraph_counter = Counter(paragraphs)

    duplicate_chr = 0
    for t, c in paragraph_counter.items():
        if c > 1:
            duplicate_chr += len(t) * (c - 1)
    frac = duplicate_chr / chr_len
    return frac


def duplicate_line_chr_fraction(span: Span) -> float:
    """Calculate the character fraction of duplicate lines.

    Args:
        span (Span): spaCy span object

    Returns:
        float: The fraction of duplicate characters.
    """
    chr_len = len(span.text)
    if chr_len == 0:
        return 0.0

    if not hasattr(span._, "lines"):
        lines = span.text.split("\n")
    else:
        lines = span._.lines
    line_counter = Counter(lines)

    duplicate_chr = 0
    for t, c in line_counter.items():
        if c > 1:
            duplicate_chr += len(t) * (c - 1)
    frac = duplicate_chr / chr_len
    return frac


def symbol_2_word_ratio(span: Span, symbol: str) -> float:
    """Calculate the ratio of symbols to words in a span.

    Args:
        span (Span): spaCy span object
        ratio (float): ratio of symbols to words
        symbol (str): symbol to count

    Returns:
        float: ratio of symbols to words
    """
    n_symbol = span.text.count(symbol)
    n_words = sum(not (t.is_space or t.is_punct) for t in span)
    if n_words:
        return n_symbol / n_words
    return 0.0


def span_ngrams(span: Span, ngram_range: Tuple[int, int]) -> Dict[str, Counter]:
    """Calculate the counts of n-grams in the specified range.

    Args:
        span (Span): spaCy span object
        ngram_range (Tuple[int, int]): The n-gram range.

    Returns:
        Dict[int, Dict[str, int, List[Span]]]: A dictionary that for each n in the ngram
            range contains the counts of the n-grams as well as the spans of the
            n-grams.
    """
    max_len = len(span)
    lower, upper = ngram_range
    shingles_count = {
        n: defaultdict(lambda: {"count": 0, "span": []})
        for n in range(lower, upper + 1)
    }
    for i, _ in enumerate(span):
        for ngram_size in range(lower, upper + 1):
            end = i + ngram_size
            if not end > max_len:
                ngram_span = span[i:end]
                ngram = ngram_span.text
                shingles_count[ngram_size][ngram]["count"] += 1
                shingles_count[ngram_size][ngram]["span"].append(ngram_span)
    return shingles_count


def duplicate_ngram_fraction(
    span: Span,
    ngram_range: Tuple[int, int],
) -> Dict[int, float]:
    """calculates the character fraction of duplicate n-gram over the overall text,
    taking care not to count overlapping n-grams twice. This does not include spaces
    between the n-grams.

    Args:
        span (Span): spaCy span object
        ngram_range (Tuple[int, int], optional): The n-gram range.

    Returns:
        Dict[int, float]: the fraction of duplicate characters for each
            n-gram size
    """
    max_len = len(span)
    chr_len = len(span.text)
    if chr_len == 0:
        return {n: 0.0 for n in range(ngram_range[0], ngram_range[1] + 1)}
    shingles_count = span_ngrams(span, ngram_range)
    duplicate_chr_fraction = {}
    for ngram_size, ngrams in shingles_count.items():
        # create a boolean array of the same length as the text
        # where True indicates that the token is a duplicate
        is_duplicate = np.zeros(max_len, dtype=bool)
        # set duplicate tokens to True
        for ngram, count in ngrams.items():
            if count["count"] > 1:
                for ngram_span in count["span"]:
                    is_duplicate[ngram_span.start : ngram_span.end] = True

        duplicate_chars = 0
        # get duplicate ranges from boolean array
        for start, end in get_ranges(is_duplicate):
            _span = span[start:end]
            duplicate_chars += _span.end_char - _span.start_char
        duplicate_chr_fraction[ngram_size] = duplicate_chars / chr_len
    return duplicate_chr_fraction


def top_ngram_chr_fraction(
    span: Span,
    ngram_range: Tuple[int, int],
    min_count: int = 0,
) -> float:
    """Calculated whether the character fraction of the top n-grams is below the
    given thresholds

    Args:
        span (Span): spaCy span object
        ngram_range (Tuple[int, int], optional): Range of n grams to examine.
        min_count (int): Minimum count of n-grams to before an n-gram is considered
            a top n-gram. Defaults to 0.

    Returns:
        float: The fraction of the top n-grams.
    """
    chr_len = len(span.text)
    if chr_len == 0:
        return {n: 0.0 for n in range(ngram_range[0], ngram_range[1] + 1)}

    ngram_counter = span_ngrams(span, ngram_range=ngram_range)
    top_ngram_chr_frac = {}
    for n in ngram_counter:
        # find the top n-gram
        ngram, count_span = max(ngram_counter[n].items(), key=lambda x: x[1]["count"])
        count = count_span["count"]
        if count >= min_count:
            # calculate the fraction of the top n-gram
            top_ngram_chr_frac[n] = (len(ngram) * count) / chr_len
        else:
            top_ngram_chr_frac[n] = 0.0

    return top_ngram_chr_frac


def contains_string(span: Span, string: str) -> bool:
    """Check if a span contains a string.

    Args:
        span (Span): spaCy span object
        string (str): string to check for

    Returns:
        bool: True if span contains string
    """
    return string in span.text


class Quality:
    """spaCy component for adding text quality metrics to the `Doc` and `Span` objects.
    Extracts metrics and returns them as a dictionary as the ._.quality attribute.
    """

    def __init__(  # pylint: disable=dangerous-default-value
        self,
        nlp: Language,
        name: str,
        symbols: List[str],
        contains: List[str],
        top_ngram_range: Tuple[int, int],
        top_ngram_min_count: int,
        duplicate_n_gram_fraction_range: Tuple[int, int],
        quality_thresholds: Optional[
            Dict[str, Union[bool, Tuple[Optional[float], Optional[float]]]]
        ] = None,
        force: bool = False,
    ):  # noqa: D107
        """Initialise components"""
        self.name = name
        self.force = force
        self.symbols = symbols
        self.contains = contains
        self.top_ngram_range = top_ngram_range
        self.top_ngram_min_count = top_ngram_min_count
        self.duplicate_n_gram_fraction_range = duplicate_n_gram_fraction_range
        if quality_thresholds is None:
            quality_thresholds = DEFAULT_QUALITY_THRESHOLDS
        self.quality_thresholds = quality_thresholds

        self.getters = {
            # heuristic quality filters
            "n_stop_words": n_stop_words,
            "alpha_ratio": alpha_ratio,
            "mean_word_length": mean_word_length,
            "doc_length": len,
            "proportion_ellipsis": proportion_ellipsis,
            "proportion_bullet_points": proportion_bullet_points,
            # text repetition
            "duplicate_line_chr_fraction": duplicate_line_chr_fraction,
            "duplicate_paragraph_chr_fraction": duplicate_paragraph_chr_fraction,
            "duplicate_ngram_chr_fraction": partial(
                duplicate_ngram_fraction, ngram_range=duplicate_n_gram_fraction_range
            ),
            "top_ngram_chr_fraction": partial(
                top_ngram_chr_fraction,
                ngram_range=top_ngram_range,
                min_count=top_ngram_min_count,
            ),
        }
        # add symbol to word ratio
        for symbol in symbols:
            self.getters[f"symbol_{symbol}_2_word_ratio"] = partial(
                symbol_2_word_ratio, symbol=symbol
            )
        # add contains
        for string in contains:
            self.getters[f"contains_{string}"] = partial(contains_string, string=string)

        self.extensions = {
            "passed_quality_check": self.passed_quality_thresholds,
            "quality": self.quality_getter,
        }

        self.set_extensions()

    def __call__(self, doc: Doc):
        """Run the pipeline component"""
        return doc

    def quality_getter(self, span: Span) -> Dict[str, Union[float, int, bool]]:
        """Apply quality functions to doc

        Args:
            span (Span): spaCy span object

        Returns:
            Dict[str, Union[float, int, bool]]: dictionary of quality metrics
        """
        quality = {}
        for name, getter in self.getters.items():
            if name == "top_ngram_chr_fraction":
                chr_frac = getter(span)
                for n_gram, frac in chr_frac.items():
                    quality[f"top_{n_gram}-gram_chr_fraction"] = frac
            elif name == "duplicate_ngram_chr_fraction":
                chr_frac = getter(span)
                for n_gram, frac in chr_frac.items():
                    quality[f"duplicate_{n_gram}-gram_chr_fraction"] = frac
            else:
                quality[name] = getter(span)
        return quality

    def passed_quality_thresholds(self, span: Span) -> bool:
        """
        Checks whether a span passed the quality thresholds
        """
        quality = span._.quality
        for name, threshold in self.quality_thresholds.items():
            if name not in quality:
                raise KeyError(f"Quality metric {name} not found in doc._.quality")
            if isinstance(threshold, bool):
                if quality[name] != threshold:
                    return False
            elif isinstance(threshold, tuple) and len(threshold) == 2:
                if threshold[0] is not None and quality[name] < threshold[0]:
                    return False
                if threshold[1] is not None and quality[name] > threshold[1]:
                    return False
            else:
                raise ValueError(
                    f"Quality threshold {name} is not a bool, or "
                    + f"Tuple of length 2, but {type(threshold)}."
                )

        return True

    def set_extensions(self):
        """Set required extensions."""

        for ext_name, span_getter in self.extensions.items():
            doc_getter = span_getter_to_doc_getter(span_getter)

            if not Span.has_extension(ext_name) or self.force is True:
                Span.set_extension(ext_name, getter=span_getter, force=True)
            if not Doc.has_extension(ext_name) or self.force is True:
                Doc.set_extension(ext_name, getter=doc_getter, force=True)


@Language.factory(
    "quality",
    default_config={
        "symbols": ["#"],
        "contains": ["lorem ipsum"],
        "top_ngram_range": [2, 4],
        "top_ngram_min_count": 3,
        "duplicate_n_gram_fraction_range": [5, 10],
        "force": True,
        "quality_thresholds": None,
    },
)
def create_quality_component(  # pylint: disable=dangerous-default-value
    nlp: Language,
    name: str,
    symbols: List[str],
    contains: List[str],
    top_ngram_range: Tuple[int, int],
    top_ngram_min_count: int,
    duplicate_n_gram_fraction_range: Tuple[int, int],
    quality_thresholds: Optional[
        Dict[str, Union[bool, Tuple[Optional[float], Optional[float]]]]
    ] = None,
    force: bool = True,
) -> Callable[[Doc], Doc]:
    """Allows Quality to be added to a spaCy pipe using nlp.add_pipe("quality").

    Set the following extensions:
    - {Span/Doc}._.quality
    - {Span/Doc}._.passed_quality_check

    It is also possible to optionally set the following extensions:
    - {Span/Doc}._.lines
    - {Span/Doc}._.paragraphs

    These are used to calculate some of the quality metrics. They can be overwritten if
    you e.g. wish lines to be split on "\\r\\n" instead of "\\n".

    A large part of the quality metrics were proposed by [1] and [2] for filtering
    out low quality text from large text corpora.

    References:
    [1] Rae, J. W., Borgeaud, S., Cai, T., Millican, K., Hoffmann, J., Song, F., ... &
        Irving, G. (2021). Scaling language models: Methods, analysis & insights from
        training gopher. arXiv preprint arXiv:2112.11446.
    [2] Raffel, C., Shazeer, N., Roberts, A., Lee, K., Narang, S., Matena, M., ... &
        Liu, P. J. (2020). Exploring the limits of transfer learning with a unified
        text-to-text transformer. J. Mach. Learn. Res., 21(140), 1-67.

    Args:
        nlp (Language): spaCy language object
        name (str): name of the component
        symbols (List[str]): list of symbols for which to calculate the
            proportion the ratio of symbols to words. Defaults to ["#"].
        contains (List[str]): list of strings for which to check whether the
            document contains them. Defaults to ["lorem ipsum"].
        top_ngram_range (Tuple[int]): range of n-grams to calculate the
            proportion of the top n-gram. Defaults to [2, 4].
        top_ngram_min_count (int): minimum number of times a n-gram must occur to
            be considered a top n-gram. Defaults to 3.
        duplicate_n_gram_fraction_range (Tuple[int]): range of n-grams to
            calculate the proportion of duplicate n-grams. Defaults to [5, 10].
        quality_thresholds (Dict[str, Union[bool, Tuple[Union[int, float, None],
            Union[int, float, None]]]]): A dictionary of quality thresholds indicated by
            either a range (Tuple), wherein the first value is the lower bound and the
            second value is the upper bound. Lower and upper bounds can be None, in
            which case they are not checked. Alternatively, a boolean can be provided,
            checking if the quality metric is boolean. For example, if you  don't want
            documents containing `lorem ipsum`, to pass the quality check, you can set
            `quality_thresholds={"contains_lorem_ipsum": False}`. Similar if you want to
            set a upper bound on the `duplicate_5-gram_chr_fraction`, you can set
            `quality_thresholds={"duplicate_5-gram_chr_fraction": (None, 0.15)}`.
            Default values are set in
            `textdescriptives.components..quality.DEFAULT_QUALITY_THRESHOLDS`.
        force (bool): whether to overwrite existing extensions. Defaults to True.


    Returns:
        Callable[[Doc], Doc]: the spaCy component

    Example:
        >>> import spacy
        >>> from spacy_quality import Quality
        >>> nlp = spacy.blank(("en_core_web_sm")
        >>> nlp.add_pipe("quality")
        >>> doc = nlp("This is a test")
        >>> # extract quality metrics
        >>> doc._.quality
        >>> # check whether the document passed the quality thresholds
        >>> doc._.passed_quality_check
    """
    return Quality(
        nlp,
        name=name,
        symbols=symbols,
        contains=contains,
        top_ngram_range=top_ngram_range,
        top_ngram_min_count=top_ngram_min_count,
        duplicate_n_gram_fraction_range=duplicate_n_gram_fraction_range,
        quality_thresholds=quality_thresholds,
        force=force,
    )
