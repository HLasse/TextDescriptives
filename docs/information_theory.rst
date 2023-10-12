Information Theory
--------------------

The `information_theory` component calculates information theoretic measures derived 
from the text. These include:

- `{doc/span}._.entropy`: the Shannon entropy of the text using the `token.prob` as the probability
  of each token. Entropy is defined as :math:`H(X) = -\sum_{i=1}^n p(x_i) \log_e p(x_i)`. Where :math:`p(x_i)` is the probability of the token :math:`x_i`.
- `{doc/span}._.perplexity`: the perplexity of the text. perplexity is a measurement of how well a
  probability distribution or probability model predicts a sample. Perplexity is defined as :math:`PPL(X) = e^{-H(X)}`, where :math:`H(X)` is the entropy of the text.
- `{doc/span}._.per_word_perplexity`: The perplexity of the text, divided by the number of words. Can se considered the length normalized perplexity.

These information theoretic measures is for example often used to describe the complexity of a text. 
The higher the entropy, the more complex the text is.
Similarly, one could imagine filtering text based on the per word perplexity given the assumption that
highly surprising text is in fact non-coherent text pieces.

.. note:: The information theory components require an available lexeme prop table from spaCy which is not available for all languages. A warning will be raised and values set to np.nan if the table cannot be found for the language.

Usage
~~~~~~~

.. code-block:: python

  import spacy
  from textdescriptives as td
  nlp = spacy.load("en_core_web_lg")
  nlp.add_pipe("textdescriptives/information_theory")

  doc = nlp("This is a simple text")
  
  # extract perplexity
  doc._.perplexity

  # extract entropy
  doc._.entropy

  # extract all metrics to a dataframe
  td.extract_df(doc)


=== ================================= ================== ================== ==================
 ..  text                               entropy            perplexity        per_word_perplexity
=== ================================= ================== ================== ==================
 0  This is a very likely sentence.       0.288195         1.334017              0.190574
=== ================================= ================== ================== ==================


-----

Component
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. autofunction:: textdescriptives.components.information_theory.create_information_theory_component