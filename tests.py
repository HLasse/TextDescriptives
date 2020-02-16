"""
Tests/how to use
"""
from textdescriptives import Textdescriptives
import pandas as pd

# Create a test input

# Can be either a string, list of strings, or pandas Series 
en_test = ['Taylor, why did you tackle me there? You utter muppet',
           'The world is changed. I feel it in the water. I feel it in the earth. I smell it in the air. Much that once was is lost, for none now live who remember it.']

# At moment, the package supports these categories:
# ['all', 'basic', 'readability', 'etymology', 'dep_distance']

# If you want to get measures of dependency distance, you will need snlp
# you can set your path to stanford nlp resources, otherwise the function will download it to your
# working directory/stanfordnlp_resources
snlp_path = '/path/to/stanfordnlp_resources'    
snlp_path = '/home/au554730/Desktop/CHCAA/DeepAnon/stanfordnlp_resources'

# Simply instantiate the class with the categories you want to calculate measures for
t = Textdescriptives(en_test, 'en', 'all', snlp_path = snlp_path)
t = Textdescriptives(en_test, 'en', 'basic')
t = Textdescriptives(en_test, 'en', 'etymology')
t = Textdescriptives(en_test, 'en', 'readability')
t = Textdescriptives(en_test, 'en', 'dep_distance', snlp_path=snlp_path)
# .. and so on

# Get dataframe
t.get_df()

# Works for most languages. Simply change the country code     
da_test = pd.Series(['Jeg ville gerne skrive noget dybt, men jeg er tom for ideer',
            'Forestil dig, det her er er utrolig klogt og velformuleret. Det er svært, jeg ved det'])

t = Textdescriptives(da_test, 'da', 'basic')
t = Textdescriptives(da_test, 'da', 'dep_distance', snlp_path=snlp_path)
t.get_df()