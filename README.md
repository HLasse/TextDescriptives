# TextDescriptives

A Python package for calculating a large variety of statistics from text(s).

## Installation
Clone the Github directory, navigate to it in a terminal, and call
`pip install .`

 ## Usage
 
To calculate all possible metrics:
```
import textdescriptives

# Input can be either a string, list of strings, or pandas Series 
en_test = ['The world is changed. I feel it in the water. I feel it in the earth. I smell it in the air. Much that once was is lost, for none now live who remember it.',
            'He felt that his whole life was some kind of dream and he sometimes wondered whose it was and whether they were enjoying it.']

textdescriptives.all_metrics(en_test, lang = 'en', snlp_path = snlp_path)
```
|    | Text                                                                                                                                                        |   avg_word_length |   median_word_length |   std_word_length |   avg_sentence_length |   median_sentence_length |   std_sentence_length |   avg_syl_per_word |   median_syl_per_word |   std_syl_per_word |   type_token_ratio |     lix |   rix |   n_types |   n_sentences |   n_tokens |   n_chars |   gunning_fog |    smog |   flesch_reading_ease |   flesch_kincaid_grade |   automated_readability_index |   coleman_liau_index |   Germanic |   Latinate |   Latinate/Germanic |   mean_dependency_distance |   std_dependency_distance |   mean_prop_adjacent_dependency_relation |   std_prop_adjacent_dependency_relation |
|---:|:------------------------------------------------------------------------------------------------------------------------------------------------------------|------------------:|---------------------:|------------------:|----------------------:|-------------------------:|----------------------:|-------------------:|----------------------:|-------------------:|-------------------:|--------:|------:|----------:|--------------:|-----------:|----------:|--------------:|--------:|----------------------:|-----------------------:|------------------------------:|---------------------:|-----------:|-----------:|--------------------:|---------------------------:|--------------------------:|-----------------------------------------:|----------------------------------------:|
|  0 | The world is changed.(...) |           3.28571 |                    3 |           1.54127 |                     7 |                        6 |               3.09839 |            1.08571 |                     1 |           0.368117 |           0.657143 | 12.7143 |   0.4 |        24 |             5 |         35 |       121 |       3.94286 | 5.68392 |               107.879 |             -0.0485714 |                      -2.45429 |            -0.708571 |    75      |    25      |            0.333333 |                    1.60381 |                   0.36493 |                                 0.695238 |                               0.0481871 |
|  1 | He felt that his whole (...)                                |           4.16667 |                    4 |           1.97203 |                    24 |                       24 |               0       |            1.16667 |                     1 |           0.471405 |           0.833333 | 40.6667 |   4   |        21 |             1 |         24 |       101 |      11.2667  | 0       |                83.775 |              7.53667   |                      10.195   |             7.46667  |    83.3333 |    16.6667 |            0.2      |                    2.16    |                   0       |                                 0.64     |                               0         |


To calculate one category at a time:
```
textdescriptives.basic_stats(texts, lang = 'en', metrics = 'all')
textdescriptives.readability(texts, lang = 'en')
textdescriptives.etymology(texts, lang = 'en')
textdescriptives.dependency_distance(texsts, lang = 'en', snlp_path = None)
```
Textdescriptives works for most languages, simply change the country code:
```
da_test = pd.Series(['Da jeg var atten, tog jeg patent på ild. Det skulle senere vise sig at blive en meget indbringende forretning',
            "Spis skovsneglen, Mulle. Du vil jo gerne være med i hulen, ikk'?"])

textdescriptives.all_metrics(da_test, lang = 'da', snlp_path=snlp_path)
```

If you only want a subset of the basic statistics
```
textdescriptives.basic_stats(en_test, lang = 'en', metrics=['avg_word_length', 'n_chars'])
```
|    | Text                                                                                                                                                        |   avg_word_length |   n_chars |
|---:|:------------------------------------------------------------------------------------------------------------------------------------------------------------|------------------:|----------:|
|  0 | The world is changed.(...) |           3.28571 |       121 |
|  1 | He felt that his whole (...) |           4.16667 |       101 |

### Readability

The readability measures are largely derived from the [textstat](https://github.com/shivam5992/textstat) library and are thoroughly defined there.

### Etymology
The etymology measures are calculated using [macroetym](https://github.com/JonathanReeve/macro-etym) only slightly rewritten to be called from a script. They are calculated since in English, a greater frequency of words with a Latinate origin tends to indicate a more formal language register. 

### Dependency Distance
Mean dependency distance can be used as a way of measuring the average syntactic complexity of a text. Requres the `snlp` library. 
The dependency distance function requires stanfordnlp, and their language models. If you have already downloaded these models, the path to the folder can be specified in the snlp_path paramter. Otherwise, the models will be downloaded to your working directory + /snlp_resources.


## Dependencies
Depending on which measures you want to calculate, the dependencies differ.
 * Basic and readability: numpy, pandas, pyphen, pycountry
 * Etymology: nltk and the following models 
`python3 -c "import nltk; nltk.download('punkt'); nltk.download('stopwords'); nltk.download('averaged_perceptron_tagger'); nltk.download('wordnet')"`
 * Depedency distance: snlp


## Metrics
Metrics currently implemented:

1. Basic descriptive statistics - mean, median, standard deviation of the following:
  * Word length
  * Sentence length, words
  * Sentence length, characters (TODO)
  * Syllables per word
  * Number of characters
  * Number of sentences
  * Number of types (unique words)
  * Number of tokens (total words)
  * Type/toḱen ratio
  * Lix
  * Rix

2. Readability metrics:
  * Gunning-Fog
  * SMOG
  * Flesch reading ease
  * Flesch-Kincaid grade
  * Automated readability index
  * Coleman-Liau index
  
 3. Etymology-related metrics:
  * Percentage words with Germanic origin
  * Percentage words with Latinate origin
  * Latinate/Germanic origin ratio
  
 4. Dependency distance metrics:
  * Mean dependency distance, sentence level (mean, standard deviation)
  * Mean proportion adjacent dependency relations, sentence level (mean, standard devaiation)
  
  
  Developed by Lasse Hansen at the [Center for Humanities Computing Aarhus](chcaa.io)
