"""Calculation of various readability metrics"""
from spacy.tokens import Doc
from spacy.language import Language


@Language.factory("utilities")
def create_readability_component(nlp: Language, name: str):
    return Readability(nlp)


class Readability():
     def __init__(self, nlp: Language):
        """Initialise components
        Only calculate n_sentences, n_words, n_syllabes when needed using getters"""
        if not Doc.has_extension("n_sentences"):
            Doc.set_extension("n_sentences", getter=self.n_sentences)

        if not Doc.has_extension("n_words"):
            Doc.set_extension("n_words", getter=self.n_words)

        if not Doc.has_extension("n_syllables"):
            Doc.set_extension("n_syllables", getter=self.n_syllables)

        if not Doc.has_extension("filtered_tokens"):
            Doc.set_extension("filtered_tokens", default=[])

    def __call__(self, doc):
        """Run the pipeline component"""
        doc._.filtered_tokens = self.filtered_tokens(doc)
        return doc







test_sent = "Det her er en testsætning, gad vide hvordan den bliver håndteret."
nlp = spacy.load("da_core_news_sm")

doc = nlp(test_sent)



