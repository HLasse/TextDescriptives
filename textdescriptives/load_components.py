"""Adds components to a spaCy pipeline"""
from components import (
    create_readability_component,
    create_dependency_distance_component,
    create_descriptive_stats_component,
)

from spacy.language import Language
from spacy.tokens import Doc


@Language.component("textdescriptives")
def textdescriptives_component(nlp: Language, name: str):
    """Add all components to a spaCy pipeline"""
    for component in [
        "descriptive_stats",
        "readability",
        "dependency_distance",
    ]:
        nlp.add_pipe(component, last=True)
    return TextDescriptives(nlp)


class TextDescriptives:
    def __init__(self, nlp: Language):
        """Don't do anything except initialise the other components"""

    def __call__(self, doc: Doc):
        """Run the pipeline component"""
        return doc


# def add_components(nlp: Language):
#     """Add all components to a spaCy pipeline"""
#     for component in [
#         "utilities",
#         "descriptive_stats",
#         "readability",
#         "dependency_distance",
#     ]:
#         nlp.add_pipe(component, last=True)
#     return nlp


import spacy

nlp = spacy.load("da_core_news_sm")
nlp = nlp.add_pipe("textdescriptives")
nlp.add_pipe("descriptive_stats")
doc = nlp("Det her er en fin lille sætning. Ja, den er bare rigtig sød.")
print(doc._.counts)
print(doc[0:4]._.token_length)
print(doc._.readability)
print(doc._.dependency_distance)
