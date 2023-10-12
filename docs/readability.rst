
Readability
------------


The *readability* component adds the following readabiltiy metrics under the :code:`._.readability` attribute to :code:`Doc` objects. 

.. note:: Note, that the hyphenation module (Pyphen) does not support all languages. If the language is not supported, a warning will be raised and np.nan will be set as the value for metrics requiring hyphenation.



* **`Gunning-Fog <https://en.wikipedia.org/wiki/Gunning_fog_index>`__**, is a readability index originally developed for English writing, but works for any language. The index estimates the years of formal education needed to understand the text on a first reading. A Gunning-Fog index of 12 requires the reading level of a U.S. high school senior (around 18 years old). The formula for calculating the index is:

    *Grade level = 0.4 × (ASL + PHW)*

    Where *ASL* is the average sentence length (total words / total sentences), and *PHW* is the percentage of hard words (words with three or more syllables).

    Note: requires hyphenation.

* **`SMOG <https://en.wikipedia.org/wiki/SMOG>`__**, or Simple Measure of Gobbledygook, is a readability formula that estimates the years of education required to understand a piece of writing. It primarily focuses on the complexity of words, using the number of polysyllabic words in the text. The formula is:

    *SMOG Index = 1.043 × √(30 × (hard words / n_sentences)) + 3.1291*

    Note: requires hyphenation.

* **`Flesch reading ease <https://en.wikipedia.org/wiki/Flesch%E2%80%93Kincaid_readability_tests#Flesch_reading_ease>`__**, is a readability score that indicates how easy a text is to read. Higher scores indicate easier reading, while lower scores indicate more difficult reading. The score is calculated using the following formula:

    *Flesch Reading Ease = 206.835 - (1.015 × ASL) - (84.6 × ASW)*

    Where *ASL* is the average sentence length and *ASW* is the average number of syllables per word.

    Note: requires hyphenation.

* **`Flesch-Kincaid grade <https://en.wikipedia.org/wiki/Flesch%E2%80%93Kincaid_readability_tests#Flesch%E2%80%93Kincaid_grade_level>`__**, is a readability metric that estimates the grade level needed to comprehend a text. It is based on the average sentence length and average number of syllables per word. The formula is:

    *Flesch-Kincaid Grade = 0.39 × (ASL) + 11.8 × (ASW) - 15.59*

    Note: requires hyphenation.

* **`Automated readability index <https://en.wikipedia.org/wiki/Automated_readability_index>`__**, is a readability test that calculates an approximate U.S. grade level needed to understand a text. It is based on the average number of characters per word and the average sentence length. The formula is:

    *ARI = 4.71 × (n_chars / n_words) + 0.5 × (n_words / n_sentences) - 21.43*

* **`Coleman-Liau index <https://en.wikipedia.org/wiki/Coleman%E2%80%93Liau_index>`___**, is a readability test that estimates the U.S. grade level needed to understand a text. It is based on the average number of letters per 100 words and the average number of sentences per 100 words. The original formula is:

    *CLI = 0.0588 × L - 0.296 × S - 15.8*

    Where *L* is the average number of characters per 100 words and *S* is the average number of sentences per 100 words. In our implementation we average over the entire text instead of just 100 words.

* **`Lix <https://en.wikipedia.org/wiki/Lix_(readability_test)>`__**, or Lesbarhetsindex, is a readability measure that calculates a readability score based on the average sentence length and the percentage of long words (more than six characters) in the text. The formula is:

    *Lix = (n_words / n_sentences) + (n_long_words * 100) / n_words*

* **`Rix <https://www.jstor.org/stable/40031755>`__**, is a readability measure that estimates the difficulty of a text based on the proportion of long words (more than six characters) in the text. The formula is:

    *Rix = (n_long_words / n_sentences)*



Usage
~~~~~~

.. code-block:: python

    import spacy
    import textdescriptives as td
    nlp = spacy.load("en_core_web_sm")
    nlp.add_pipe("textdescriptives/readability") 
    doc = nlp("The world is changed. I feel it in the water. I feel it in the earth. I smell it in the air. Much that once was is lost, for none now live who remember it.")

    # all attributes are stored as a dict in the ._.readability attribute
    doc._.readability

    # extract to dataframe
    td.extract_df(doc)

====  =========================  =====================  ======================  =======  =============  =============================  ====================  =======  =====  ===================  =====================  ==================  ======================  ========================  =====================  ==========================  ============================  =========================  ==========  =================  ==========================  ==============  =============
  ..  text                         flesch_reading_ease    flesch_kincaid_grade     smog    gunning_fog    automated_readability_index    coleman_liau_index      lix    rix    token_length_mean    token_length_median    token_length_std    sentence_length_mean    sentence_length_median    sentence_length_std    syllables_per_token_mean    syllables_per_token_median    syllables_per_token_std    n_tokens    n_unique_tokens    proportion_unique_tokens    n_characters    n_sentences
====  =========================  =====================  ======================  =======  =============  =============================  ====================  =======  =====  ===================  =====================  ==================  ======================  ========================  =====================  ==========================  ============================  =========================  ==========  =================  ==========================  ==============  =============
   0  The world is changed(...)                107.879              -0.0485714  5.68392        3.94286                       -2.45429             -0.708571  12.7143    0.4              3.28571                      3             1.54127                       7                         6                3.09839                     1.08571                             1                   0.368117          35                 23                    0.657143             121              5
====  =========================  =====================  ======================  =======  =============  =============================  ====================  =======  =====  ===================  =====================  ==================  ======================  ========================  =====================  ==========================  ============================  =========================  ==========  =================  ==========================  ==============  =============


-----

Component
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. autofunction:: textdescriptives.components.readability.create_readability_component

