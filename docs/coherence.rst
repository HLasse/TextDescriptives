Coherence
----------

The `coherence` components calculates the coherence of the document, based on
word embedding cosine similarity between sentences. 

textdescriptives currently implements first-order and second-order coherence. The 
implementation follows e.g. [1] and [2]:
* First-order coherence: The cosine similarity between consecutive sentences.
* Second-order coherence: The cosine similarity between sentences that are two sentences apart.

The implementation uses spacy's :code:`Span.similarity` method to calculate the
similarity between sentences. The similarity is based on the word embeddings in 
the spacy pipeline, i.e. small, medium, large, or transformer models will have 
different results. If you want to use a specific word embedding (e.g. fasttext)
you should overwrite the :code:`Doc.vector` attribute. Read more on spacy's documentation for `similarity <https://spacy.io/usage/linguistic-features#vectors-similarity>`_
and `overwriting the vector attribute <https://spacy.io/usage/linguistic-features#adding-individual-vectors>`_

The following attributes are added to :code:`Doc` objects.:

* ._.first_order_coherence_values: A list of floats, where each float is the
  cosine similarity between consecutive sentences.
* ._.second_order_coherence_values: A list of floats, where each float is the
    cosine similarity between sentences that are two sentences apart.
* ._.cohererence: a dict containing the mean coherence values for first and
  second order coherence (keys: "first_order_coherence", "second_order_coherence")

[1] Bedi, G., Carrillo, F., Cecchi, G. A., Slezak, D. F., Sigman, M., Mota, N. B., Ribeiro, S., Javitt, D. C., Copelli, M., & Corcoran, C. M. (2015). Automated analysis of free speech predicts psychosis onset in high-risk youths. Npj Schizophrenia, 1(1), Article 1. https://doi.org/10.1038/npjschz.2015.30
[2] Parola, A., Lin, J. M., Simonsen, A., Bliksted, V., Zhou, Y., Wang, H., Inoue, L., Koelkebeck, K., & Fusaroli, R. (2022). Speech disturbances in schizophrenia: Assessing cross-linguistic generalizability of NLP automated measures of coherence. Schizophrenia Research. https://doi.org/10.1016/j.schres.2022.07.002

-----

Component
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. automodule:: textdescriptives.components.coherence
   :members:
   :undoc-members:
   :show-inheritance:
