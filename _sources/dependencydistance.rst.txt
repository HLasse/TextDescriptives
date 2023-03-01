Dependency Distance
--------------------

The *dependency_distance* component adds measures of dependency distance to both :code:`Doc`, :code:`Span`, and :code:`Token` objects 
under the :code:`._.dependency_distance` attribute.
Dependency distance can be used a measure of syntactics complexity, the greater the distance, the more complex 
(`Liu 2008 <https://pdfs.semanticscholar.org/b6b9/cf00698a76d7a1e5ba58baa92d8799366813.pdf>`__, `Oya 2011 <http://www.paaljapan.org/conference2011/ProcNewest2011/pdf/poster/P-13.pdf>`__). 

The implementation in textdescriptives follows Oya, 2011. We calculate the distances 
from each token to their dependent, and take the mean of this for calculating the mean 
dependency distance for spans. We then calculate the Doc level dependency distance by
averaging over the sentence-level mean dependency distances.

Please see `this issue <https://github.com/HLasse/TextDescriptives/issues/77>`__ for
how to calculate the dependency distance metric proposed by Liu, 2008 with TextDescriptives.


For :code:`Doc` objects, the mean and standard deviation of dependency distance on the
sentence level is returned along with the mean and standard deviation of the proportion
adjacent dependency relations on sentence level.

For :code:`Span` objects, the mean dependency distance and the mean proportion adjacent
dependency relations in the span are returned.

For :code:`Token` objects, the dependency distance and whether the dependency relation
is an adjacent token is returned. 

Usage
~~~~~~

.. code-block:: python

   import spacy
   import textdescriptives as td
   nlp = spacy.load("en_core_web_sm")
   nlp.add_pipe("textdescriptives/dependency_distance") 
   doc = nlp("The world is changed. I feel it in the water. I feel it in the earth. I smell it in the air. Much that once was is lost, for none now live who remember it.")

   # all attributes are stored as a dict in the ._.dependency_distance attribute
   doc._.dependency_distance

   # access span and token level dependency distance in the same way
   doc[:3]._.dependency_distance
   doc[1]._.dependency_distance

   # extract to dataframe
   td.extract_df(doc)

====  =========================  ==========================  =========================  ========================================  =======================================
  ..  text                         dependency_distance_mean    dependency_distance_std    prop_adjacent_dependency_relation_mean    prop_adjacent_dependency_relation_std
====  =========================  ==========================  =========================  ========================================  =======================================
   0  The world is changed(...)                     1.77524                   0.553188                                  0.457143                                0.0722806
====  =========================  ==========================  =========================  ========================================  =======================================

-----


Component
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. autofunction:: textdescriptives.components.dependency_distance.create_dependency_distance_component

