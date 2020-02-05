import string
import re
from pyphen import Pyphen
 
from nltk import tokenize # evt ændr tokenizer
import numpy as np

class Calculators():
    #__lang == "set a value"
    def __init__(self, lang = 'da'):
        self.__lang = lang

    def remove_punct(self, text):
        return text.translate(str.maketrans('', '', string.punctuation))

    def newline_to_period(self, text):
        text = re.sub(r"\n", '.', text)
        text = re.sub(r"\.\.+", '. ', text)
        return text

    ## Word length -----------------
    def avg_word_length(self, text):
        text = self.remove_punct(text)
        tokens = text.split(' ')
        token_length = [len(token) for token in tokens]
        avg = sum(token_length) / len(token_length)
        return avg

    def median_word_length(self, text):
        text = self.remove_punct(text)
        tokens = text.split(' ')
        token_length = [len(token) for token in tokens]
        return np.median(token_length)
        
    def std_word_length(self, text):
        text = self.remove_punct(text)
        tokens = text.split(' ')
        token_length = [len(token) for token in tokens]
        return np.std(token_length)

    ## Sentence length ------------
    def avg_sentence_length(self, text):
        sentences = tokenize.sent_tokenize(text)
        tokens = self.remove_punct(text).split(' ')
        try:
            return len(tokens) / len(sentences)
        except ZeroDivisionError:
            return 0
        return len(tokens) / len(sentences)

    def median_sentence_length(self, text):
        sentences = tokenize.sent_tokenize(text)
        tokenized_sentences = [self.remove_punct(sentence).split(' ') for sentence in sentences]
        lengths = [len(sentence) for sentence in tokenized_sentences]
        return np.median(lengths)

    def std_sentence_length(self, text):
        sentences = tokenize.sent_tokenize(text)
        tokenized_sentences = [self.remove_punct(sentence).split(' ') for sentence in sentences]
        lengths = [len(sentence) for sentence in tokenized_sentences]
        return np.std(lengths)

    ## Syllables ------------
    def syllable_count(self, text):
        """
        Calculates total number of syllables in a string
        """
        text = self.remove_punct(text.lower())
        if not text:
            return 0
        
        count = 0
        dic = Pyphen(lang = self.__lang)
        for token in text.split(' '):
            word_hyphenated = dic.inserted(token)
            count += max(1, word_hyphenated.count("-") + 1)
        return count
    
    def avg_syl_per_word(self, text):
        syllables = self.syllable_count(text)
        n_tokens = self.n_tokens(text)
        try:
            return float(syllables) / float(n_tokens)
        except ZeroDivisionError:
            return 0.0
    
    def median_syl_per_word(self, text):
        syllables = [self.syllable_count(token) for token in text.split(' ')]
        return np.median(syllables)

    def std_syl_per_word(self, text):
        syllables = [self.syllable_count(token) for token in text.split(' ')]
        return np.std(syllables)

    ## Misc
    def type_token_ratio(self, text):
        text = self.remove_punct(text)
        tokens = text.lower().split(' ')
        types = set(tokens)
        ratio = len(types) / len(tokens)
        return ratio

    def lix(self, text):
        words = self.remove_punct(text).split()

        words_len = len(words)
        long_words = len([wrd for wrd in words if len(wrd) > 6])
        try:
            per_long_words = (float(long_words) * 100) / words_len
        except ZeroDivisionError:
            return 0
        asl = self.avg_sentence_length(text)
        lix = asl + per_long_words
        return lix

    def rix(self, text):
        """
        n_long words / n sentences
        """
        tokens = self.remove_punct(text).split(' ')
        n_long_words = len([token for token in tokens if len(token) > 6])

        n_sentences = self.n_sentences(text)

        try:
            rix = n_long_words / n_sentences
        except ZeroDivisionError:
            rix = 0.0
        return rix

    def n_types(self, text):
        text = self.remove_punct(text)
        return len(set(text.split(' ')))

    def n_tokens(self, text):
        text = self.remove_punct(text)
        return len(text.split(' '))

    def n_sentences(self, text):
        sentences = tokenize.sent_tokenize(text)
        return len(sentences)
    
    def n_chars(self, text, ignore_whitespace = True):
        if ignore_whitespace:
            text = text.replace(" ", "")
        return len(text)
        
