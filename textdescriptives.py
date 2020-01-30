from calculators import Calculators
from readability import Readability
import pandas as pd


class Textdescriptives():
    def __init__(self, texts, lang = 'da', category = 'all', measures = 'all'):
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


        valid_categories = ['all', 'basic', 'readability', 'entropy', 'sentiment', 'etymology']

        # lav category check

        if category == 'all':
            self.basic()
            self.readability()
            self.etymology()

        if 'basic' in category:
            self.basic(measures = measures)
        if 'readability' in category:
            self.readability(measures = measures)
        if 'etymology' in category:
            self.etymology()


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
            raise ValueError(f"Invalid measures provided to self.readability {measures}")
    
        else:
            for measure in measures:
                self.df[measure] = [valid_measures[measure](text) for text in self.df['Text']]

    def etymology(self, remove_empty = True):
        """
        Calculates emymological origins of the text using the macroetym package
        Further calculates ratio of words with Germanic to Latinate origins
        """
        from macroetym.etym import etym
        from iso639 import languages

        # Macroetym uses 3 letter language codes, have to map them to iso-639
        lan = languages.get(part1 = self.lang).part3

        etym_df = etym(self.df['Text'], lang = lan).T
        etym_df = etym_df.reset_index().rename({'index' : 'Text'}, axis = 1)
        
        self.etym_df = etym_df

        self.df = pd.merge(self.df, etym_df, on ='Text')
        try:
            self.df['Latinate/Germanic'] = self.df['Latinate'] / self.df['Germanic']
        except KeyError:
            self.df['Latinate/Germanic'] = 'No Latinate'
    
    def entropy(self):
        pass

    def sentiment(self):
        pass

    def get_df(self):
        return self.df


test = ['Det her er en lang dansk test. Gad vide om den virker efter hensigten',
        'Også lige en til her, ja tak ja tak. Vi tester bare lige om funktionen virker efter hensigten',
        "Meget formelt sprogbrug, information processering computer, hvorfor finder den ikke nogen ord"]

test = "Meget formelt sprogbrug, information processering computer, hvorfor finder den ikke nogen ord" 

test = ['Not so much in this text, it is also short',
'This is a test in English where I use quite posh words']
t = Textdescriptives(test, 'da', 'basic', ['avg_word_length'])
Textdescriptives(test, 'en', 'etymology').df
t.basic('all')
t.basic(['avg_word_length', 'median_word_length', 'fisse'])
t.readability(['gunning_fog'])
t.df
sents = 'teste sdf. sd sd sd. d'
sentences = tokenize.sent_tokenize(sents)

