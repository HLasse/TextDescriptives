"""Calculation of various readability metrics."""
from collections import Counter, defaultdict
from functools import partial
from typing import Callable, Dict, List, Tuple, Union

import numpy as np
from spacy.language import Language
from spacy.tokens import Doc, Span

from textdescriptives.components.utils import span_getter_to_doc_getter


def n_stop_words(span: Span) -> int:
    """Count the number of stop words in a document.

    Args:
        span (Span): spaCy span object

    Returns:
        int: number of stop words
    """
    return len([t for t in span if t.is_stop])


def mean_word_length(span: Span) -> float:
    """Calculate the mean word length of a document.

    Args:
        span (Span): spaCy span object

    Returns:
        float: mean word length
    """
    return np.mean([len(t) for t in span])


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

    return np.mean([contains_alpha(t) for t in span])


def proportion_bullet_points(  # pylint: disable=dangerous-default-value
    span: Span, bullet_point: set = {"-", "*"}
) -> float:
    """Calculate the proportion of lines which start with a bullet points in a span.

    Args:
        span (Span): spaCy span object

    Returns:
        float: proportion of bullet points
    """
    lines = span._.lines
    return np.mean([line.strip().startswith(bullet_point) for line in lines])


def proportion_ellipsis(  # pylint: disable=dangerous-default-value
    span: Span, ellipsis: set = {"…", "..."}
) -> float:
    """Calculate the proportion line which ends with an ellipsis in a span.

    Args:
        span (Span): spaCy span object

    Returns:
        float: proportion of ellipsis
    """
    lines = span._.lines
    return np.mean([line.strip().endswith(ellipsis) for line in lines])


def duplicate_line_fraction(span: Span) -> float:
    """Calculate the proportion of of characters within duplicate lines.

    Args:
        span (Span): spaCy span object

    Returns:
        float: proportion of characters within a duplicate lines
    """
    lines = span._.lines
    unique_lines = set(lines)
    return 1 - len(unique_lines) / len(lines)


def duplicate_chr_fraction_getter(doc: Doc, attr: str) -> float:
    """Calculate the character fraction of duplicates based on a counter object.
    Args:
        doc (Doc):
            A spaCy Doc.
        attr (str):
            The document attribute to extract.
    Returns:
        float:
            The fraction of duplicate characters.
    """
    counter = getattr(doc._, attr)
    duplicate_chr = 0
    for t, c in counter.items():
        if c > 1:
            duplicate_chr += len(t) * (c - 1)
    frac = duplicate_chr / doc._.chr_len
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
    return n_symbol / len([t for t in span if not (t.is_space or t.is_punct)])


def duplicate_ngram_fraction(
    span: Span,
    ngram_range: Tuple[int, int],
) -> Dict[int, float]:
    """calculates the character fraction of duplicate n-gram over the overall text,
    taking care not to count overlapping n-grams twice.

    Args:
        span (Span): spaCy span object
        ngram_range (Tuple[int, int], optional): The n-gram range.

    Returns:
        Dict[int, float]: the fraction of duplicate characters for each
            n-gram size
    """
    lower, upper = ngram_range

    # calcuate maximum chr. limits according to thresholds
    ngrams = defaultdict(set)
    duplicate_char = defaultdict(int)
    minmax = defaultdict(lambda: [0, 0])
    max_len = len(span)

    for i, _ in enumerate(span):
        for ngram_size in range(lower, upper + 1):

            min_, max_ = minmax[ngram_size]
            end = i + ngram_size

            if end < max_len:
                span = span[i:end]
                ngram = span.text.lower()  # create n-gram from span

                if ngram in ngrams[ngram_size]:
                    # if it doesn't overlap with other ngrams of the same size
                    # update
                    if span.start_char > max_:
                        duplicate_char[ngram_size] += max_ - min_
                        minmax[ngram_size] = [span.start_char, span.end_char]
                    else:
                        # extend range of duplicates
                        minmax[ngram_size][1] = span.end_char
                else:
                    ngrams[ngram_size].add(ngram)

    # empty buffer for of duplicate chr. which have yet to be added.
    for ngram_size in range(lower, upper + 1):
        min_, max_ = minmax[ngram_size]
        duplicate_char[ngram_size] += max_ - min_

    return duplicate_char


def n_gram_counter(span: Span, ngram_range: Tuple[int, int]) -> Dict[str, Counter]:
    """Calculate the counts of n-grams in the specified range.
    Args:
        span (Span): spaCy span object
        ngram_range (Tuple[int, int]): The n-gram range.
    Returns:
        Dict[str, Counter]: Dict with str keys and Counter values. A dictionary
            containing the counts of n-grams for a specific n.
    """
    max_len = len(span)
    lower, upper = ngram_range
    shingles_count = defaultdict(Counter)
    for i, _ in enumerate(span):
        for ngram_size in range(lower, upper + 1):
            end = i + ngram_size
            if end < max_len:
                span = span[i:end]
                shingles_count[ngram_size][span.text.lower()] += 1
    return shingles_count


def top_ngram_chr_fraction(
    span: Span,
    ngram_range: Tuple[int, int],
) -> float:
    """Calculated whether the character fraction of the top n-grams is below the
    given thresholds

    Args:
        span (Span): spaCy span object
        ngram_range (Tuple[int, int], optional): Range of n grams to examine.

    Returns:
        float: The fraction of the top n-grams.
    """
    ngram_counter = n_gram_counter(span, ngram_range=ngram_range)
    top_ngram_chr_frac = {}
    for n in zip(ngram_counter):
        ngram, count = ngram_counter[n].most_common(1)[0]
        top_ngram_chr_frac[n] = len(ngram) * count / span._.chr_len
        top_ngram_chr_frac = len(ngram) * count / span._.chr_len


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
        symbols: List[str] = ["#"],
        contains=["lorem ipsum"],
        duplicate_n_gram_fraction_range: Tuple[int] = [5, 10],
        force: bool = False,
    ):  # noqa: D107
        """Initialise components"""
        self.name = name
        self.force = force

        duplicate_lines_chr_fraction = partial(
            duplicate_chr_fraction_getter, attr="lines_counter"
        )
        duplicate_paragraph_chr_fraction = partial(
            duplicate_chr_fraction_getter, attr="paragraphs_counter"
        )

        self.extensions = {
            "lines": lambda span: span.text.split("\n"),
            "paragrahs": lambda span: span.text.split("\n\n"),
            "lines_counter": lambda span: Counter(span._.lines),
            "paragraphs_counter": lambda span: Counter(span._.paragraphs),
            "chr_len": lambda span: len(span.text),
        }

        self.getters = {
            # heuristic quality filters
            "n_stop_words": n_stop_words,
            "alpha_ratio": alpha_ratio,
            "mean_word_length": mean_word_length,
            "proportion_ellipsis": proportion_ellipsis,
            "proportion_bullet_points": proportion_bullet_points,
            # text repetition
            "duplicate_lines_chr_fraction": duplicate_lines_chr_fraction,
            "duplicate_paragraph_chr_fraction": duplicate_paragraph_chr_fraction,
            "duplicate_ngram_chr_fraction": partial(
                duplicate_ngram_fraction, ngram_range=duplicate_n_gram_fraction_range
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

        self.set_extensions()

        if not Span.has_extension("quality") or force:
            Span.set_extension("quality", getter=self.quality_getter, force=force)
        if not Doc.has_extension("quality") or force:
            Doc.set_extension(
                "quality",
                getter=span_getter_to_doc_getter(self.quality_getter),
                force=force,
            )

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
                    quality[f"{n_gram}_gram_chr_fraction"] = frac
            if name == "duplicate_ngram_chr_fraction":
                chr_frac = getter(span)
                for n_gram, frac in chr_frac.items():
                    quality[f"{n_gram}_gram_duplicate_chr_fraction"] = frac

            quality[name] = getter(span)
        return quality

    def set_extensions(self):
        """Set required extensions."""

        for ext_name, span_getter in self.extensions.items():
            doc_getter = span_getter_to_doc_getter(span_getter)

            if not Span.has_extension(ext_name) or self.force is True:
                Span.set_extension(ext_name, getter=span_getter)
            if not Doc.has_extension(ext_name) or self.force is True:
                Doc.set_extension(ext_name, getter=doc_getter)


@Language.factory("quality")
def create_quality_component(
    nlp: Language, name: str, force: bool = False
) -> Callable[[Doc], Doc]:
    """Allows Quality to be added to a spaCy pipe using nlp.add_pipe("quality").

    Set the following extensions:
        - {Span/Doc}._.quality
        - {Span/Doc}._.lines
        - {Span/Doc}._.paragraphs
        - {Span/Doc}._.lines_counter
        - {Span/Doc}._.paragraphs_counter
        - {Span/Doc}._.chr_len

    Where the last are used to calculate some of the quality metrics. The can be
    overwritten if you e.g. wish lines to be split on "\\r\\n" instead of "\\n".

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

    Returns:
        Quality: the spaCy component
    """
    return Quality(nlp, name=name, force=force)
