Quick Start
=======================


Use :code:`extract_metrics` to quickly extract your desired metrics. Available metrics are :code:`["descriptive_stats", "readability", "dependency_distance", "pos_proportions", "coherence", "quality]`

Set the :code:`spacy_model` parameter to specify which spaCy model to use, otherwise, TextDescriptives will auto-download an appropriate one based on :code:`lang`. If :code:`lang` is set, :code:`spacy_model` is not necessary and vice versa.

Specify which metrics to extract in the :code:`metrics` argument. :code:`None` extracts all metrics. 

.. code-block:: python

   import textdescriptives as td

   text = "The world is changed. I feel it in the water. I feel it in the earth. I smell it in the air. Much that once was is lost, for none now live who remember it."
   # will automatically download the relevant model (´en_core_web_lg´) and extract all metrics
   df = td.extract_metrics(text=text, lang="en", metrics=None)

   # specify spaCy model and which metrics to extract
   df = td.extract_metrics(text=text, spacy_model="en_core_web_lg", metrics=["readability", "coherence"])


Usage with spaCy
------------------

To integrate with other spaCy pipelines, import the library and add the component(s) to your pipeline using the standard spaCy syntax. Available components are :code:`descriptive_stats`, :code:`readability`, :code:`dependency_distance`, :code:`pos_proportions`, :code:`coherence`, and :code:`quality` prefixed with :code:`textdescriptives/`. 
If you want to add all the components you can use the shorthand :code:`textdescriptives/all`.


.. code-block:: python

   import spacy
   import textdescriptives as td
   nlp = spacy.load("en_core_web_sm")
   nlp.add_pipe("textdescriptives/all") 
   doc = nlp("The world is changed. I feel it in the water. I feel it in the earth. I smell it in the air. Much that once was is lost, for none now live who remember it.")

   # access some of the values
   doc._.readability
   doc._.token_length

The calculated metrics can be conveniently extracted to a Pandas DataFrame using the :code:`extract_df` function or to a dictionary using the :code:`extract_dict` function.


.. code-block:: python

   td.extract_df(doc)
   td.extract_dict(doc)

You can control which measures to extract with the *metrics* argument.

.. code-block:: python

   td.extract_df(doc, metrics = ["descriptive_stats", "readability", "dependency_distance", "pos_proportions", "coherence", "quality", "information_theory"])

.. note::
   By default, the :code:`extract_X` functions adds a column containing the text. You can change this behaviour by setting :code:`include_text = False`.

:code:`extract_df` and :code:`extract_dict` also work on objects created by :code:`nlp.pipe`. The output will be formatted with 1 row for each document and a column for each metric.

.. code-block:: python

   docs = nlp.pipe(['The world is changed. I feel it in the water. I feel it in the earth. I smell it in the air. Much that once was is lost, for none now live who remember it.',
   'He felt that his whole life was some kind of dream and he sometimes wondered whose it was and whether they were enjoying it.'])
   td.extract_df(docs, metrics = "dependency_distance")

Using Specific Components
=========================

TextDescriptives includes 6 components that can be used individually: :code:`descriptive_stats`, :code:`readability`, :code:`dependency_distance`, :code:`pos_proportions`, :code:`coherence`, and :code:`quality`. 
This can be helpful if you're only interested in e.g. readabiltiy metrics or descriptive statistics and don't to run a dependency parser.
If you have imported the TextDesriptives package you can add them to a pipe using the standard spaCy syntax.

.. code-block:: python

   nlp = spacy.blank("da")
   nlp.add_pipe("textdescriptives/descriptive_stats")
   docs = nlp.pipe(['Da jeg var atten, tog jeg patent på ild. Det skulle senere vise sig at blive en meget indbringende forretning',
            "Spis skovsneglen, Mulle. Du vil jo gerne være med i hulen, ikk'?"])
   # extract_df is clever enough to only extract metrics that are in the Doc
   td.extract_df(docs, include_text = False)



Available Attributes
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
   ":code:`Doc._.pos_proportions`","`pos_proportions`","Dict containing the proportion of each part-of-speech tag in the Doc."
   ":code:`Doc._.coherence`","`coherence`","Dict containing the first and second order coherence scores for the Doc."
   ":code:`Doc._.quality`","`quality`","Dict containing the quality scores for the Doc."
   ":code:`Doc._.passed_quality_check`","`quality`","Boolean indicator of whether the doc passed the quality check."
   ":code:`Doc._.information_theory`","`information_theory`","Dict containing the information theory scores for the Doc."
   ":code:`Doc._.entropy`","`information_theory`","The entropy score for the Doc as a float."
   ":code:`Doc._.perplexity`","`information_theory`","The perplexity score for the Doc as a float."
   ":code:`Doc._.per_word_perplexity`","`information_theory`","The per-word perplexity score for the Doc as a float."
   ":code:`Span._.token_length`","`descriptive_stats`","Dict containing mean, median, and std of token length in the span."
   ":code:`Span._.counts`","`descriptive_stats`","Dict containing the number of tokens, number of unique tokens, proportion unique tokens, and number of characters in the span."
   ":code:`Span._.dependency_distance`","`dependency_distance`","Dict containing the mean dependency distance and proportion adjacent dependency relations in the Doc."
   ":code:`Span._.quality`","`quality`","Dict containing the quality scores for the Span."
   ":code:`Span._.entropy`","`information_theory`","The entropy score for the Span as a float."
   ":code:`Span._.perplexity`","`information_theory`","The perplexity score for the Span as a float."
   ":code:`Span._.per_word_perplexity`","`information_theory`","The per-word perplexity score for the Span as a float."
   ":code:`Token._.dependency_distance`","`dependency_distance`","Dict containing the dependency distance and whether the head word is adjacent for a Token."

   
   