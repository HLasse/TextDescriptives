"""Adds all components to a spaCy pipeline."""
from spacy.language import Language
from spacy.tokens import Doc


class TextDescriptives:
    """Utility spaCy v3.0 component to add all functionality from the
    TextDescriptives package to a `Doc` objects. See `DescriptiveStatistics`,
    `Readability`, and `DependencyDistance` for more details.

    Example:
        >>> import spacy
        >>> from textdescriptives import TextDescriptives
        >>> nlp = spacy.load("en_core_web_sm")
        >>> nlp.add_pipe("textdescriptives")
        >>> text = "This is a the first sentence. Here's a second, slightly longer one."
        >>> doc = nlp(text)
        >>> doc._.dependency_distance
        >>> doc._.readability
        >>> doc[0:4]._.token_length
    """

    def __init__(self, nlp: Language):
        """Don't do anything, just return the Doc."""

    def __call__(self, doc: Doc):
        """Run the pipeline component."""
        return doc


@Language.factory(
    "textdescriptives/all",
    assigns=[
        "doc._.readability",
        "doc._.dependency_distance",
        "doc._.token_length",
        "doc._.sentence_length",
        "doc._.n_sentences",
        "doc._.n_tokens",
        "doc._.descriptive_stats",
        "doc._.pos_proportions",
        "doc._.quality",
        "doc._.syllables",
        "doc._.counts",
        "doc._.coherence",
        "doc._.first_order_coherence_values",
        "doc._.second_order_coherence_values",
        "doc._.passed_quality_check",
        "doc._._n_sentences",
        "doc._._n_tokens",
        "doc._._n_syllables",
    ],  # intentionally not assigning span attributes
)
def create_textdescriptives_component(nlp: Language, name: str):
    components = [
        k
        for k in Language.factories.keys()
        if k.startswith("textdescriptives") and k != "textdescriptives/all"
    ]

    for component in components:
        nlp.add_pipe(component, last=True)
    return TextDescriptives(nlp)
