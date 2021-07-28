"""Adds all components to a spaCy pipeline"""
from .components import (
    Readability,
    DependencyDistance,
    DescriptiveStatistics,
)

from spacy.language import Language
from spacy.tokens import Doc


@Language.factory("textdescriptives")
def create_textdescriptives_component(nlp: Language, name: str):
    for component in [
        "descriptive_stats",
        "readability",
        "dependency_distance",
    ]:
        nlp.add_pipe(component, last=True)
    return TextDescriptives(nlp)


class TextDescriptives:
    """
    Utility spaCy v3.0 component to add all functionality from the TextDescriptives
    package to a `Doc` objects. See `DescriptiveStatistics`, `Readability`, and `DependencyDistance`
    for more details.

    USAGE:
        >>> import spacy
        >>> from textdescriptives import TextDescriptives
        >>> nlp = spacy.load("en_core_web_sm")
        >>> nlp.add_pipe("textdescriptives")
        >>> doc = nlp("This is a the first sentence. Here's a second, slightly longer one.")
        >>> doc._.dependency_distance
        >>> doc._.readability
        >>> doc[0:4]._.token_length
    """

    def __init__(self, nlp: Language):
        """Don't do anything, just return the Doc"""

    def __call__(self, doc: Doc):
        """Run the pipeline component"""
        return doc
