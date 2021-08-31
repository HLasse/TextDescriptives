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

    assert doc._.pos_proportions == {'RB': 0.125, 'VBZ': 0.08333333333333333, 'DT': 0.08333333333333333, 'JJ': 0.125, 'NN': 0.08333333333333333, '.': 0.125, 'PRP': 0.08333333333333333, 'VBD': 0.041666666666666664, 'VB': 0.08333333333333333, 'WDT': 0.041666666666666664, 'JJR': 0.041666666666666664, 'CC': 0.041666666666666664, 'RBR': 0.041666666666666664}