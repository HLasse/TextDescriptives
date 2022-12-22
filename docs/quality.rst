Quality
--------------------

The :code:`quality` component adds the following quality metrics under the
:code:`._.quality`` attribute to :code:`Doc` and :code:`Span` objects. 

Heuristic quality metrics:

* Number of stop words (:code:`n_stop_words``): The number of stop words in the document.
* Alpha Ratio (:code:`alpha_ratio`): Ratio of words containing at least one alphabetic characters.
* Mean word length (:code:`mean_word_length`): Mean/average word length.
* Proportion of ellipsis (:code:`proportion_ellipsis`): Proportion of lines in a documents which end with an ellipsis.
* Proportion of bullet points (:code:`proportion_bullet_points`): Proportion of lines in a documents which start with a bullet point.
* Symbol to word ratio (:code:`symbol_{symbol}_2_word_ratio`): Ratio of specified symbols to words, could e.g. include ratio of hashtags or curly brackets.
* Contains string (:code:`contains_{string}`): Whether the document contains a specified string. For instance documents containing the string "lorem ipsum".

Repetitious text metrics:

* Duplicate lines character fraction (:code:`duplicate_lines_chr_fraction`): Fraction of characters in a document which are contained within duplicate lines.
* Duplicate paragraphs character fraction (:code:`duplicate_paragraphs_chr_fraction`): Fraction of characters in a document which are contained within duplicate paragraphs.
* Duplicate n-gram character fraction (:code:`duplicate_{n}_gram_chr_fraction`): Fraction of characters in a document which are contained within duplicate n-grams. For a speciifed n-gram range.
* Top n-gram character fraction (:code:`top_{n}_gram_chr_fraction`): Fraction of characters in a document which are contained within the top n-grams. For a speciifed n-gram range.


These quality metrics were for example used by
`Rae et al. (2021) <https://arxiv.org/abs/2112.11446>`__ and
`Raffel et al. (2020) <https://arxiv.org/abs/1910.10683>`__ to filter large text
corpora for pre-training language models.

Note: this implementation is not optimized for speed, but rather for usability, simplicity, and spacy integration.
If you need to run quality filters on a large corpus, you should consider using the implementation from
`Danish Foundation Models <https://github.com/centre-for-humanities-computing/danish-foundation-models>`__ which also
includes a number of other quality filters and deduplication strategies.


Usage
~~~~~~

.. code-block:: python

    import spacy
    import textdescriptives as td
    nlp = spacy.load("en_core_web_sm")
    nlp.add_pipe("textdescriptives.quality") 
    doc = nlp("The world is changed. I feel it in the water. I feel it in the earth. I smell it in the air. Much that once was is lost, for none now live who remember it.")

    # all attributes are stored as a dict in the ._.quality attribute
    doc._.quality
    # check if the document passed all quality checks
    doc._.passed_quality_check

    # extract to dataframe
    td.extract_df(doc)


====  =========================  ==============  =============  ==================  ============  =====================  ==========================  =============================  ==================================  ===============================  ===============================  ===============================  ===============================  ===============================  ================================  =========================  =========================  =========================  =======================  ======================  ======================
  ..  text                         n_stop_words    alpha_ratio    mean_word_length    doc_length    proportion_ellipsis    proportion_bullet_points    duplicate_line_chr_fraction    duplicate_paragraph_chr_fraction    duplicate_5-gram_chr_fraction    duplicate_6-gram_chr_fraction    duplicate_7-gram_chr_fraction    duplicate_8-gram_chr_fraction    duplicate_9-gram_chr_fraction    duplicate_10-gram_chr_fraction    top_2-gram_chr_fraction    top_3-gram_chr_fraction    top_4-gram_chr_fraction    symbol_#_2_word_ratio  contains_lorem ipsum    passed_quality_check
====  =========================  ==============  =============  ==================  ============  =====================  ==========================  =============================  ==================================  ===============================  ===============================  ===============================  ===============================  ===============================  ================================  =========================  =========================  =========================  =======================  ======================  ======================
   0  The world is changed(...)              24       0.853659             2.95122            41                      0                           0                              0                                   0                         0.232258                         0.232258                                0                                0                                0                                 0                  0.0580645                   0.174194                          0                        0  False                   False
====  =========================  ==============  =============  ==================  ============  =====================  ==========================  =============================  ==================================  ===============================  ===============================  ===============================  ===============================  ===============================  ================================  =========================  =========================  =========================  =======================  ======================  ======================


If you want to specify the thresholds for the quality metrics, you can do so by passing a
`QualityThresholds <https://textdescriptives.readthedocs.io/en/latest/api/textdescriptives.components.quality.html#textdescriptives.components.quality.QualityThresholds>`__ object to the component.

.. code-block:: python

    import spacy
    import textdescriptives as td
    nlp = spacy.load("en_core_web_sm")

    # set thresholds for quality metrics (these are just the default)
    thresholds = QualityThresholds(
        n_stop_words(2, None),
        alpha_ratio=(0.8, None),
        mean_word_length=(3, 10),
        doc_length= (10, 100_000),
        symbol_hashtag_to_word_ratio=(None, 0.1),
        proportion_ellipsis=(None, 0.3),
        proportion_bullet_points=(None, 0.8),
        duplicate_line_chr_fraction=(None, 0.2),
        duplicate_paragraph_chr_fraction=(None, 0.2),
        duplicate_5gram_chr_fraction=(None, 0.15),
        duplicate_6gram_chr_fraction=(None, 0.14),
        duplicate_7gram_chr_fraction=(None, 0.13),
        duplicate_8gram_chr_fraction=(None, 0.12),
        duplicate_9gram_chr_fraction=(None, 0.11),
        duplicate_10gram_chr_fraction=(None, 0.1),
        top_2gram_chr_fraction=(None, 0.20),
        top_3gram_chr_fraction=(None, 0.18),
        top_4gram_chr_fraction=(None, 0.16),
        contains_lorem_ipsum=False
    )

    nlp.add_pipe("textdescriptives.quality", config={"quality_thresholds": thresholds.dict()})
    doc = nlp("The world is changed. I feel it in the water. I feel it in the earth. I smell it in the air. Much that once was is lost, for none now live who remember it.")

    # all attributes are stored as a dict in the ._.quality attribute
    doc._.quality
    # check if the document passed all quality checks
    doc._.passed_quality_check


-----


Component
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. autofunction:: textdescriptives.components.quality.create_quality_component

Data Classes
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. autopydantic_model:: textdescriptives.components.quality.QualityThresholds

