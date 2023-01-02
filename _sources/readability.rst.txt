Readability
--------------------

The *readability* component adds the following readabiltiy metrics under the :code:`._.readability` attribute to :code:`Doc` objects.

* Gunning-Fog
* SMOG
* Flesch reading ease
* Flesch-Kincaid grade
* Automated readability index
* Coleman-Liau index
* Lix
* Rix

For specifics of the implementation, refer to the source.±

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

====  =========================  =====================  ======================  =======  =============  =============================  ====================  =======  =====
  ..  text                         flesch_reading_ease    flesch_kincaid_grade     smog    gunning_fog    automated_readability_index    coleman_liau_index      lix    rix
====  =========================  =====================  ======================  =======  =============  =============================  ====================  =======  =====
   0  The world is changed(...)                107.879              -0.0485714  5.68392        3.94286                       -2.45429             -0.708571  12.7143    0.4
====  =========================  =====================  ======================  =======  =============  =============================  ====================  =======  =====

-----

Component
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. autofunction:: textdescriptives.components.readability.create_readability_component
