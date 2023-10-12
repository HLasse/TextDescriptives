Part-of-Speech Proportions
-----------------------------

The *pos_proportions* component adds one attribute to a Doc or Span:

* :code:`Doc._.pos_proportions` 
    * Dict of :code:`{pos_prop_POSTAG: proportion of all tokens tagged with POSTAG}`. By default creates a key for each possible POS tag. This behaviour can be turned off 
    by setting :code:`add_all_tags=False` in the component's initialization.


* :code:`Span._.pos_proportions`
* 
    * Dict of :code:`{pos_prop_POSTAG: proportion of all tokens tagged with POSTAG}`. 
    


Usage
~~~~~~

.. code-block:: python

    import spacy
    import textdescriptives as td
    nlp = spacy.load("en_core_web_sm")
    nlp.add_pipe("textdescriptives/pos_proportions") 
    doc = nlp("The world is changed. I feel it in the water. I feel it in the earth. I smell it in the air. Much that once was is lost, for none now live who remember it.")

    # all attributes are stored as a dict in the ._.pos_proportions attribute
    doc._.pos_proportions

    # extract to dataframe
    td.extract_df(doc)


====  =========================  ==============  ==============  ==============  ==============  ================  ==============  ===============  ===============  ==============  ===============  ===============  ================  ================  ================  ==============  ===============  ============
  ..  text                         pos_prop_ADJ    pos_prop_ADP    pos_prop_ADV    pos_prop_AUX    pos_prop_CCONJ    pos_prop_DET    pos_prop_INTJ    pos_prop_NOUN    pos_prop_NUM    pos_prop_PART    pos_prop_PRON    pos_prop_PROPN    pos_prop_PUNCT    pos_prop_SCONJ    pos_prop_SYM    pos_prop_VERB    pos_prop_X
====  =========================  ==============  ==============  ==============  ==============  ================  ==============  ===============  ===============  ==============  ===============  ===============  ================  ================  ================  ==============  ===============  ============
   0  The world is changed(...)       0.0243902        0.097561       0.0487805       0.0731707                 0        0.097561                0         0.121951               0                0         0.195122                 0          0.146341         0.0243902               0         0.170732             0
====  =========================  ==============  ==============  ==============  ==============  ================  ==============  ===============  ===============  ==============  ===============  ===============  ================  ================  ================  ==============  ===============  ============

-----


Component
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. autofunction:: textdescriptives.components.pos_proportions.create_pos_proportions_component