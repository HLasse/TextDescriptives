from utils import create_utils_component
from readability import create_readability_component
from dependency_distance import create_dependency_distance_component
from descriptive_stats import create_descriptive_stats_component

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


"""
import spacy
nlp = spacy.load("da_core_news_sm")
nlp = add_components(nlp)
doc = nlp(
    "Her er der et par testsætninger. Der var sørme en ekstra her, som var en smule længere"
)

docs = nlp.pipe(
    [
        "Her er der et par testsætninger. Der var sørme en ekstra her, som var en smule længere",
        "Og så lige endnu en her",
    ]
)

extract_df(doc)
extract_df(docs)
"""
