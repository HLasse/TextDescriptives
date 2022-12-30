"""Calculation of statistics that require a pos-tagger in the pipeline."""

from typing import Callable, Counter, Union

from spacy.language import Language
from spacy.tokens import Doc, Span


class POSProportions:
    """spaCy v.3.0 component that adds attributes for POS statistics to `Doc`
    and `Span` objects."""

    def __init__(self, nlp: Language, use_pos: bool):
        """Initialise components.

        Args:
            use_pos: If True, uses the simple POS tag. If False, uses the detailed
                universal POS tag.
        """
        self.use_pos = use_pos

        if not Doc.has_extension("pos_proportions"):
            Doc.set_extension("pos_proportions", getter=self.pos_proportions)

        if not Span.has_extension("pos_proportions"):
            Span.set_extension("pos_proportions", getter=self.pos_proportions)

    def pos_proportions(self, text: Union[Doc, Span]) -> dict:
        """Calculates the proportion of tokens in a `Doc`|`Span` that are
        tagged with each POS tag.

        Returns:
            Dict containing {pos_prop_POSTAG: proportion of all tokens tagged with
                POSTAG. Does not create a key if no tokens in the document fit the
                POSTAG.
        """
        pos_counts: Counter = Counter()
        if self.use_pos:
            pos_counts.update([token.pos_ for token in text])
        else:
            pos_counts.update([token.tag_ for token in text])
        pos_proportions = {
            "pos_prop_" + tag: count / len(text) for tag, count in pos_counts.items()
        }

        return pos_proportions

    def __call__(self, doc):
        """Run the pipeline component."""
        return doc


@Language.factory(
    "textdescriptives/pos_proportions",
    assigns=["doc._.pos_proportions", "span._.pos_proportions"],
    default_config={"use_pos": True},
)
def create_pos_stats_component(
    nlp: Language,
    name: str,
    use_pos: bool,
) -> Callable[[Doc], Doc]:
    """Allows PosPropotions to be added to a spaCy pipe using
    nlp.add_pipe("textdescriptives/pos_proportions")

    Adding this component to a pipeline sets the following attributes:
        - `doc._.pos_proportions`
        - `span._.pos_proportions`

    Args:
        nlp (Language): spaCy language object, does not need to be specified in the
            nlp.add_pipe call.
        name (str): name of the component. Can be optionally specified in the
            nlp.add_pipe call, using the name argument.
        use_pos: If True, uses the simple token.pos attribute. If False, uses the
            detailed token.tag attribute.

    Returns:
        Callable[[Doc], Doc]: The POSProportions component to be added to the pipe.

    Example:
        >>> import spacy
        >>> nlp = spacy.load("en_core_web_sm")
        >>> nlp.add_pipe("textdescriptives/pos_proportions")
        >>> # apply the component to a document
        >>> doc = nlp("This is a test sentence.")
        >>> doc._.pos_proportions
    """

    tagger = {"tagger", "attribute_ruler"}
    if not tagger.intersection(set(nlp.pipe_names)):
        raise ValueError(
            "The pipeline does not contain a component for POS tagging. Please load "
            + "a spaCy model which includes a 'tagger' or an 'attribute ruler' "
            + "component.",
        )
    return POSProportions(nlp, use_pos=use_pos)
