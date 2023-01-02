Descriptive Statistics
----------------------

The *descriptive_stats* component extracts a number of descriptive statistics. 
The following attributes are added:

* :code:`{Doc/Span}._.counts`

  *  Number of tokens.
  *  Number of unique tokens.
  *  Proportion unique tokens.
  *  Number of characters.

* :code:`{Doc/Span}._.sentence_length`

  * Mean sentence length.
  * Median sentence length.
  * Std of sentence length.

* :code:`{Doc/Span}._.syllables`

  * Mean number of syllables per token.
  * Median number of syllables per token.
  * Std of number of syllables per token.

* :code:`{Doc/Span}._.token_length`
  
  * Mean token length.
  * Median token length.
  * Std of token length.

Usage
~~~~~~

.. code-block:: python

  import spacy
  import textdescriptives as td
  nlp = spacy.load("en_core_web_sm")
  nlp.add_pipe("textdescriptives/descriptive_stats") 
  doc = nlp("The world is changed. I feel it in the water. I feel it in the earth. I smell it in the air. Much that once was is lost, for none now live who remember it.")

  # all attributes are stored as a single dict in the ._.descriptive_stats attribute
  doc._.descriptive_stats
  
  # or individually 
  doc._.counts
  doc._.sentence_length
  doc._.syllables
  doc._.token_length
  
  # extract to dataframe
  td.extract_df(doc)

====  =========================  ===================  =====================  ==================  ======================  ========================  =====================  ==========================  ============================  =========================  ==========  =================  ==========================  ==============  =============
  ..  text                         token_length_mean    token_length_median    token_length_std    sentence_length_mean    sentence_length_median    sentence_length_std    syllables_per_token_mean    syllables_per_token_median    syllables_per_token_std    n_tokens    n_unique_tokens    proportion_unique_tokens    n_characters    n_sentences
====  =========================  ===================  =====================  ==================  ======================  ========================  =====================  ==========================  ============================  =========================  ==========  =================  ==========================  ==============  =============
   0  The world is changed(...)              3.28571                      3             1.54127                       7                         6                3.09839                     1.08571                             1                   0.368117          35                 23                    0.657143             121              5
====  =========================  ===================  =====================  ==================  ======================  ========================  =====================  ==========================  ============================  =========================  ==========  =================  ==========================  ==============  =============

-----


Component
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. autofunction:: textdescriptives.components.descriptive_stats.create_descriptive_stats_component
