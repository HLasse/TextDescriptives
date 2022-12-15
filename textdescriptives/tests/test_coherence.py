import numpy as np
import pytest
import spacy

from textdescriptives.components import Coherence


@pytest.fixture(scope="function")
def nlp_small():
    nlp = spacy.load("en_core_web_sm")
    nlp.add_pipe("textdescriptives.coherence")
    return nlp


@pytest.fixture(scope="function")
def nlp_large():
    nlp = spacy.load("en_core_web_lg")
    nlp.add_pipe("textdescriptives.coherence")
    return nlp


def test_coherence_integration(nlp_small):
    assert "textdescriptives.coherence" == nlp_small.pipe_names[-1]


def test_coherence_small_model(nlp_small):
    doc = nlp_small(
        "This is a short and simple sentence. Here is yet another one. We need quite a few before these coherences metrics make sense. Rambling, on and on."
    )

    assert doc._.coherence
    assert doc._.first_order_coherence_values
    assert doc._.second_order_coherence_values


def test_coherence_large_model(nlp_large):
    doc = nlp_large(
        "This is a short and simple sentence. Here is yet another one. We need quite a few before these coherences metrics make sense. Rambling, on and on."
    )

    assert doc._.coherence
    assert doc._.first_order_coherence_values
    assert doc._.second_order_coherence_values


def test_coherence_small_model_single_sentence(nlp_small):
    doc = nlp_small("This is a short and simple sentence.")

    assert np.isnan(doc._.first_order_coherence_values).all()
    assert np.isnan(doc._.second_order_coherence_values).all()


def test_coherence_large_model_single_sentence(nlp_large):
    doc = nlp_large("This is a short and simple sentence.")

    assert np.isnan(doc._.first_order_coherence_values).all()
    assert np.isnan(doc._.second_order_coherence_values).all()


def test_coherence_difference(nlp_large):
    coherent_doc = nlp_large(
        "We will now talk about animals. Dogs are animals. Cats are animals. Birds are animals. Fish are animals."
    )
    incoherent_doc = nlp_large(
        "Let's talk about a bunch of things. Houses made of pancakes and dogs talking like humans. Look, the snow is falling."
    )
    assert (
        coherent_doc._.coherence["first_order_coherence"]
        > incoherent_doc._.coherence["first_order_coherence"]
    )
    assert (
        coherent_doc._.coherence["second_order_coherence"]
        > incoherent_doc._.coherence["second_order_coherence"]
    )


def test_coherence_multi_process(nlp_small):
    docs = nlp_small.pipe(
        [
            "This is a short and simple sentence. Here is yet another one. We need quite a few before these coherences metrics make sense. Rambling, on and on.",
            "And another one. That's it. No more.",
        ],
        n_process=2,
    )
    for doc in docs:
        assert doc._.coherence
