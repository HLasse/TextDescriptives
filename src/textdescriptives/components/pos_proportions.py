""" Calculation of statistics that require a pos-tagger in the pipeline."""

from typing import Callable, Counter, List, Union

import numpy as np
from spacy.language import Language
from spacy.tokens import Doc, Span

from textdescriptives.components.utils import all_upos_tags


class POSProportions:
    """spaCy v.3.0 component that adds attributes for POS statistics to `Doc`
    and `Span` objects."""

    def __init__(self, nlp: Language, use_pos: bool, add_all_tags: bool):
        """Initialise components.

        Args:
            use_pos: If True, uses the simple POS tag. If False, uses the detailed
                universal POS tag.
            add_all_tags: If True, returns proportions of all possible POS tags.
                If False, only returns proportions for the POS tags present in the
                text.
        """
        self.use_pos: bool = use_pos
        self.add_all_tags: bool = add_all_tags
        self.model_tags: List[str] = (
            all_upos_tags if use_pos else nlp.meta["labels"]["tagger"]
        )

        if not Doc.has_extension("pos_proportions"):
            Doc.set_extension("pos_proportions", getter=self.pos_proportions)

        if not Span.has_extension("pos_proportions"):
            Span.set_extension("pos_proportions", getter=self.pos_proportions)

    def pos_proportions(self, text: Union[Doc, Span]) -> dict:
        """Calculates the proportion of tokens in a `Doc`|`Span` that are tagged
        with each POS tag.

        Returns:
            Dict containing {pos_prop_POSTAG: proportion of all tokens tagged with
                POSTAG.
        """
        pos_counts: Counter = Counter()
        if self.add_all_tags:
            # add all tags to the counter so they are included in the output
            pos_counts.update(self.model_tags)
            # reset all counts to 0
            pos_counts.subtract(self.model_tags)

        if self.use_pos:
            pos_counts.update([token.pos_ for token in text])
        else:
            pos_counts.update([token.tag_ for token in text])

        if self.add_all_tags:
            # filter out tags that are not in self.model_tags
            pos_counts = {  # type: ignore
                tag: count
                for tag, count in pos_counts.items()
                if tag in self.model_tags
            }

        len_text = len(text)
        return {
            f"pos_prop_{tag}": count / len(text) if len_text > 0 else np.nan
            for tag, count in pos_counts.items()
        }

    def __call__(self, doc):
        """Run the pipeline component."""
        return doc


@Language.factory(
    "textdescriptives/pos_proportions",
    assigns=["doc._.pos_proportions", "span._.pos_proportions"],
    default_config={"use_pos": True, "add_all_tags": True},
)
def create_pos_proportions_component(
    nlp: Language,
    name: str,
    use_pos: bool,
    add_all_tags: bool,
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
    return POSProportions(nlp, use_pos=use_pos, add_all_tags=add_all_tags)
