Descriptive Statistics
----------------------

The *descriptive_stats* component extracts a number of descriptive statistics. 
The following attributes are added:

* ._.counts (:code:`Doc` & :code:`Span`) 
  
  *  Number of tokens.
  *  Number of unique tokens.
  *  Proportion unique tokens.
  *  Number of characters.
* ._.sentence_length(:code:`Doc`)

  * Mean sentence length.
  * Median sentence length.
  * Std of sentence length.
* ._.syllables(:code:`Doc`)

  * Mean number of syllables per token.
  * Median number of syllables per token.
  * Std of number of syllables per token.
* ._.token_length(:code:`Doc` & :code:`Span`) 
  
  * Mean token length.
  * Median token length.
  * Std of token length.

textdescriptives.components.descriptive_stats
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. automodule:: textdescriptives.components.descriptive_stats
   :members:
   :undoc-members:
   :show-inheritance:

.. :exclude-members: function
.. for functions you wish to exclude