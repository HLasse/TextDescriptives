""" Calculate the entropy and perplexity of a corpus."""

from typing import Callable, Dict, Union

import numpy as np
from spacy.language import Language
from spacy.lookups import load_lookups
from spacy.tokens import Doc, Span
from spacy.vocab import Vocab
from wasabi import msg


def set_lexeme_prob_table(vocab: Vocab, verbose: bool = False):
    """Ensure that the pipeline has a lexeme probability table."""
    if not vocab.lookups.has_table("lexeme_prob"):
        if verbose:
            msg.info(
                "Pipeline does not have a lexeme probability table. "
                + "Will attempt to add it. This will fail if specified language does "
                + "not have a registered lexeme probability table.",
            )
        lookups = load_lookups(vocab.lang, ["lexeme_prob"])
        vocab.lookups.add_table("lexeme_prob", lookups.get_table("lexeme_prob"))


def entropy(log_probs=np.ndarray) -> float:
    """Calculates the Shannon entropy based on log probs."""
    return -np.sum(np.exp(log_probs) * log_probs)


def perplexity(entropy: float) -> float:
    """Calculates the perplexity.

    Calculated as exp(H(p)), where H is the entropy using a base e and p is the
    probabilities of a given word.
    """
    return np.exp(entropy)


def entropy_getter(doc: Union[Doc, Span], log_prob_attr: str = "prob") -> float:
    """Calculate the shannon entropy of a document."""
    log_probs = np.array([getattr(token, log_prob_attr) for token in doc])
    return entropy(log_probs)


def perplexity_getter(doc: Union[Doc, Span]) -> float:
    """Calculates the perplexity of a doc.

    Calculated as exp(H(p)), where H is the entropy using a base e and p is the
    probabilities of a given word.
    """
    # check if it has the attribute entropy
    if hasattr(doc._, "entropy") and doc._.entropy is not None:
        entropy = doc._.entropy
    else:
        entropy = entropy_getter(doc)
    return perplexity(entropy)


def per_word_perplexity_getter(doc: Union[Doc, Span]) -> float:
    """Calculates the per word perplexity of a document."""
    if hasattr(doc._, "perplexity") and doc._.perplexity is not None:
        perplexity = doc._.perplexity
    else:
        perplexity = perplexity_getter(doc)

    return perplexity / len(doc)


def set_docspan_extension(
    extension,
    getter: Callable,
    prefix: str = "",
    force: bool = False,
) -> None:
    """Set a document extension to None and set a span extension to a getter
    function."""
    if not Doc.has_extension(prefix + extension) or force:
        Doc.set_extension(prefix + extension, default=None, force=True)
    if not Span.has_extension(prefix + extension) or force:
        Span.set_extension(prefix + extension, getter=getter)


def set_entropy_and_perplexity(doc: Union[Doc, Span]) -> None:
    doc._.entropy = entropy_getter(doc)
    doc._.perplexity = perplexity_getter(doc)
    doc._.per_word_perplexity = per_word_perplexity_getter(doc)


def set_entropy_and_perplexity_to_nan(doc: Union[Doc, Span]) -> None:
    doc._.entropy = np.nan
    doc._.perplexity = np.nan
    doc._.per_word_perplexity = np.nan


class InformationTheory:
    """SpaCy component for adding information theoretic metrics such as entropy
    and perplexity."""

    def __init__(self, nlp: Language, name: str, force: bool) -> None:
        self.name = name
        self.set_extensions(force=force)
        try:
            set_lexeme_prob_table(nlp.vocab, verbose=False)
            self.has_lexeme_prob_table = True
        except ValueError:
            msg.warn(
                f"Could not load lexeme probability table for language {nlp.lang}. "
                + "This will result in NaN values for perplexity and entropy.",
            )
            self.has_lexeme_prob_table = False

    @staticmethod
    def dict_getter(doc: Union[Doc, Span]) -> Dict[str, float]:
        return {
            "entropy": doc._.entropy,
            "perplexity": doc._.perplexity,
            "per_word_perplexity": doc._.per_word_perplexity,
        }

    @staticmethod
    def set_extensions(force: bool) -> None:
        """Add entropy and perplexity as attributes to a document."""
        for ext, getter in [
            ("entropy", entropy_getter),
            ("perplexity", perplexity_getter),
            ("per_word_perplexity", per_word_perplexity_getter),
            ("information_theory", InformationTheory.dict_getter),
        ]:
            set_docspan_extension(
                ext,
                getter=getter,  # type: ignore
                prefix="",
                force=force,
            )

    def __call__(self, doc: Doc) -> Doc:
        if self.has_lexeme_prob_table:
            set_entropy_and_perplexity(doc)
        else:
            set_entropy_and_perplexity_to_nan(doc)
        doc._.information_theory = InformationTheory.dict_getter(doc)
        return doc


@Language.factory(
    "textdescriptives/information_theory",
    assigns=[
        "doc._.entropy",
        "doc._.perplexity",
        "doc._.per_word_perplexity",
        "span._.entropy",
        "span._.perplexity",
        "span._.per_word_perplexity",
    ],
)
def create_information_theory_component(nlp: Language, name: str) -> InformationTheory:
    """
    Allows the InformationTheory component to be added to the spaCy pipeline using the
    command: `nlp.add_pipe('textdescriptives/information_theory')`

    It also set the following attributes on the document and span:

    - {Doc/Span}._.entropy: The shannon entropy of the document.
    - {Doc/Span}._.perplexity: The perplexity of the document.
    - {Doc/Span}._.per_word_perplexity: The per word perplexity of the document.
    - {Doc/Span}._.information_theory: A dictionary with the
        keys: entropy, perplexity, and per_word_perplexity.

    Args:
        - nlp: The spaCy Language object.
        - name: The name of the component.

    Example:
        >>> import spacy
        >>> nlp = spacy.blank('en_core_web_lg')
        >>> nlp.add_pipe('textdescriptives/information_theory')
        >>> doc = nlp('This is a sentence.')
        >>> doc._.information_theory
        {'entropy': ...
    """
    return InformationTheory(nlp, name, force=False)
