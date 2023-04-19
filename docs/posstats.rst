Part-of-Speech Proportions
-----------------------------

The *pos_proportions* component adds one attribute to a Doc or Span:

* :code:`Doc._.pos_proportions` 
    * Dict of :code:`{pos_prop_POSTAG: proportion of all tokens tagged with POSTAG}`. Does not create a key if no tokens in the document fit the POSTAG.

* :code:`Span._.pos_proportions`
* 
    * Dict of :code:`{pos_prop_POSTAG: proportion of all tokens tagged with POSTAG}`. Does not create a key if no tokens in the document fit the POSTAG.


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


====  =========================  ==============  ===============  ==============  ===============  ================  ===============  ==============  ==============  ================
  ..  text                         pos_prop_DET    pos_prop_NOUN    pos_prop_AUX    pos_prop_VERB    pos_prop_PUNCT    pos_prop_PRON    pos_prop_ADP    pos_prop_ADV    pos_prop_SCONJ
====  =========================  ==============  ===============  ==============  ===============  ================  ===============  ==============  ==============  ================
   0  The world is changed(...)        0.097561         0.121951       0.0731707         0.170732          0.146341         0.195122       0.0731707       0.0731707         0.0487805
====  =========================  ==============  ===============  ==============  ===============  ================  ===============  ==============  ==============  ================

-----


Component
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. autofunction:: textdescriptives.components.pos_proportions.create_pos_proportions_component