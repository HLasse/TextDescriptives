Part-of-Speech Proportions
-------------------------

The *pos_stats* component adds one attribute to a Doc or Span:

* ._.proportions (:code:`Doc`) 
    * Dict of :code:`{pos_prop_POSTAG: proportion of all tokens tagged with POSTAG}`. Does not create a key if no tokens in the document fit the POSTAG.

* ._.proportions (:code:`Span`) 
    * Dict of :code:`{pos_prop_POSTAG: proportion of all tokens tagged with POSTAG}`. Does not create a key if no tokens in the document fit the POSTAG.


Usage
~~~~~~

.. code-block:: python

    import spacy
    import textdescriptives as td
    nlp = spacy.load("en_core_web_sm")
    nlp.add_pipe("textdescriptives.pos_proportions") 
    doc = nlp("The world is changed. I feel it in the water. I feel it in the earth. I smell it in the air. Much that once was is lost, for none now live who remember it.")

    # all attributes are stored as a dict in the ._.pos_proportions attribute
    doc._.pos_proportions

    # extract to dataframe
    td.extract_df(doc)


textdescriptives.components.pos_proportions
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. automodule:: textdescriptives.components.pos_proportions
   :members:
   :undoc-members:
   :show-inheritance:

.. :exclude-members: function
.. for functions you wish to exclude
