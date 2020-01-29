from calculators import Calculators
from readability import Readability
import pandas as pd


class Textdescriptives():
    def __init__(self, texts, lang = 'da', category = 'all', measures = None):
        """
        texts: str/list/pd.Series containing text
        lang: str with the language code
        category: which categories to calculate. Options are ['all', 'readability', 'basic', ..., None]
        measures: if you only want to calculate specific measures.
        """

        if not isinstance(texts, (str, list, pd.Series)):
            raise ValueError(f"Input should be string, list, or pandas series, not {type(texts)}")

        if isinstance(texts, str):
            texts = [texts]
        self.df = pd.DataFrame(texts, columns = ['Text'])
        self.lang = lang


        valid_categories = ['all', 'basic', 'readability', 'entropy', 'sentiment']

        # lav category check

        if category == 'all':
            self.basic()
            self.readability()


    def basic(self, measures = 'all'):
        """
        Calculates simple descriptive statistics
        """
        basic_calc = Calculators(lang = self.lang)

        valid_measures = {'avg_word_length' : basic_calc.avg_word_length, 'median_word_length' : basic_calc.median_word_length,
                          'std_word_length' : basic_calc.std_word_length, 'avg_sentence_length' : basic_calc.avg_sentence_length, 
                          'median_sentence_length' : basic_calc.median_sentence_length, 'std_sentence_length' : basic_calc.std_sentence_length,
                          'avg_syl_per_word' : basic_calc.avg_syl_per_word, 'median_syl_per_word' : basic_calc.median_syl_per_word, 
                          'std_syl_per_word' : basic_calc.std_syl_per_word, 'type_token_ratio' : basic_calc.type_token_ratio, 
                          'lix' : basic_calc.lix, 'rix' : basic_calc.rix, 'n_types' : basic_calc.n_types,
                          'n_sentences' : basic_calc.n_sentences, 'n_tokens' : basic_calc.n_tokens, 'n_chars' : basic_calc.n_chars
                          }
        
        if measures == 'all':
            for measure, func in valid_measures.items():
                self.df[measure] = [func(text) for text in self.df['Text']]

        elif not (set(measures).issubset(set(valid_measures.keys()))):
            raise ValueError("Invalid measures provided to self.basic")
    
        else:
            for measure in measures:
                self.df[measure] = [valid_measures[measure](text) for text in self.df['Text']]          

    def readability(self, measures = 'all'):
        """
        Calculates readability scores
        """
        read = Readability(lang = self.lang)

        valid_measures = {'gunning_fog' : read.gunning_fog, 'smog' : read.smog,
                          'flesch_reading_ease' : read.flesch_reading_ease, 'flesch_kincaid_grade' : read.flesch_kincaid_grade,
                          'automated_readability_index' : read.automated_readability_index, 'coleman_liau_index' : read.coleman_liau_index,
                          }

        if measures == 'all':
            for measure, func in valid_measures.items():
                self.df[measure] = [func(text) for text in self.df['Text']]

        elif not (set(measures).issubset(set(valid_measures.keys()))):
            raise ValueError("Invalid measures provided to self.readability")
    
        else:
            for measure in measures:
                self.df[measure] = [valid_measures[measure](text) for text in self.df['Text']]

    def entropy(self):
        pass

    def sentiment(self):
        pass



test = 'Det her er en alng stesteskl. sdælfksdælfksdæ df  ksdf læskeæ  kæeo   weorwp. erowopor  erwa  jkre krlwe as  klæerwk æ lekrl er. erw rew erere erw asdf. sdfsfsd fdsf rte fgdf.'

t = Textdescriptives(test, 'da')
t.basic('all')
t.basic(['avg_word_length', 'median_word_length', 'fisse'])
t.readability(['gunning_fog'])
t.df
sents = 'teste sdf. sd sd sd. d'
sentences = tokenize.sent_tokenize(sents)


t.texts
isinstance(test.tolist(), list)