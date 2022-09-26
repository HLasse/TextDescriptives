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
`Raffel et al. (2020) <https://arxiv.org/abs/1910.10683>`__` to filter large text
corpora for pre-training language models.

Note: this implementation is not optimized for speed, but rather for usability, simplicity, and spacy integration.
If you need to run quality filters on a large corpus, you should consider using the implementation from
[Danish Foundation Models](https://github.com/centre-for-humanities-computing/danish-foundation-models) which also
includes a number of other quality filters and deduplication strategies.


Quality Component
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. autofunction:: textdescriptives.components.quality.create_quality_component
