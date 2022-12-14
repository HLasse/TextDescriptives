Dependency Distance
--------------------

The *dependency_distance* component adds measures of depedency distance to both :code:`Doc`, :code:`Span`, and :code:`Token` objects under the ._.dependency_distance attribute.
Dependency distance can be used a measure of syntactics complexity, the greater the distance, the more complex (`Liu 2008 <https://pdfs.semanticscholar.org/b6b9/cf00698a76d7a1e5ba58baa92d8799366813.pdf>`__, `Oya 2011 <http://www.paaljapan.org/conference2011/ProcNewest2011/pdf/poster/P-13.pdf>`__). 

The implementation in textdescriptives follows Oya, 2011. We calculate the distances from each token to their dependent, and take the mean of this for calculating the mean dependency distance for spans. We then calculate the Doc level DD by averaging over the sentence-level mean DDs.

Please see `this issue <https://github.com/HLasse/TextDescriptives/issues/77>`__ for how to calculate the DD metric proposed by Liu, 2008 with TextDescriptives.


For :code:`Doc` objects, the mean and standard deviation of dependency distance on the sentence level is returned along with the mean and standard deviation of the proportion adjacent dependency relations on sentence level.

For :code:`Span` objects, the mean dependency distance and the mean proportion adjacent dependency relations in the span are returned.

For :code:`Token` objects, the dependency distance and whether the dependency relation is an adjacent token is returned. 

textdescriptives.components.dependency_distance
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. automodule:: textdescriptives.components.dependency_distance
   :members:
   :undoc-members:
   :show-inheritance:

.. :exclude-members: function
.. for functions you wish to exclude
