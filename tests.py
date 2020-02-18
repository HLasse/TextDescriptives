"""
How to use
TODO tests
"""
import pandas as pd

import textdescriptives

# Input can be either a string, list of strings, or pandas Series 
en_test = ['The world is changed. I feel it in the water. I feel it in the earth. I smell it in the air. Much that once was is lost, for none now live who remember it.',
            'He felt that his whole life was some kind of dream and he sometimes wondered whose it was and whether they were enjoying it.']

# If you want to calculate all measures at once
textdescriptives.all_metrics(en_test, lang = 'en', snlp_path = snlp_path)

# Otherwise, the following calculates one category at a time
textdescriptives.basic_stats(en_test, lang = 'en')
textdescriptives.readability(en_test, lang = 'en')
textdescriptives.etymology(en_test, lang = 'en')
# Dependency distance uses stanfordnlp, and thus requires snlp language resources
# If you already have them downloaded, you can specify the folder path
# Otherwise, they will be downloaded
snlp_path = '/path/to/stanfordnlp_resources'    
textdescriptives.dependency_distance(en_test, lang = 'en', snlp_path = snlp_path)

# Textdescriptives works for most languages. Simply change the country code     
da_test = pd.Series(['Da jeg var atten, tog jeg patent på ild. Det skulle senere vise sig at blive en meget indbringende forretning',
            "Spis skovsneglen, Mulle. Du vil jo gerne være med i hulen, ikk'?"])

textdescriptives.all_metrics(da_test, 'da', snlp_path=snlp_path)


# If you want to calculate a subset of the basic statistics they can be specified in the measures paratmer
textdescriptives.basic_stats(en_test, lang = 'en', metrics=['avg_word_length', 'avg_sentence_length'])