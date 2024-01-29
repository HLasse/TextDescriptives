""" Data classes used for the quality component."""

from typing import Any, Dict, Optional, Tuple, Union

from pydantic import BaseModel, Extra, Field

Interval = Tuple[Optional[float], Optional[float]]


class ThresholdsOutput(BaseModel):
    """An output which contains an three items. 1) a thresholds which is either
    an interval or a accepted boolean value. 2) a value which is the value of
    the metric. 3) a boolean which is True if the value is within the
    thresholds.

    Example:
        >>> t_out = ThresholdsOutput(threshold=(0, 2), value=2)
        >>> t_out
        ThresholdsOutput(value=2.0, passed=True, threshold=(0.0, 2.0))
        >>> t_out.passed
        True
    """

    class Config:
        extra = Extra.forbid

    threshold: Union[Interval, bool, None]
    value: Union[float, None]

    @property
    def passed(self) -> Optional[bool]:
        """Return True if the value is within the thresholds."""
        if self.value is None:
            return None
        if self.threshold is None:
            return True
        if isinstance(self.threshold, bool):
            return self.threshold == self.value
        lower, upper = self.threshold
        return (lower is None or lower <= self.value) and (
            upper is None or self.value <= upper
        )

    def __repr_str__(self, join_str: str) -> str:
        value = round(self.value, 2) if isinstance(self.value, float) else self.value
        return join_str.join(
            repr(v) if a is None else f"{a}={v!r}"
            for a, v in [
                ("value", value),
                ("passed", self.passed),
                ("threshold", self.threshold),
            ]
        )

    def __eq__(self, other: Any) -> bool:
        if isinstance(other, ThresholdsOutput):
            return self.value == other.value and self.threshold == other.threshold
        return self.value == other


class QualityThresholds(BaseModel):
    """Thresholds for quality metrics."""

    class Config:
        extra = Extra.forbid

    n_stop_words: Interval = Field(
        (2, None),
        description="A Range for the number of stop words. Default: (2, None), i.e. "
        + "at least 2 stop words, but no upper limit.",
    )
    alpha_ratio: Interval = Field(
        (0.7, None),
        description="A Range for the alpha ratio. Default: (0.7, None), i.e. at "
        + r"least 70% of tokens contain at least one alphabetic character, but no "
        + "upper limit. Note this is lowered from the original 0.8 to account for a"
        + "different definition of word boundaries. E.g. in spaCy a punctuation is"
        + "not a part of a word.",
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
    oov_ratio: Interval = Field(
        (None, 0.2),
        description="A range for the out-of-vocabulary ratio. Default: (None, 0.2)"
        + r" i.e. no lower limit, but at most 20% of words are out-of-vocabulary.",
    )


class QualityOutput(BaseModel):
    """The output of the quality function."""

    class Config:
        extra = Extra.forbid

    n_stop_words: ThresholdsOutput = Field(
        ...,
        description="The thresholds output for the number of stop words.",
    )
    alpha_ratio: ThresholdsOutput = Field(
        ...,
        description="The thresholds output for the alpha ratio.",
    )
    mean_word_length: ThresholdsOutput = Field(
        ...,
        description="The thresholds output for the mean word length.",
    )
    doc_length: ThresholdsOutput = Field(
        ...,
        description="The thresholds output for the document length.",
    )
    symbol_to_word_ratio: Dict[str, ThresholdsOutput] = Field(
        ...,
        description="The thresholds output for the symbol-to-word-ratio.",
    )
    proportion_ellipsis: ThresholdsOutput = Field(
        ...,
        description="The thresholds output for the proportion of lines ending with "
        + "ellipsis.",
    )
    proportion_bullet_points: ThresholdsOutput = Field(
        ...,
        description="The thresholds output for the proportion of lines starting with "
        + "bullet points.",
    )
    contains: Dict[str, ThresholdsOutput] = Field(
        ...,
        description="The thresholds output for the presence of strings.",
    )
    duplicate_line_chr_fraction: ThresholdsOutput = Field(
        ...,
        description="The thresholds output for the duplicate line character fraction.",
    )
    duplicate_paragraph_chr_fraction: ThresholdsOutput = Field(
        ...,
        description="The thresholds output for the duplicate paragraph character "
        + "fraction.",
    )
    duplicate_ngram_chr_fraction: Dict[str, ThresholdsOutput] = Field(
        ...,
        description="The thresholds output for the duplicate n-gram character "
        + "fraction.",
    )
    top_ngram_chr_fraction: Dict[str, ThresholdsOutput] = Field(
        ...,
        description="The thresholds output for the top n-gram character fraction.",
    )
    oov_ratio: ThresholdsOutput = Field(
        ...,
        description="The thresholds output for the out-of-vocabulary ratio.",
    )

    @property
    def passed(self) -> bool:
        """
        Returns:
            bool: Whether all thresholds have been passed.
        """
        passed_or_none = [
            self.n_stop_words.passed,
            self.alpha_ratio.passed,
            self.mean_word_length.passed,
            self.doc_length.passed,
            all(v.passed for v in self.symbol_to_word_ratio.values()),
            self.proportion_ellipsis.passed,
            self.proportion_bullet_points.passed,
            all(v.passed for v in self.contains.values()),
            self.duplicate_line_chr_fraction.passed,
            self.duplicate_paragraph_chr_fraction.passed,
            all(v.passed for v in self.duplicate_ngram_chr_fraction.values()),
            all(v.passed for v in self.top_ngram_chr_fraction.values()),
            self.oov_ratio.passed,
        ]

        return all(i is None or i for i in passed_or_none)

    def __repr_str__(self, join_str: str) -> str:
        return join_str.join(
            repr(v) if a is None else f"\n\t{a}={v!r}"
            for a, v in [
                ("passed", self.passed),
            ]
            + list(self.__repr_args__())
        )

    def to_flat_value_dict(self) -> Dict[str, Any]:
        """Creates a flat dictionary representation of the object to allow for
        easy easy conversion to a pandas DataFrame."""
        flat_dict = {"passed_quality_check": self.passed}

        for k, v in self.__dict__.items():
            if isinstance(v, dict):
                for k2, v2 in v.items():
                    flat_dict[f"{k}_{k2}"] = v2.value
            else:
                flat_dict[k] = v.value

        return flat_dict
