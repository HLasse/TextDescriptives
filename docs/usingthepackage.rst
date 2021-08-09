Using TextDescriptives
=======================

Import the library and add the component to your pipeline using the string name of the "textdescriptives" component factory:

.. code-block:: python

   import spacy
   import textdescriptives as td
   # or only load the component: 
   nlp = spacy.load("en_core_web_sm")
   nlp.add_pipe("textdescriptives") 
   doc = nlp("The world is changed. I feel it in the water. I feel it in the earth. I smell it in the air. Much that once was is lost, for none now live who remember it.")

   # access some of the values
   doc._.readability
   doc._.token_length

The calculated metrics can be conveniently extracted to a Pandas DataFrame using the :code:`extract_df` function.


.. code-block:: python

   td.extract_df(doc)

You can control which measures to extract with the *metrics* argument.

.. code-block:: python

   td.extract_df(doc, metrics = ["descriptive_stats", "readability", "dependency_distance"])

.. note::
   By default, :code:`extract_df` adds a column containing the text. You can change this behaviour by setting :code:`include_text = False`.

:code:`extract_df` also works on objects created by :code:`nlp.pipe`. The output will be formatted with 1 row for each document and a column for each metric.

.. code-block:: python

   docs = nlp.pipe(['The world is changed. I feel it in the water. I feel it in the earth. I smell it in the air. Much that once was is lost, for none now live who remember it.',
   'He felt that his whole life was some kind of dream and he sometimes wondered whose it was and whether they were enjoying it.'])
   td.extract_df(docs, metrics = "dependency_distance")

Using specific components
=========================

TextDescriptives includes 3 components that can be used individually: *descriptive_stats*, *readability*, and *dependency_distance*. 
This can be helpful if you're only interested in e.g. readabiltiy metrics or descriptive statistics and don't to run a dependency parser.
If you have imported the TextDesriptives package you can add them to a pipe using the standard spaCy syntax.

.. code-block:: python

   nlp = spacy.blank("da")
   nlp.add_pipe("descriptive_stats")
   docs = nlp.pipe(['Da jeg var atten, tog jeg patent på ild. Det skulle senere vise sig at blive en meget indbringende forretning',
            "Spis skovsneglen, Mulle. Du vil jo gerne være med i hulen, ikk'?"])
   # extract_df is clever enough to only extract metrics that are in the Doc
   td.extract_df(docs, include_text = False)


If you don't to import the entire TextDescriptives library (although it is very lightweight), you can import only the components you need.

.. code-block:: python

  from textdescriptives import (DescriptiveStatistics, 
                                Readability, 
                                DependencyDistance, 
                                TextDecriptives)


Available attributes
====================
The table below shows the metrics included in TextDecriptives and the attributes they set on spaCy's :code:`Doc`, :code:`Span`, and :code:`Token` objects.
For more details on each metrics, see the following sections in the documentation.

.. csv-table:: 
   :header: "Attribute", "Component", "Description"
   :widths: 30, 30, 40
   
   ":code:`Doc._.token_length`", "`descriptive_stats`","Dict containing mean, median, and std of token length."
   ":code:`Doc._.sentence_length`","`descriptive_stats`","Dict containing mean, median, and std of sentence length."
   ":code:`Doc._.syllables`","`descriptive_stats`","Dict containing mean, median, and std of number of syllables per token."
   ":code:`Doc._.counts`","`descriptive_stats`","Dict containing the number of tokens, number of unique tokens, proportion unique tokens, and number of characters in the Doc."
   ":code:`Doc._.readability`","`readability`","Dict containing Flesch Reading Ease, Flesch-Kincaid Grade, SMOG, Gunning-Fog, Automated Readability Index, Coleman-Liau Index, LIX, and RIX readability metrics for the Doc."
   ":code:`Doc._.dependency_distance`","`dependency_distance`","Dict containing the mean and standard deviation of the dependency distance and proportion adjacent dependency relations in the Doc."
   ":code:`Span._.token_length`","`descriptive_stats`","Dict containing mean, median, and std of token length in the span."
   ":code:`Span._.counts`","`descriptive_stats`","Dict containing the number of tokens, number of unique tokens, proportion unique tokens, and number of characters in the span."
   ":code:`Span._.dependency_distance`","`dependency_distance`","Dict containing the mean dependency distance and proportion adjacent dependency relations in the Doc."
   ":code:`Token._.dependency_distance`","`dependency_distance`","Dict containing the dependency distance and whether the head word is adjacent for a Token."