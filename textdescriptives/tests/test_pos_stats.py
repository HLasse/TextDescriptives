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

def test_pos_proportions(nlp):
    doc = nlp(
        "Here is the first sentence. It was pretty short. Let's make another one that's slightly longer and more complex."
    )

    assert doc._.pos_proportions == {'pos_prop_RB': 0.125, 'pos_prop_VBZ': 0.08333333333333333, 'pos_prop_DT': 0.08333333333333333, 'pos_prop_JJ': 0.125, 'pos_prop_NN': 0.08333333333333333, 'pos_prop_.': 0.125, 'pos_prop_PRP': 0.08333333333333333, 'pos_prop_VBD': 0.041666666666666664, 'pos_prop_VB': 0.08333333333333333, 'pos_prop_WDT': 0.041666666666666664, 'pos_prop_JJR': 0.041666666666666664, 'pos_prop_CC': 0.041666666666666664, 'pos_prop_RBR': 0.041666666666666664}