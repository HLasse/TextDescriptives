"""Adds components to a spaCy pipeline"""
from .components.utils import create_utils_component
from .components.readability import create_readability_component
from .components.dependency_distance import create_dependency_distance_component
from .components.descriptive_stats import create_descriptive_stats_component

from spacy.language import Language


def add_components(nlp: Language):
    """Add all components to a spaCy pipeline"""
    for component in [
        "utilities",
        "descriptive_stats",
        "readability",
        "dependency_distance",
    ]:
        nlp.add_pipe(component, last=True)
    return nlp
