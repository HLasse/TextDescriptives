import string
import re
from pyphen import Pyphen
 
from nltk import tokenize # evt ændr tokenizer
import numpy as np
import pandas as pd

from .text import Text

class Calculators():
    #__lang == "set a value"
    def __init__(self, lang = 'da'):
        self.__lang = lang
    
    def calculate_metrics(self, texts, metrics = "all"):
        # Convert to Text objects
        texts = [Text(text) for text in texts]

        metric_funcs = {
            'mean_word_length' : self.avg_word_length, 
            'median_word_length' : self.median_word_length,
            'std_word_length' : self.std_word_length, 
            'mean_sentence_length' : self.avg_sentence_length, 
            'median_sentence_length' : self.median_sentence_length, 
            'std_sentence_length' : self.std_sentence_length,
            'mean_syl_per_word' : self.avg_syl_per_word, 
            'median_syl_per_word' : self.median_syl_per_word, 
            'std_syl_per_word' : self.std_syl_per_word, 
            'type_token_ratio' : self.type_token_ratio, 
            'n_chars' : self.n_chars, 
            'n_sentences' : self.n_sentences, 
            'n_types' : self.n_types,  
            'n_tokens' : self.n_tokens
        }        

        if isinstance(metrics, str):
            if metrics == "all":
                metrics = metric_funcs.keys()
            elif metrics == "mean_only":
                metrics = [
                'mean_word_length', 
                'mean_sentence_length',
                'mean_syl_per_word',
                'type_token_ratio',
                'n_chars',
                'n_sentences',
                'n_types',
                'n_tokens']
            else:
                raise ValueError("'metrics' can be either 'all', 'mean_only' or a list of metric names.")
        elif isinstance(metrics, list):
            if not isinstance(metrics[0], str):
                raise ValueError("'metrics' can be either 'all', 'mean_only' or a list of metric names.")
            if not set(metrics).issubset(set(metric_funcs.keys())):
                raise ValueError(f"'metrics' contained unknown metric name.")

        calculated_metrics = [
            pd.Series([metric_funcs[met](txt) for txt in texts]) \
                for met in metrics
        ]
        calculated_metrics = pd.concat(calculated_metrics, axis = 1)
        calculated_metrics.columns = metrics
        return calculated_metrics

    # TODO Not used?
    # def newline_to_period(self, text):
    #     text = re.sub(r"\n", '.', text)
    #     text = re.sub(r"\.\.+", '. ', text)
    #     return text

    ## Word length -----------------

    def __token_lengths(self, text):
        text = Text.to_text(text)
        return [len(token) for token in text.tokens_without_punctuation]
         
    def avg_word_length(self, text):
        token_lengths = self.__token_lengths(text)
        return np.mean(token_lengths)

    def median_word_length(self, text):
        token_lengths = self.__token_lengths(text)
        return np.median(token_lengths)
        
    def std_word_length(self, text):
        token_lengths = self.__token_lengths(text)
        return np.std(token_lengths)

    ## Sentence length ------------
    def avg_sentence_length(self, text):
        text = Text.to_text(text)
        try:
            return float(text.num_tokens_without_punctuation) / float(text.num_sentences)
        except ZeroDivisionError:
            return 0

    def median_sentence_length(self, text):
        text = Text.to_text(text)
        tokenized_sentences = [Text.remove_punct(sentence).split(' ') for sentence in text.sentences]
        sentence_lengths = [len(sentence) for sentence in tokenized_sentences]
        return np.median(sentence_lengths)

    def std_sentence_length(self, text):
        text = Text.to_text(text)
        tokenized_sentences = [Text.remove_punct(sentence).split(' ') for sentence in text.sentences]
        sentence_lengths = [len(sentence) for sentence in tokenized_sentences]
        return np.std(sentence_lengths)

    ## Syllables ------------
    # TODO We're rerunning syllably_counts() every time. 
    # That is only necessary when calling the methods one at a time?

    def syllable_counts(self, text):
        """
        Calculates number of syllables per token
        Punctuation is removed before tokenization
        """
        text = Text.to_text(text)
        if not text.text:
            return 0
        dic = Pyphen(lang = self.__lang)
        def count_syl(token):
            word_hyphenated = dic.inserted(token.lower())
            return max(1, word_hyphenated.count("-") + 1)
        return [count_syl(token) for token in text.tokens_without_punctuation]

    def syllable_count(self, text):
        """
        Calculates total number of syllables in a string
        """
        return sum(self.syllable_counts(text))

    def avg_syl_per_word(self, text):
        return np.mean(self.syllable_counts(text))
    
    def median_syl_per_word(self, text):
        return np.median(self.syllable_counts(text))

    def std_syl_per_word(self, text):
        return np.std(self.syllable_counts(text))

    ## Misc
    def type_token_ratio(self, text):
        text = Text.to_text(text)
        tokens = [token.lower() for token in text.tokens_without_punctuation]
        types = set(tokens)
        ratio = len(types) / len(tokens)
        return ratio

    def lix(self, text):
        text = Text.to_text(text)
        words = text.tokens_without_punctuation
        words_len = text.num_tokens_without_punctuation
        if words_len == 0:
            return 0
        long_words = len([wrd for wrd in words if len(wrd) > 6])
        per_long_words = (float(long_words) * 100) / words_len
        asl = self.avg_sentence_length(text)
        lix = asl + per_long_words
        return lix

    def rix(self, text):
        """
        n_long words / n sentences
        """
        text = Text.to_text(text)
        if text.num_sentences == 0:
            return 0.0
        n_long_words = len([token for token in text.tokens_without_punctuation if len(token) > 6])
        return float(n_long_words) / float(text.num_sentences)

    def n_types(self, text): 
        # TODO Why is this called n_types?
        # TODO Should the tokens be lower case?
        text = Text.to_text(text)
        return len(set(text.tokens_without_punctuation))

    def n_tokens(self, text):
        text = Text.to_text(text)
        return text.num_tokens_without_punctuation

    def n_sentences(self, text):
        text = Text.to_text(text)
        return text.num_sentences
    
    def n_chars(self, text, ignore_whitespace = True):
        text = Text.to_text(text)
        text = text.text
        if ignore_whitespace:
            text = text.replace(" ", "")
        return len(text)
        
