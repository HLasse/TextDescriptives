
[![spacy](https://img.shields.io/badge/built%20with-spaCy-09a3d5.svg)](https://spacy.io)
[![github actions pytest](https://github.com/hlasse/textdescriptives/actions/workflows/pytest-cov-comment.yml/badge.svg)](https://github.com/hlasse/textdescriptives/actions)
[![github actions docs](https://github.com/hlasse/textdescriptives/actions/workflows/documentation.yml/badge.svg)](https://hlasse.github.io/TextDescriptives/)
![github coverage](https://img.shields.io/endpoint?url=https://gist.githubusercontent.com/hlasse/24ee79064ca9d49616cbc410da65cee2/raw/badge-textdescriptives-pytest-coverage.json)
<!-- Needs to add gist -->




# TextDescriptives

A Python library for calculating a large variety of statistics from text(s) using spaCy v.3 pipeline components and extensions. TextDescriptives can be used to calculate several descriptive statistics, readability metrics, and metrics related to dependency distance. 

# 🔧 Installation
`pip install textdescriptives`

# 📰 News

* TextDescriptives has been completely re-implemented using spaCy v.3.0. The stanza implementation can be found in the `stanza_version` branch and will no longer be maintained. 
* Check out the brand new documentation [here](https://hlasse.github.io/TextDescriptives/)!


# 👩‍💻 Usage
 
Import the library and add the component to your pipeline using the string name of the "textdescriptives" component factory:

```py
import spacy
import textdescriptives as td
nlp = spacy.load("en_core_web_sm")
nlp.add_pipe("textdescriptives") 
doc = nlp("The world is changed. I feel it in the water. I feel it in the earth. I smell it in the air. Much that once was is lost, for none now live who remember it.")

# access some of the values
doc._.readability
doc._.token_length
```

TextDescriptives includes a convenience function for extracting metrics to a Pandas DataFrame

```py
td.extract_df(doc)
```
|    | text                                                                                                                                                        |   token_length_mean |   token_length_median |   token_length_std |   sentence_length_mean |   sentence_length_median |   sentence_length_std |   syllables_per_token_mean |   syllables_per_token_median |   syllables_per_token_std |   n_tokens |   n_unique_tokens |   proportion_unique_tokens |   n_characters |   n_sentences |   flesch_reading_ease |   flesch_kincaid_grade |    smog |   gunning_fog |   automated_readability_index |   coleman_liau_index |     lix |   rix |   dependency_distance_mean |   dependency_distance_std |   prop_adjacent_dependency_relation_mean |   prop_adjacent_dependency_relation_std |
|---:|:------------------------------------------------------------------------------------------------------------------------------------------------------------|--------------------:|----------------------:|-------------------:|-----------------------:|-------------------------:|----------------------:|---------------------------:|-----------------------------:|--------------------------:|-----------:|------------------:|---------------------------:|---------------:|--------------:|----------------------:|-----------------------:|--------:|--------------:|------------------------------:|---------------------:|--------:|------:|---------------------------:|--------------------------:|-----------------------------------------:|----------------------------------------:|
|  0 | The world (...) |             3.28571 |                     3 |            1.54127 |                      7 |                        6 |               3.09839 |                    1.08571 |                            1 |                  0.368117 |         35 |                23 |                   0.657143 |            121 |             5 |               107.879 |             -0.0485714 | 5.68392 |       3.94286 |                      -2.45429 |            -0.708571 | 12.7143 |   0.4 |                    1.69524 |                  0.422282 |                                  0.44381 |                               0.0863679 |

Set which group(s) of metrics you want to extract using the `metrics` parameter (one or more of `readability`, `dependency_distance`, `descriptive_stats`, defaults to `all`)

If `extract_df` is called on an object created using `nlp.pipe` it will format the output with 1 row for each document and a column for each metric.
```py
docs = nlp.pipe(['The world is changed. I feel it in the water. I feel it in the earth. I smell it in the air. Much that once was is lost, for none now live who remember it.',
            'He felt that his whole life was some kind of dream and he sometimes wondered whose it was and whether they were enjoying it.'])

td.extract_df(docs, metrics="dependency_distance")
```
|    | text                                                                                                                                                        |   dependency_distance_mean |   dependency_distance_std |   prop_adjacent_dependency_relation_mean |   prop_adjacent_dependency_relation_std |
|---:|:------------------------------------------------------------------------------------------------------------------------------------------------------------|---------------------------:|--------------------------:|-----------------------------------------:|----------------------------------------:|
|  0 | The world (...) |                    1.69524 |                  0.422282 |                                  0.44381 |                               0.0863679 |
|  1 | He felt (...)  |                    2.56    |                  0        |                                  0.44    |                               0         |

The `text` column can by exluded by setting `include_text` to `False`.

### Using specific components
The specific components (`descriptive_stats`, `readability`, and `dependency_distance`) can be loaded individually. This can be helpful if you're only interested in e.g. readability metrics or descriptive statistics and don't want to run the dependency parser. 

```py
nlp = spacy.blank("da")
nlp.add_pipe("descriptive_stats")
docs = nlp.pipe(['Da jeg var atten, tog jeg patent på ild. Det skulle senere vise sig at blive en meget indbringende forretning',
            "Spis skovsneglen, Mulle. Du vil jo gerne være med i hulen, ikk'?"])

# extract_df is clever enough to only extract metrics that are in the Doc
td.extract_df(docs, include_text = False)
```

|    |   token_length_mean |   token_length_median |   token_length_std |   sentence_length_mean |   sentence_length_median |   sentence_length_std |   syllables_per_token_mean |   syllables_per_token_median |   syllables_per_token_std |   n_tokens |   n_unique_tokens |   proportion_unique_tokens |   n_characters |   n_sentences |
|---:|--------------------:|----------------------:|-------------------:|-----------------------:|-------------------------:|----------------------:|---------------------------:|-----------------------------:|--------------------------:|-----------:|------------------:|---------------------------:|---------------:|--------------:|
|  0 |                 4.4 |                   3   |            2.59615 |                     10 |                       10 |                     1 |                    1.65    |                            1 |                  0.852936 |         20 |                19 |                       0.95 |             90 |             2 |
|  1 |                 4   |                   3.5 |            2.44949 |                      6 |                        6 |                     3 |                    1.58333 |                            1 |                  0.862007 |         12 |                12 |                       1    |             53 |             2 |

## Available attributes
The table below shows the metrics included in TextDescriptives and their attribues on spaCy's `Doc`, `Span`, and `Token` objects. For more information, see the docs.

| Attribute            | Component                       | Description                                                   |
| -------------------- | -------------------------- | ------------------------------------------------------------- |
| `Doc._.token_length`   | `descriptive_stats`                       | Dict containing mean, median, and std of token length.                                |
| `Doc._.sentence_length` | `descriptive_stats`                        | Dict containing mean, median, and std of sentence length.   |
| `Doc._.syllables`    | `descriptive_stats`                       | Dict containing mean, median, and std of number of syllables per token.  |
| `Doc._.counts`        | `descriptive_stats` | Dict containing the number of tokens, number of unique tokens, proportion unique tokens, and number of characters in the Doc.|
| `Doc._.readability`        | `readability` | Dict containing Flesch Reading Ease, Flesch-Kincaid Grade, SMOG, Gunning-Fog, Automated Readability Index, Coleman-Liau Index, LIX, and RIX readability metrics for the Doc. |
| `Doc._.dependency_distance`        | `dependency_distance` | Dict containing the mean and standard deviation of the dependency distance and proportion adjacent dependency relations in the Doc.|
`Span._.token_length`   | `descriptive_stats`                       | Dict containing mean, median, and std of token length in the span.                                |
| `Span._.counts`        | `descriptive_stats` | Dict containing the number of tokens, number of unique tokens, proportion unique tokens, and number of characters in the span. |
| `Span._.dependency_distance`        | `dependency_distance` | Dict containing the mean dependency distance and proportion adjacent dependency relations in the Doc.|
| `Token._.dependency_distance`        | `dependency_distance` | Dict containing the dependency distance and whether the head word is adjacent for a Token.|



  ## Authors

  Developed by Lasse Hansen ([@HLasse](https://lassehansen.me)) at the [Center for Humanities Computing Aarhus](https://chcaa.io)


  Collaborators:

  *  Ludvig Renbo Olsen ([@ludvigolsen]( https://github.com/ludvigolsen ), [ludvigolsen.dk]( http://ludvigolsen.dk ))
  * Kenneth Enevoldsen ([@KennethEnevoldsen](https://github.com/kennethenevoldsen))
