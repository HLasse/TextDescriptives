""" Component for calculating quality metrics."""

from collections import Counter, defaultdict
from typing import Callable, Dict, List, Mapping, Optional, Tuple, Union

import numpy as np
from spacy.language import Language
from spacy.tokens import Doc, Span

from .quality_data_classes import QualityOutput, QualityThresholds, ThresholdsOutput


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
    """The percentage of spacy tokens in this document which contains at
    least one alphabetic character.

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


def oov_ratio(span: Union[Span, Doc], vocab: Optional[Mapping] = None) -> float:
    """Calculates the out-of-vocabulary ratio.

    Args:
        span (Union[Span, Doc]): A spaCy Span or Doc object.
        vocab (Optional[Mapping], optional): A vocabulary to check against.
            If None, will use the spaCy vocab. Note that the spaCy vocab
            is not defined for small models. Defaults to None.

    Returns:
        float: the out-of-vocabulary ratio
    """
    len_span = len(span)
    if len_span == 0:
        return 0.0
    if vocab is None:
        return len([token for token in span if token.is_oov]) / len_span
    return len([token for token in span if token.text not in vocab]) / len_span


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
        vocab: Optional[Mapping],
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
        self.vocab = vocab

        self.set_extensions()

    def quality_setter(
        self,
        span: Union[Span, Doc],
    ) -> QualityOutput:
        """Apply quality functions to doc.

        Args:
            span (Union[Span, Doc]): spaCy span or doc object

        Returns:
            QualityOutput: The quality metrics
        """
        threshold = self.quality_thresholds

        thresholds_outputs: Dict[
            str,
            Union[Dict[str, ThresholdsOutput], ThresholdsOutput],
        ] = {}
        # filter with only one threshold
        getters = {
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
        }

        for name, getter in getters.items():
            thresholds_outputs[name] = ThresholdsOutput(
                value=getter(span),  # type: ignore
                threshold=getattr(threshold, name),
            )

        thresholds_outputs["contains"] = {
            string: ThresholdsOutput(
                value=contains_string(span, string),
                threshold=threshold.contains.get(string, None),
            )
            for string in self.contains
        }
        thresholds_outputs["symbol_to_word_ratio"] = {
            symbol: ThresholdsOutput(
                value=symbol_to_word_ratio(span, symbol),
                threshold=threshold.symbol_to_word_ratio.get(symbol, None),
            )
            for symbol in self.symbols
        }

        chr_frac = top_ngram_chr_fraction(
            span,
            ngram_range=self.top_ngram_range,
            min_count=self.top_ngram_min_count,
        )

        thresholds_outputs["top_ngram_chr_fraction"] = {
            str(n_gram): ThresholdsOutput(
                value=frac,
                threshold=threshold.top_ngram_chr_fraction.get(
                    str(n_gram),
                    (None, None),
                ),
            )
            for n_gram, frac in chr_frac.items()
        }

        duplicate_ngram_chr_fraction = duplicate_ngram_fraction(
            span,
            ngram_range=self.duplicate_n_gram_fraction_range,
        )
        thresholds_outputs["duplicate_ngram_chr_fraction"] = {
            str(n_gram): ThresholdsOutput(
                value=frac,
                threshold=threshold.duplicate_ngram_chr_fraction.get(
                    str(n_gram),
                    (None, None),
                ),
            )
            for n_gram, frac in duplicate_ngram_chr_fraction.items()
        }

        # add oov_ratio if spacy model is not small or has a vocab
        # vector length is 0 for small models
        if span.vocab.vectors_length > 0 or self.vocab:
            value_oov = oov_ratio(span, self.vocab)
            thresholds_oov = threshold.oov_ratio
        else:
            value_oov = None
            thresholds_oov = (None, None)

        thresholds_outputs["oov_ratio"] = ThresholdsOutput(
            value=value_oov,
            threshold=thresholds_oov,
        )

        return QualityOutput(**thresholds_outputs)

    def quality_getter(self, span: Union[Span, Doc]) -> QualityOutput:
        """Get quality metrics from doc.

        Args:
            span (Union[Span, Doc]): spaCy span or doc object

        Returns:
            QualityOutput: The quality metrics
        """
        if not hasattr(span._, "_quality"):
            return self.quality_setter(span)
        return QualityOutput(**span._._quality)

    def set_quality(self, doc: Doc) -> None:
        """Set the quality attribute on a doc.

        Args:
            doc (Doc): spaCy doc object
        """
        # to allow the variable to json serializable we convert it to json
        # it is then converted back into a quality output object in the getter

        doc._._quality = self.quality_setter(doc).dict()
        doc._.passed_quality_check = self.passed_quality_thresholds(doc)

    def passed_quality_thresholds(self, span: Union[Span, Doc]) -> bool:
        """Check if a span passes the quality thresholds.

        Args:
            span (Union[Span, Doc]): spaCy span or doc object

        Returns:
            bool: True if span passes quality thresholds
        """
        quality_output = self.quality_getter(span)
        return quality_output.passed

    def set_extensions(self):
        """Set required extensions."""
        ext_name = "passed_quality_check"
        if not Span.has_extension(ext_name) or self.force is True:
            Span.set_extension(
                ext_name,
                getter=self.passed_quality_thresholds,
                force=True,
            )
        if not Doc.has_extension(ext_name) or self.force is True:
            Doc.set_extension(
                ext_name,
                getter=self.passed_quality_thresholds,
                force=True,
            )

        ext_name = "quality"
        if not Doc.has_extension(ext_name) or self.force is True:
            Doc.set_extension(ext_name, getter=self.quality_getter, force=True)
            Doc.set_extension("_" + ext_name, default=None, force=True)
        if not Span.has_extension(ext_name) or self.force is True:
            Span.set_extension(ext_name, getter=self.quality_getter, force=True)
            Span.set_extension("_" + ext_name, default=None, force=True)

    def set_quality_thresholds(self, thresholds: QualityThresholds) -> None:
        """Sets the quality thresholds.

        Args:
            thresholds (QualityThresholds): The desired quality thresholds.
        """
        self.quality_thresholds = thresholds

    def __call__(self, doc: Doc):
        """Run the pipeline component."""
        self.set_quality(doc)
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
        "vocab": None,
        "force": True,
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
    vocab: Optional[Mapping],
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
        vocab (Optional[Mapping]): vocabulary to use for calculating the
            out-of-vocabulary ratio (`oov_ratio`). If None, will use the vocabulary
            of the spaCy model. Note, that small spaCy models do not have a
            vocabulary. The attribute will only be set if the vocabulary is not
            None or the spaCy model is medium or large.
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
    return Quality(
        nlp,
        name=name,
        symbols=symbols,
        contains=contains,
        top_ngram_range=top_ngram_range,
        top_ngram_min_count=top_ngram_min_count,
        duplicate_n_gram_fraction_range=duplicate_n_gram_fraction_range,
        quality_thresholds=None,
        vocab=vocab,
        force=force,
    )
