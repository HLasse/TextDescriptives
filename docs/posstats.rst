Part-of-Speech Statistics
----------------------

The *pos_stats* component adds one attribute to a Doc or Span:

* ._.proportions (:code:`Doc`) 
    * Dict of :code:`{pos_prop_POSTAG: proportion of all tokens tagged with POSTAG}`. Does not create a key if no tokens in the document fit the POSTAG.

* ._.proportions (:code:`Span`) 
    * Dict of :code:`{pos_prop_POSTAG: proportion of all tokens tagged with POSTAG}`. Does not create a key if no tokens in the document fit the POSTAG.

textdescriptives.components.pos_stats
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. automodule:: textdescriptives.components.pos_stats
   :members:
   :undoc-members:
   :show-inheritance:

.. :exclude-members: function
.. for functions you wish to exclude
