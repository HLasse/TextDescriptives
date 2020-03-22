# 3) Fry readability graph
# 5) The FORCAST formula
# 6) Readability and newspaper readership

import pandas as pd

from .calculator import Calculator
from .text import Text

class Readability(Calculator):

    def calculate_metrics(self, texts, metrics = "all"):
        # Convert to Text objects
        texts = [Text(text) for text in texts]

        metric_funcs = {
            'gunning_fog' : self.gunning_fog, 
            'smog' : self.smog,
            'flesch_selfing_ease' : self.flesch_reading_ease, 
            'flesch_kincaid_grade' : self.flesch_kincaid_grade,
            'automated_selfability_index' : self.automated_readability_index, 
            'coleman_liau_index' : self.coleman_liau_index,
            'lix' : self.lix,
            'rix' : self.rix
        }        

        if isinstance(metrics, str):
            if metrics == "all":
                metrics = metric_funcs.keys()
            else:
                raise ValueError("'metrics' can be either 'all' or a list of metric names.")
        elif isinstance(metrics, list):
            if not isinstance(metrics[0], str):
                raise ValueError("'metrics' can be either 'all' or a list of metric names.")
            if not set(metrics).issubset(set(metric_funcs.keys())):
                raise ValueError(f"'metrics' contained unknown metric name.")

        calculated_metrics = [
            pd.Series([metric_funcs[met](txt) for txt in texts]) \
                for met in metrics
        ]
        calculated_metrics = pd.concat(calculated_metrics, axis = 1)
        calculated_metrics.columns = metrics
        return calculated_metrics

    def hard_words(self, text, n_syls = 3):
        """
        Calculates the number of hard words (more than 3 syllables) in a text
        """
        text = Text.to_text(text)
        syllables = self.syllable_counts(text) # TODO Breaking: This removes punctuation before tokenization? Should it?
        hard_words = [syllable for syllable in syllables if syllable >= n_syls]
        return len(hard_words)

    def gunning_fog(self, text):
        """
        Grade level = 0.4 * ((avg_sentence_length) + (percentage hard words))
        hard words = 3+ syllables
        """
        text = Text.to_text(text)
        avg_sent_len = self.avg_sentence_length(text)
        percent_hard_words = (self.hard_words(text) / self.n_tokens(text)) * 100
        return 0.4 * (avg_sent_len + percent_hard_words)

    def smog(self, text):
        """
        grade level = 1.043( sqrt(30 * (hard words /n sentences)) + 3.1291
        Preferably need 30+ sentences. Will not work with less than 4
        """
        text = Text.to_text(text)
        if text.num_sentences >= 3:
            hard_words = self.hard_words(text)
            smog = (1.043 * (30 * (hard_words / text.num_sentences)) ** 0.5) + 3.1291
            return smog
        else:
            return 0.0
    
    def flesch_reading_ease(self, text):
        """
        206.835 - (1.015 X avg sent len) - (84.6 * avg_syl_per_word)

        Higher = easier to read
        Works best for English
        """
        text = Text.to_text(text)
        score = 206.835 - (1.015 * self.avg_sentence_length(text)) - (84.6 * self.avg_syl_per_word(text))
        return score

    def flesch_kincaid_grade(self, text):
        """
        Score = grade required to read the text
        """
        text = Text.to_text(text)
        score = 0.39 * self.avg_sentence_length(text) + 11.8 * self.avg_syl_per_word(text) - 15.59
        return score
    
    def automated_readability_index(self, text):
        """
        Score = grade required to read the text
        """
        text = Text.to_text(text)
        score = 4.71 * self.avg_word_length(text) + 0.5 * self.avg_sentence_length(text) - 21.43
        return score
    
    def coleman_liau_index(self, text):
        """
        score = 0.0588 * avg number of chars pr 100 words - 0.296 * avg num of sents pr 100 words -15.8
        Score = grade required to read the text
        
        """
        text = Text.to_text(text)
        l = self.avg_word_length(text) * 100
        s = (text.num_sentences / text.num_tokens_without_punctuation) * 100
        return 0.0588 * l - 0.296 * s - 15.8

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


# r = Readability(lang = 'da')