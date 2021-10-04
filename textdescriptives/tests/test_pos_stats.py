import spacy
from spacy.lang.en import English
import pytest
from textdescriptives.components import POSStatistics

@pytest.fixture(scope="function")
def nlp():
    nlp = spacy.load("en_core_web_sm", disable=('ner', 'textcat'))
    nlp.add_pipe("pos_stats")

    return nlp

def test_pos_integrations(nlp):
    assert "pos_stats" == nlp.pipe_names[-1]

def test_pos_proportions_doc(nlp):
    doc = nlp(
        "Here is the first sentence. It was pretty short. Let's make another one that's slightly longer and more complex."
    )

    assert doc._.pos_proportions == pytest.approx({'pos_prop_ADV': 0.1666, 'pos_prop_AUX': 0.0833, 'pos_prop_DET': 0.125, 'pos_prop_ADJ': 0.1666, 'pos_prop_NOUN': 0.0833, 'pos_prop_PUNCT': 0.125, 'pos_prop_PRON': 0.0833, 'pos_prop_VERB': 0.125, 'pos_prop_CCONJ': 0.0416}, rel=1e-2)

def test_pos_proportions_span(nlp):
    doc = nlp(
        "Here is the first sentence. It was pretty short. Let's make another one that's slightly longer and more complex."
    )

    span = doc[0:]

    assert doc._.pos_proportions == pytest.approx({'pos_prop_ADV': 0.1666, 'pos_prop_AUX': 0.0833, 'pos_prop_DET': 0.125, 'pos_prop_ADJ': 0.1666, 'pos_prop_NOUN': 0.0833, 'pos_prop_PUNCT': 0.125, 'pos_prop_PRON': 0.0833, 'pos_prop_VERB': 0.125, 'pos_prop_CCONJ': 0.0416}, rel=1e-2)
    
