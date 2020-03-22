
import string
import re
from nltk import tokenize # evt ændr tokenizer

class Text():
    def __init__(self, text):
        assert isinstance(text, str), "'text' must have type str."
        self.text = text
        self.text_without_punctuation = Text.remove_punct(self.text)
        self.tokens = self.text.split()
        self.tokens_without_punctuation = self.text_without_punctuation.split()
        self.sentences = tokenize.sent_tokenize(text)
        self.num_tokens = len(self.tokens)
        self.num_tokens_without_punctuation = len(self.tokens_without_punctuation)
        self.num_sentences = len(self.sentences)

    @staticmethod
    def remove_punct(text):
        return text.translate(str.maketrans('', '', string.punctuation))

    def __newline_to_period(self, text):
        text = re.sub(r"\n", '.', text)
        text = re.sub(r"\.\.+", '. ', text)
        return text

    @staticmethod
    def to_text(text):
        """
        If not of type Text, convert to Text object and return
        Otherwise, return as is.
        """
        if not isinstance(text, Text):
            if not isinstance(text, str):
                raise TypeError(f"'text' must have type str, not {type(text)}")
            text = Text(text)
        return text
