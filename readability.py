# 3) Fry readability graph
# 5) The FORCAST formula
# 6) Readability and newspaper readership

from calculators import Calculators

class Readability(Calculators):


    def hard_words(self, text, n_syls = 3):
        """
        Calculates the number of hard words (more than 3 syllables) in a text
        """
        syllables = [self.syllable_count(token) for token in text.split(' ')]
        hard_words = [syllable for syllable in syllables if syllable >= n_syls]
        return len(hard_words)

    def gunning_fog(self, text):
        """
        Grade level = 0.4 * ((avg_sentence_length) + (percentage hard words))
        hard words = 3+ syllables
        """

        avg_sent_len = self.avg_sentence_length(text)
        tokens = self.n_tokens(text)
        percent_hard_words = (self.hard_words(text) / tokens) * 100

        return 0.4 * (avg_sent_len + percent_hard_words)

    def smog(self, text):
        """
        grade level = 1.043( sqrt(30 * (hard words /n sentences)) + 3.1291
        Preferably need 30+ sentences. Will not work with less than 4
        """
        n_sentences = self.n_sentences(text)
        
        if n_sentences >= 3:
            hard_words = self.hard_words(text)
            smog = (1.043 * (30 * (hard_words / n_sentences)) ** 0.5) + 3.1291

            return smog
        else:
            return 0.0
    
    def flesch_reading_ease(self, text):
        """
        206.835 - (1.015 X avg sent len) - (84.6 * avg_syl_per_word)

        Higher = easier to read
        Works best for English
        """
        score = 206.835 - (1.015 * self.avg_sentence_length(text)) - (84.6 * self.avg_syl_per_word(text))
        return score

    def flesch_kincaid_grade(self, text):
        """
        Score = grade required to read the text
        """
        #avg_sent_len = self.avg_sentence_length(tex)
        score = 0.39 * self.avg_sentence_length(text) + 11.8 * self.avg_syl_per_word(text) - 15.59
        return score
    
    def automated_readability_index(self, text):
        """
        Score = grade required to read the text
        """
        score = 4.71 * self.avg_word_length(text) + 0.5 * self.avg_sentence_length(text) - 21.43
        return score
    
    def coleman_liau_index(self, text):
        """
        score = 0.0588 * avg number of chars pr 100 words - 0.296 * avg num of sents pr 100 words -15.8
        Score = grade required to read the text
        
        """
        l = self.avg_word_length(text) * 100
        s = (self.n_sentences(text) / self.n_tokens(text)) * 100
        return 0.0588 * l - 0.296 * s - 15.8




r = Readability(lang = 'da')