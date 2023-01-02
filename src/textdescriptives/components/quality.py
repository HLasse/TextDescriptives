"""Component for calculating quality metrics."""
from collections import Counter, defaultdict
from functools import partial
from typing import Callable, Dict, List, Optional, Tuple, Union

import numpy as np
from pydantic import BaseModel, Field
from spacy.language import Language
from spacy.tokens import Doc, Span

Interval = Tuple[Optional[float], Optional[float]]


class QualityThresholds(BaseModel):
    """Thresholds for quality metrics."""

    n_stop_words: Interval = Field(
        (2, None),
        description="A Range for the number of stop words. Default: (2, None), i.e. "
        + "at least 2 stop words, but no upper limit.",
    )
    alpha_ratio: Interval = Field(
        (0.8, None),
        description="A Range for the alpha ratio. Default: (0.8, None), i.e. at "
        + r"least 80% of tokens contain at least one alphabetic character, but no "
        + "upper limit.",
    )
    mean_word_length: Interval = Field(
        (3, 10),
        description="A Range for the mean word length. Default: (3, 10), i.e. between"
        + " 3 and 10 characters.",
    )
    doc_length: Interval = Field(
        (10, 100_000),
        description="A Range for the document length. Default: (10, 100_000), i.e."
        + " between 10 and 100_000 characters.",
    )
    symbol_to_word_ratio: Dict[str, Interval] = Field(
        {"#": (None, 0.1)},
        description="A dict of symbols and the allowed range for the "
        + r"symbol-to-word-ratio. The symbol-to-word-ratio is the ratio between symbol"
        + "occurrence and word occurrence. Defaults to {'#': (None, 0.1)} i.e. no lower"
        + r" limit, but there must at most be a ratio of 0.1 between the number of of "
        + "words and hashtags. i.e. if we have 100 words the symbol should appear no "
        + "more than 10 times. Values not in the dict are not checked.",
    )
    proportion_ellipsis: Interval = Field(
        (None, 0.3),
        description="A Range for the proportion of lines which end with ellipsis. "
        + "Default: (None, 0.3), "
        + r"i.e. no lower limit, but at most 30% of lines end with an ellipsis.",
    )
    proportion_bullet_points: Interval = Field(
        (None, 0.8),
        description="A Range for the proportion lines which start with a bullet "
        + r"points. Default: (None, 0.8), i.e. no lower limit, but at most 80% of lines"
        + " start with a bullet point.",
    )
    contains: Dict[str, bool] = Field(
        {"lorem ipsum": False},
        description="A dictionary of strings and whether they should be contained in "
        + "the document. Default: {'lorem ipsum': False}, i.e. the document should not"
        + " contain the string 'lorem ipsum'.",
    )
    duplicate_line_chr_fraction: Interval = Field(
        (None, 0.2),
        description="A Range for the duplicate line character fraction. Default: "
        + r"(None, 0.2), i.e. no lower limit, but at most 20% of characters are"
        + " duplicates.",
    )
    duplicate_paragraph_chr_fraction: Interval = Field(
        (None, 0.2),
        description="A Range for the duplicate paragraph character fraction. Default:"
        + r" (None, 0.2), i.e. no lower limit, but at most 20% of characters are "
        + "duplicates.",
    )
    duplicate_ngram_chr_fraction: Dict[str, Interval] = Field(
        {
            "5": (None, 0.15),
            "6": (None, 0.14),
            "7": (None, 0.13),
            "8": (None, 0.12),
            "9": (None, 0.11),
            "10": (None, 0.1),
        },
        description="A dictionary of n-gram lengths and the allowed range for the "
        + "duplicate n-gram character fraction. Default: {5: (None, 0.15), 6: (None, "
        + "0.14), 7: (None, 0.13), 8: (None, 0.12), 9: (None, 0.11), 10: (None, 0.1)}, "
        + r"i.e. no lower limit, but at most 15% of characters are duplicates for "
        + r"5-grams, 14% for 6-grams, 13% for 7-grams, 12% for 8-grams, 11% for 9-grams"
        + r" and 10% for 10-grams.",
    )
    top_ngram_chr_fraction: Dict[str, Interval] = Field(
        {
            "2": (None, 0.2),
            "3": (None, 0.18),
            "4": (None, 0.16),
        },
        description="A dictionary of n-gram lengths and the allowed range for the "
        + "top n-gram character fraction. Default: {2: (None, 0.2), 3: (None, 0.18)"
        + r", 4: (None, 0.16)}, i.e. no lower limit, but at most 20% of characters "
        + r"are contained within a duplicate for 2-grams, 18% for 3-grams and 16% "
        + "for 4-grams.",
    )


def n_stop_words(span: Union[Doc, Span]) -> int:
    """Count the number of stop words in a document.

    Args:
        span (Union[Doc, Span]): A spaCy Doc or Span object

    Returns:
        int: number of stop words
    """
    return sum(t.is_stop for t in span)


def mean_word_length(span: Union[Doc, Span]) -> float:
    """Calculate the mean word length of a document.

    Args:
        span (Union[Doc, Span]): A spaCy Doc or Span object

    Returns:
        float: mean word length
    """
    tokens_lengths = [len(t) for t in span]
    if tokens_lengths:
        return float(np.mean(tokens_lengths))
    return 0.0


def alpha_ratio(span: Union[Doc, Span]) -> float:
    """The percentage of spacy tokens in this document which contain at leat
    one alphabetic character.

    Args:
        span (Union[Doc, Span]): A spaCy Doc or Span object

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
    span: Union[Doc, Span],
    bullet_point: set = {"-", "*"},
) -> float:
    """Calculate the proportion of lines which start with a bullet points in a
    span.

    Args:
        span (Union[Doc, Span]): A spaCy Doc or Span object
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
    span: Union[Doc, Span],
    ellipsis: set = {"…", "..."},
) -> float:
    """Calculate the proportion line which ends with an ellipsis in a span.

    Args:
        span (Union[Doc, Span]): A spaCy Doc or Span object
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
    """Get ranges that evaluate to true a from boolean array, i.e.

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


def duplicate_paragraph_chr_fraction(span: Union[Doc, Span]) -> float:
    """Calculate the character fraction of duplicate paragraphs.

    Args:
        span (Union[Doc, Span]): A spaCy Doc or Span object

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


def duplicate_line_chr_fraction(span: Union[Doc, Span]) -> float:
    """Calculate the character fraction of duplicate lines.

    Args:
        span (Union[Doc, Span]): A spaCy Doc or Span object

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


def symbol_to_word_ratio(span: Union[Span, Doc], symbol: str) -> float:
    """Calculate the ratio of symbols to words in a span.

    Args:
        span (Union[Span, Doc]): spaCy Span or Doc object
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


def span_ngrams(
    span: Union[Span, Doc],
    ngram_range: Tuple[int, int],
) -> Dict[int, Dict[str, Union[int, List[Span]]]]:
    """Calculates the counts of n-grams in the specified range.

    Args:
        span (Union[Span, Doc]): A spaCy Span or Doc object.
        ngram_range (Tuple[int, int]): The n-gram range.

    Returns:
        Dict[int, Dict[str, Union[int, List[Span]]]]: A dictionary that for each n in
            the ngram range contains the counts of the n-grams as well as the spans of
            the n-grams.
    """
    max_len = len(span)
    lower, upper = ngram_range
    shingles_count = {  # type: ignore
        n: defaultdict(lambda: {"count": 0, "span": []})
        for n in range(lower, upper + 1)
    }
    for i, _ in enumerate(span):
        for ngram_size in range(lower, upper + 1):
            end = i + ngram_size
            if not end > max_len:
                ngram_span = span[i:end]
                ngram = ngram_span.text
                shingles_count[ngram_size][ngram]["count"] += 1  # type: ignore
                shingles_count[ngram_size][ngram]["span"].append(  # type: ignore
                    ngram_span,
                )
    return shingles_count  # type: ignore


def duplicate_ngram_fraction(
    span: Union[Span, Doc],
    ngram_range: Tuple[int, int],
) -> Dict[int, float]:
    """Calculates the character fraction of duplicate n-gram over the overall
    text, taking care not to count overlapping n-grams twice. This does not
    include spaces between the n-grams.

    Args:
        span (Union[Span, Doc]): A spaCy Span or Doc object.
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
            if count["count"] > 1:  # type: ignore
                for ngram_span in count["span"]:  # type: ignore
                    is_duplicate[ngram_span.start : ngram_span.end] = True

        duplicate_chars = 0
        # get duplicate ranges from boolean array
        for start, end in get_ranges(is_duplicate):
            _span = span[start:end]
            duplicate_chars += _span.end_char - _span.start_char
        duplicate_chr_fraction[ngram_size] = duplicate_chars / chr_len
    return duplicate_chr_fraction


def top_ngram_chr_fraction(
    span: Union[Doc, Span],
    ngram_range: Tuple[int, int],
    min_count: int = 0,
) -> Dict[int, float]:
    """Calculates the character fraction of the top ngrams.

    Args:
        span (Union[Span, Doc]): A spaCy Span or Doc object.
        ngram_range (Tuple[int, int], optional): Range of n grams to examine.
        min_count (int): Minimum count of n-grams to before an n-gram is considered
            a top n-gram. Defaults to 0.

    Returns:
        Dict[int, float]: the fraction of duplicate characters for each
            n-gram size
    """
    # check if span has enough tokens within the range

    chr_len = len(span.text)
    if chr_len == 0:
        return {n: 0.0 for n in range(ngram_range[0], ngram_range[1] + 1)}

    ngram_counter = span_ngrams(span, ngram_range=ngram_range)
    top_ngram_chr_frac = {}
    for n in ngram_counter:
        # find the top n-gram
        if ngram_counter[n]:
            ngram, count_span = max(
                ngram_counter[n].items(),
                key=lambda x: x[1]["count"],  # type: ignore
            )
            count = count_span["count"]  # type: ignore
            if count >= min_count:
                # calculate the fraction of the top n-gram
                top_ngram_chr_frac[n] = (len(ngram) * count) / chr_len
            else:
                top_ngram_chr_frac[n] = 0.0
        else:
            top_ngram_chr_frac[n] = 0.0

    return top_ngram_chr_frac


def contains_string(span: Union[Span, Doc], string: str) -> bool:
    """Check if a span contains a string.

    Args:
        span (Union[Span, Doc]): A spaCy Span or Doc object.
        string (str): string to check for

    Returns:
        bool: True if span contains string
    """
    return string in span.text


class Quality:
    """spaCy component for adding text quality metrics to the `Doc` and `Span`
    objects.

    Extracts metrics and returns them as a dictionary as the ._.quality
    attribute.
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
        quality_thresholds: Optional[QualityThresholds] = None,
        force: bool = False,
    ):  # noqa: D107
        """Initialise components."""
        self.name = name
        self.force = force
        self.symbols = symbols
        self.contains = contains
        self.top_ngram_range = top_ngram_range
        self.top_ngram_min_count = top_ngram_min_count
        self.duplicate_n_gram_fraction_range = duplicate_n_gram_fraction_range
        if quality_thresholds is None:
            quality_thresholds = QualityThresholds()
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
                duplicate_ngram_fraction,
                ngram_range=duplicate_n_gram_fraction_range,
            ),
            "top_ngram_chr_fraction": partial(
                top_ngram_chr_fraction,
                ngram_range=top_ngram_range,
                min_count=top_ngram_min_count,
            ),
        }
        # add symbol to word ratio
        for symbol in symbols:
            self.getters[f"symbol_{symbol}_to_word_ratio"] = partial(
                symbol_to_word_ratio,
                symbol=symbol,
            )
        # add contains
        for string in contains:
            self.getters[f"contains_{string}"] = partial(contains_string, string=string)

        self.extensions = {
            "passed_quality_check": self.passed_quality_thresholds,
            "quality": self.quality_getter,
        }

        self.set_extensions()

    def quality_getter(self, span: Span) -> Dict[str, Union[float, int, bool]]:
        """Apply quality functions to doc.

        Args:
            span (Span): spaCy span object

        Returns:
            Dict[str, Union[float, int, bool]]: dictionary of quality metrics
        """
        quality = {}
        for name, getter in self.getters.items():
            if name == "top_ngram_chr_fraction":
                chr_frac = getter(span)  # type: ignore
                for n_gram, frac in chr_frac.items():
                    quality[f"top_{n_gram}-gram_chr_fraction"] = frac
            elif name == "duplicate_ngram_chr_fraction":
                chr_frac = getter(span)  # type: ignore
                for n_gram, frac in chr_frac.items():
                    quality[f"duplicate_{n_gram}-gram_chr_fraction"] = frac
            else:
                quality[name] = getter(span)  # type: ignore
        return quality

    @staticmethod
    def is_within_range(rangetuple: Interval, value: float) -> bool:
        """Check if a value is within a range tuple. If one of the values in
        the range tuple is None it is considered to be unbounded.

        Args:
            rangetuple (Interval): range tuple
            value (float): value to check

        Returns:
            bool: True if value is within range
        """
        return (rangetuple[0] is None or rangetuple[0] <= value) and (
            rangetuple[1] is None or value <= rangetuple[1]
        )

    def passed_quality_thresholds(self, span: Span) -> bool:
        """Checks whether a span passed the quality thresholds."""
        quality = span._.quality
        qt = self.quality_thresholds

        # heuristic quality filters
        if not self.is_within_range(qt.n_stop_words, quality["n_stop_words"]):
            return False
        if not self.is_within_range(qt.alpha_ratio, quality["alpha_ratio"]):
            return False
        if not self.is_within_range(qt.mean_word_length, quality["mean_word_length"]):
            return False
        if not self.is_within_range(qt.doc_length, quality["doc_length"]):
            return False
        if not self.is_within_range(
            qt.proportion_ellipsis,
            quality["proportion_ellipsis"],
        ):
            return False
        if not self.is_within_range(
            qt.proportion_bullet_points,
            quality["proportion_bullet_points"],
        ):
            return False

        for symbol in self.symbols:
            if symbol in qt.symbol_to_word_ratio:
                if not self.is_within_range(
                    qt.symbol_to_word_ratio[symbol],
                    quality[f"symbol_{symbol}_to_word_ratio"],
                ):
                    return False

        for string in self.contains:
            if string in qt.contains and (
                qt.contains[string] is not quality[f"contains_{string}"]
            ):
                return False

        # text repetition
        if not self.is_within_range(
            qt.duplicate_line_chr_fraction,
            quality["duplicate_line_chr_fraction"],
        ):
            return False
        if not self.is_within_range(
            qt.duplicate_paragraph_chr_fraction,
            quality["duplicate_paragraph_chr_fraction"],
        ):
            return False

        for ngram in qt.duplicate_ngram_chr_fraction:
            key = f"duplicate_{ngram}-gram_chr_fraction"
            if key in quality:
                if not self.is_within_range(
                    qt.duplicate_ngram_chr_fraction[ngram],
                    quality[key],
                ):
                    return False

        for n_gram in qt.top_ngram_chr_fraction:
            if n_gram in quality:
                if not self.is_within_range(
                    qt.top_ngram_chr_fraction[n_gram],
                    quality[n_gram],
                ):
                    return False

        return True

    def set_extensions(self):
        """Set required extensions."""

        for ext_name, span_getter in self.extensions.items():
            # doc_getter = span_getter_to_doc_getter(span_getter)

            if not Span.has_extension(ext_name) or self.force is True:
                Span.set_extension(ext_name, getter=span_getter, force=True)
            if not Doc.has_extension(ext_name) or self.force is True:
                Doc.set_extension(ext_name, getter=span_getter, force=True)

    def __call__(self, doc: Doc):
        """Run the pipeline component."""
        return doc


@Language.factory(
    "textdescriptives/quality",
    assigns=[
        "doc._.quality",
        "doc._.passed_quality_check",
        "span._.quality",
        "span._.passed_quality_check",
    ],
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
def create_quality_component(
    nlp: Language,
    name: str,
    symbols: List[str],
    contains: List[str],
    top_ngram_range: Tuple[int, int],
    top_ngram_min_count: int,
    duplicate_n_gram_fraction_range: Tuple[int, int],
    quality_thresholds: Optional[dict] = None,
    force: bool = True,
) -> Callable[[Doc], Doc]:
    """Allows Quality to be added to a spaCy pipe using
    nlp.add_pipe("textdescriptives/quality").

    Adding this component to a pipeline sets the following attributes:

    - {Span/Doc}._.quality
    - {Span/Doc}._.passed_quality_check

    It also sets:

    - {Span/Doc}._.lines
    - {Span/Doc}._.paragraphs

    These are used to calculate some of the quality metrics. They can be overwritten if
    you e.g. wish lines to be split on "\\r\\n" instead of "\\n".

    A large part of the quality metrics were proposed by [1] and [2] for filtering
    out low quality text from large text corpora.

    References:
    - [1] Rae, J. W., Borgeaud, S., Cai, T., Millican, K., Hoffmann, J., Song, F., ... &
    Irving, G. (2021). Scaling language models: Methods, analysis & insights from
    training gopher. arXiv preprint arXiv:2112.11446.
    - [2] Raffel, C., Shazeer, N., Roberts, A., Lee, K., Narang, S., Matena, M., ... &
    Liu, P. J. (2020). Exploring the limits of transfer learning with a unified
    text-to-text transformer. J. Mach. Learn. Res., 21(140), 1-67.

    Args:
        nlp (Language): spaCy language object, does not need to be specified in the
            nlp.add_pipe call.
        name (str): name of the component. Can be optionally specified in the
            nlp.add_pipe call, using the name argument.
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
        quality_thresholds (Optional[dict]): A dictionary object containing the
            thresholds indicated by either an interval (Tuple) or a boolean. We
            recommend using the QualityThresholds class to create this dictionary by
            calling QualityThresholds(...).dict(). This ensures that all the thresholds
            are validated. Defaults to None in which case the default for
            QualityThresholds is used.
        force (bool): whether to overwrite existing extensions. Defaults to True.


    Returns:
        Callable[[Doc], Doc]: the Quality component

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
    # recons quality_thresholds since it needs to be json serializable for the config
    # in the nlp.add_pipe call
    if quality_thresholds is not None:
        quality_thresholds_ = QualityThresholds(**quality_thresholds)
    else:
        quality_thresholds_ = None

    return Quality(
        nlp,
        name=name,
        symbols=symbols,
        contains=contains,
        top_ngram_range=top_ngram_range,
        top_ngram_min_count=top_ngram_min_count,
        duplicate_n_gram_fraction_range=duplicate_n_gram_fraction_range,
        quality_thresholds=quality_thresholds_,
        force=force,
    )
