
<a href="https://github.com/HLasse/TextDescriptives"><img src="https://github.com/HLasse/TextDescriptives/raw/main/docs/_static/icon.png" width="175" height="175" align="right" /></a>


# TextDescriptives

[![spacy](https://img.shields.io/badge/built%20with-spaCy-09a3d5.svg)](https://spacy.io)
[![github actions pytest](https://github.com/hlasse/textdescriptives/actions/workflows/tests.yml/badge.svg)](https://github.com/hlasse/textdescriptives/actions)
[![github actions docs](https://github.com/hlasse/textdescriptives/actions/workflows/documentation.yml/badge.svg)](https://hlasse.github.io/TextDescriptives/)
[![status](https://joss.theoj.org/papers/06447337ee61969b5a64de484199df24/status.svg)](https://joss.theoj.org/papers/06447337ee61969b5a64de484199df24)
[![Open in Streamlit](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://huggingface.co/spaces/HLasse/textdescriptives)

A Python library for calculating a large variety of metrics from text(s) using spaCy v.3 pipeline components and extensions. 

# 🔧 Installation
`pip install textdescriptives`

# 📰 News

* We now have a TextDescriptives-powered web-app so you can extract and downloads metrics without a single line of code! Check it out [here](https://huggingface.co/spaces/HLasse/textdescriptives)
* Version 2.0 out with a new API, a new component, updated documentation, and tutorials! Components are now called by "`textdescriptives/{metric_name}`. New `coherence` component for calculating the semantic coherence between sentences. See the [documentation](https://github.com/HLasse/TextDescriptives) for tutorials and more information!  



# ⚡ Quick Start

Use `extract_metrics` to quickly extract your desired metrics. To see available methods you can simply run:
```python
import textdescriptives as td
td.get_valid_metrics()
# {'quality', 'readability', 'all', 'descriptive_stats', 'dependency_distance', 'pos_proportions', 'information_theory', 'coherence'}
```

Set the `spacy_model` parameter to specify which spaCy model to use, otherwise, TextDescriptives will auto-download an appropriate one based on `lang`. If `lang` is set, `spacy_model` is not necessary and vice versa.

Specify which metrics to extract in the `metrics` argument. `None` extracts all metrics. 

```py
import textdescriptives as td

text = "The world is changed. I feel it in the water. I feel it in the earth. I smell it in the air. Much that once was is lost, for none now live who remember it."
# will automatically download the relevant model (´en_core_web_lg´) and extract all metrics
df = td.extract_metrics(text=text, lang="en", metrics=None)

# specify spaCy model and which metrics to extract
df = td.extract_metrics(text=text, spacy_model="en_core_web_lg", metrics=["readability", "coherence"])
```


## Usage with spaCy

To integrate with other spaCy pipelines, import the library and add the component(s) to your pipeline using the standard spaCy syntax. Available components are *descriptive_stats*, *readability*, *dependency_distance*, *pos_proportions*, *coherence*, and *quality* prefixed with `textdescriptives/`. 

If you want to add all components you can use the shorthand `textdescriptives/all`.

```py
import spacy
import textdescriptives as td
# load your favourite spacy model (remember to install it first using e.g. `python -m spacy download en_core_web_sm`)
nlp = spacy.load("en_core_web_sm")
nlp.add_pipe("textdescriptives/all") 
doc = nlp("The world is changed. I feel it in the water. I feel it in the earth. I smell it in the air. Much that once was is lost, for none now live who remember it.")

# access some of the values
doc._.readability
doc._.token_length
```

TextDescriptives includes convenience functions for extracting metrics from a `Doc` to a Pandas DataFrame or a dictionary.

```py
td.extract_dict(doc)
td.extract_df(doc)
```
|      | text                      | first_order_coherence | second_order_coherence | pos_prop_DET | pos_prop_NOUN | pos_prop_AUX | pos_prop_VERB | pos_prop_PUNCT | pos_prop_PRON | pos_prop_ADP | pos_prop_ADV | pos_prop_SCONJ | flesch_reading_ease | flesch_kincaid_grade |    smog | gunning_fog | automated_readability_index | coleman_liau_index |     lix |  rix | n_stop_words | alpha_ratio | mean_word_length | doc_length | proportion_ellipsis | proportion_bullet_points | duplicate_line_chr_fraction | duplicate_paragraph_chr_fraction | duplicate_5-gram_chr_fraction | duplicate_6-gram_chr_fraction | duplicate_7-gram_chr_fraction | duplicate_8-gram_chr_fraction | duplicate_9-gram_chr_fraction | duplicate_10-gram_chr_fraction | top_2-gram_chr_fraction | top_3-gram_chr_fraction | top_4-gram_chr_fraction | symbol_#_to_word_ratio | contains_lorem ipsum | passed_quality_check | dependency_distance_mean | dependency_distance_std | prop_adjacent_dependency_relation_mean | prop_adjacent_dependency_relation_std | token_length_mean | token_length_median | token_length_std | sentence_length_mean | sentence_length_median | sentence_length_std | syllables_per_token_mean | syllables_per_token_median | syllables_per_token_std | n_tokens | n_unique_tokens | proportion_unique_tokens | n_characters | n_sentences |
| ---: | :------------------------ | --------------------: | ---------------------: | -----------: | ------------: | -----------: | ------------: | -------------: | ------------: | -----------: | -----------: | -------------: | ------------------: | -------------------: | ------: | ----------: | --------------------------: | -----------------: | ------: | ---: | -----------: | ----------: | ---------------: | ---------: | ------------------: | -----------------------: | --------------------------: | -------------------------------: | ----------------------------: | ----------------------------: | ----------------------------: | ----------------------------: | ----------------------------: | -----------------------------: | ----------------------: | ----------------------: | ----------------------: | ---------------------: | :------------------- | :------------------- | -----------------------: | ----------------------: | -------------------------------------: | ------------------------------------: | ----------------: | ------------------: | ---------------: | -------------------: | ---------------------: | ------------------: | -----------------------: | -------------------------: | ----------------------: | -------: | --------------: | -----------------------: | -----------: | ----------: |
|    0 | The world is changed(...) |              0.633002 |               0.573323 |     0.097561 |      0.121951 |    0.0731707 |      0.170732 |       0.146341 |      0.195122 |    0.0731707 |    0.0731707 |      0.0487805 |             107.879 |           -0.0485714 | 5.68392 |     3.94286 |                    -2.45429 |          -0.708571 | 12.7143 |  0.4 |           24 |    0.853659 |          2.95122 |         41 |                   0 |                        0 |                           0 |                                0 |                      0.232258 |                      0.232258 |                             0 |                             0 |                             0 |                              0 |               0.0580645 |                0.174194 |                       0 |                      0 | False                | False                |                  1.77524 |                0.553188 |                               0.457143 |                             0.0722806 |           3.28571 |                   3 |          1.54127 |                    7 |                      6 |             3.09839 |                  1.08571 |                          1 |                0.368117 |       35 |              23 |                 0.657143 |          121 |           5 |



# 📖 Documentation

TextDescriptives has a detailed documentation as well as a series of Jupyter notebook tutorials.
All the tutorials are located in the `docs/tutorials` folder and can also be found on the documentation website.


| Documentation              |                                                                                    |
| -------------------------- | ---------------------------------------------------------------------------------- |
| 📚 **[Getting started]**    | Guides and instructions on how to use TextDescriptives and its features.           |
| 👩‍💻 **[Demo]**               | A live demo of TextDescriptives.                                                   |
| 😎 **[Tutorials]**          | Detailed tutorials on how to make the most of TextDescriptives                     |
| 📰 **[News and changelog]** | New additions, changes and version history.                                        |
| 🎛 **[API References]**     | The detailed reference for TextDescriptive's API. Including function documentation |
| 📄 **[Paper]**              | The preprint of the TextDescriptives paper.                                        |

[Paper]: https://arxiv.org/abs/2301.02057
[Tutorials]: https://hlasse.github.io/TextDescriptives/tutorial.html
[Getting started]: https://hlasse.github.io/TextDescriptives/usingthepackage.html
[API References]: https://hlasse.github.io/TextDescriptives/index.html
[News and changelog]: https://hlasse.github.io/TextDescriptives/news.html
[Demo]: https://huggingface.co/spaces/HLasse/textdescriptives
