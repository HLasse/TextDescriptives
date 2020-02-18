from .calculators import Calculators
from .readability import Readability
from .dependency_distance import Dep_distance
from .macroetym.etym import Etym
import pandas as pd

class Textdescriptives():
    def __init__(self, texts, lang = 'da', category = 'all', measures = 'all', snlp_path = None):
        """
        texts: str/list/pd.Series containing text
        lang: str with the language code
        category: which categories to calculate. Options are ['all', 'basic', 'readability', 'etymology', 'dep_distance']
        measures: if you only want to calculate specific measures (don't use atm)
        """

        if not isinstance(texts, (str, list, pd.Series)):
            raise ValueError(f"Input should be string, list, or pandas series, not {type(texts)}")

        if isinstance(texts, str):
            texts = [texts]
        self.df = pd.DataFrame(texts, columns = ['Text'])
        self.lang = lang
        self.snlp_path = snlp_path


        # Category check
        valid_categories = ['all', 'basic', 'readability', 'entropy', 'sentiment', 'etymology', 'dep_distance']

        if isinstance(category, str):
            if category not in valid_categories:
                print((f"{category} is not a valid category.\nValid categories are: ['all', 'basic', 'readability', 'etymology', 'dep_distance']"))
        else:
            for cat in category:
                if cat not in valid_categories:
                    print(f"{cat} is not a valid category.\nValid categories are: ['all', 'basic', 'readability', 'etymology', 'dep_distance']")
    

        if category == 'all':
            self.basic()
            self.readability()
            self.etymology()
            self.dependency_distance()

        if 'basic' in category:
            self.basic(measures = measures)
        if 'readability' in category:
            self.readability(measures = measures)
        if 'etymology' in category:
            self.etymology()
        if 'dep_distance' in category:
            self.dependency_distance()


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
        from iso639 import languages

        # Macroetym uses 3 letter language codes, have to map them to iso-639
        lan = languages.get(part1 = self.lang).part3

        etym_df = Etym(self.df['Text'], lang = lan).T
        etym_df = etym_df.reset_index().rename({'index' : 'Text'}, axis = 1)
        
        self.etym_df = etym_df

        self.df = pd.merge(self.df, etym_df, on ='Text')
        try:
            self.df['Latinate/Germanic'] = self.df['Latinate'] / self.df['Germanic']
        except KeyError:
            self.df['Latinate/Germanic'] = 'No Latinate'
        
    def dependency_distance(self):
        """
        Calculates mean dependency distance (MDD) of each text, following http://www.lingviko.net/jcs.pdf
        Dependency distance (DD) = abs(governor - dependent)
        As such, adjacent words have a DD of 1. Roots are defined as have a DD of 0
        MDD is calculated on sentence level, ie. MDD is the mean of the average dependency distance pr sentence.
        Mean and standard deviation of the proportion of adjacent dependency relations pr sentence is further calculated
        """
        dep = Dep_distance(self.df['Text'], self.lang, self.snlp_path)

        self.df['mean_dependency_distance'] = dep.mean_dep_dist()
        self.df['std_dependency_distance'] = dep.std_dep_dist()
        self.df['mean_prop_adjacent_dependency_relation'] = dep.proportion_adjacent_dep()
        self.df['std_prop_adjacent_dependency_relation'] = dep.std_proportion_adjacent_dep()
 
    
    def entropy(self):
        pass

    def sentiment(self):
        pass

    def get_df(self):
        return self.df


def all_metrics(texts, lang = 'en', snlp_path = None):
    """
    Calculates all implemented statistical metrics
    text: str/list/pd.Series of strings
    lang: two character language code, e.g. 'en', 'da'
    snlp_path: string, path to stanfordnlp_resources
    """
    return Textdescriptives(texts, lang, 'all', snlp_path = snlp_path).df

def basic_stats(texts, lang = 'en', metrics = 'all'):
    """
    Calculates standard descriptive statistics
    text: str/list/pd.Series of strings
    lang: string, two character language code
    measures: string/list of strings, which measures to calculate
    """
    return Textdescriptives(texts, lang, 'basic', measures = metrics).df

def readability(texts, lang = 'en', measures = 'all'):
    """
    Calculates readability metrics
    texts: str/list/pd.Series of strings
    lang: string, two character language code
    measures: string/list of strings, which measures to calculate
    """
    return Textdescriptives(texts, lang, 'readability', measures = measures).df

def etymology(texts, lang = 'en'):
    """
    Calculates measures related to etymology
    texts: str/list/pd.Series of strings
    lang: string, two character language code
    """
    return Textdescriptives(texts, lang, 'etymology').df

def dependency_distance(texts, lang = 'en', snlp_path = None):
    """
    Calculates measures related to etymology
    texts: str/list/pd.Series of strings
    lang: string, two character language code
    snlp_path: string, path to stanfordnlp_resources
    """
    return Textdescriptives(texts, lang, 'dep_distance', snlp_path = snlp_path).df