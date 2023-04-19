import numpy as np
import pytest
import spacy

import textdescriptives as td  # noqa: F401
import warnings


@pytest.fixture(scope="function")
def nlp():
    nlp = spacy.load("en_core_web_sm")
    nlp.add_pipe("textdescriptives/coherence")
    return nlp


def test_coherence_integration(nlp):
    assert "textdescriptives/coherence" == nlp.pipe_names[-1]


def test_coherence(nlp):
    doc = nlp(
        "This is a short and simple sentence. Here is yet another one. We need quite "
        + "a few before these coherences metrics make sense. Rambling, on and on.",
    )

    assert doc._.coherence
    assert doc._.first_order_coherence_values
    assert doc._.second_order_coherence_values


def test_coherence_single_sentence(nlp):
    doc = nlp("This is a short and simple sentence.")

    assert np.isnan(doc._.first_order_coherence_values).all()
    assert np.isnan(doc._.second_order_coherence_values).all()


def test_coherence_difference(nlp):
    coherent_doc = nlp(
        "We will now talk about animals. Dogs are animals. Cats are animals. Birds are"
        + " animals. Fish are animals.",
    )
    incoherent_doc = nlp(
        "Let's talk about a bunch of things. Houses made of pancakes and dogs talking"
        + " like humans. Look, the snow is falling.",
    )
    assert (
        coherent_doc._.coherence["first_order_coherence"]
        > incoherent_doc._.coherence["first_order_coherence"]
    )
    assert (
        coherent_doc._.coherence["second_order_coherence"]
        > incoherent_doc._.coherence["second_order_coherence"]
    )


def test_coherence_multi_process(nlp):
    docs = nlp.pipe(
        [
            "This is a short and simple sentence. Here is yet another one. We need "
            + "quite a few before these coherences metrics make sense. Rambling, on "
            + "and on.",
            "And another one. That's it. No more.",
        ],
        n_process=2,
    )
    for doc in docs:
        assert doc._.coherence


def test_coherence_blank_pipe():
    nlp = spacy.blank("en")
    nlp.add_pipe("textdescriptives/coherence")

    text = "This is a short and simple sentence. Here is yet another one."
    # check that an exception is raised
    with pytest.raises(ValueError) as e:
        doc = nlp(text)  # noqa F841
    assert "sentence boundary detector has not been" in str(e.value)

    # add a sentencizer
    nlp.add_pipe("sentencizer", before="textdescriptives/coherence")

    with pytest.raises(ValueError) as e:
        doc = nlp(text)  # noqa F841
    assert "Sentence vectors are not available" in str(e.value)


def test_no_warnings(nlp):
    # check that it does not raise a warning
    with warnings.catch_warnings():
        warnings.simplefilter("error")  # raise error is warning is raised
        doc = nlp("hello there!")  # noqa F841
