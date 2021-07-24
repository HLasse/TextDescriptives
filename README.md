<!-- 
[![PyPI version](https://badge.fury.io/py/tomsup.svg)](https://pypi.org/project/tomsup/)
[![Code style: flake8](https://img.shields.io/badge/Code%20Style-flake8-blue)](https://pypi.org/project/flake8/)
[![pip downloads](https://img.shields.io/pypi/dm/textdescriptives.svg)](https://crate.io/packages/textdescriptives)
[![python versions](https://img.shields.io/pypi/pyversions/textdescriptives?colorB=blue)](https://pypi.org/project/textdescriptives/)
-->




# TextDescriptives

A Python package for calculating a large variety of statistics from text(s).

## Installation
`python -m pip install git+https://github.com/HLasse/TextDescriptives.git`

## News

* TextDescriptives has been completely re-implemented using `spaCy`. The old `stanza` implementation can be found in the `stanza_version` branch but will no longer be maintained. 
* Now uses `stanza` for dependency parsing. `stanfordnlp` is no longer a dependency.

## Usage
 
TextDescriptives adds components to your spaCy pipelines to calculate descriptive statistics, readability metrics, and metrics related to dependency distance. The components are implemented using getters, which means they will only be calculated if you try to access them. 

```py
import spacy
import textdescriptives as td

nlp = spacy.load("en_core_news_sm")
nlp = td.add_components(nlp) # adds the components to the pipeline
doc = nlp("The world is changed. I feel it in the water. I feel it in the earth. I smell it in the air. Much that once was is lost, for none now live who remember it.")

# access some of the values
doc._.readability
doc._.token_length
```

TODO: add output

TextDescriptives includes a convenience function for converting metrics to a Pandas DataFrame

```py
td.extract_df(doc)
```

TODO: add output

Set which group(s) of metrics you want to extract using the `metrics` parameter (one or more of `readability`, `dependency_distance`, `descriptive_stats`, defaults to `all`)
```py
td.extract_df(doc, metrics="readability")
```

If `extract_df` is called on an object created using `nlp.pipe` it will format the output with 1 row for each document and a column for each metric.
```py
docs = nlp.pipe(['The world is changed. I feel it in the water. I feel it in the earth. I smell it in the air. Much that once was is lost, for none now live who remember it.',
            'He felt that his whole life was some kind of dream and he sometimes wondered whose it was and whether they were enjoying it.'])

td.extract_df(doc, metrics="dependency_distance")
```

TODO: add output

If you don't want to include the `text` column set `include_text` to `False`.


Textdescriptives works for any language that has a spaCy model.
```py
nlp = spacy.load("da_core_news_sm")
docs = nlp.pipe(['Da jeg var atten, tog jeg patent på ild. Det skulle senere vise sig at blive en meget indbringende forretning',
            "Spis skovsneglen, Mulle. Du vil jo gerne være med i hulen, ikk'?"])

td.extract_df(docs, include_text = False)
```

### Readability

The readability measures are largely derived from the [textstat](https://github.com/shivam5992/textstat) library and are thoroughly defined there.

### Dependency Distance
Mean dependency distance can be used as a way of measuring the average syntactic complexity of a text. 

## Metrics
Metrics currently implemented:

1. Descriptive statistics - mean, median, standard deviation of the following:
  * Word length
  * Sentence length, words
  * Syllables per word
  * Number of characters
  * Number of sentences
  * Number of types (unique words)
  * Number of tokens (total words)
  * Type/toḱen ratio

2. Readability metrics:
  * Gunning-Fog
  * SMOG
  * Flesch reading ease
  * Flesch-Kincaid grade
  * Automated readability index
  * Coleman-Liau index
  * Lix
  * Rix
  
 4. Dependency distance metrics:
  * Mean dependency distance, sentence level (mean, standard deviation)
  * Mean proportion adjacent dependency relations, sentence level (mean, standard devaiation)
  
  ## Authors

  Developed by Lasse Hansen at the [Center for Humanities Computing Aarhus](https://chcaa.io)

  Collaborators:

  *  Ludvig Renbo Olsen ([@ludvigolsen]( https://github.com/ludvigolsen ), [ludvigolsen.dk]( http://ludvigolsen.dk ))
