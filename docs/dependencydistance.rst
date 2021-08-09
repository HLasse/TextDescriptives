Dependency Distance
--------------------

The *dependency_distance* component adds measures of depedency distance to both :code:`Doc`, :code:`Span`, and :code:`Token` objects under the ._.dependency_distance attribute.
Dependency distance can be used a measure of syntactics complexity (the greater the distance, the more complex). 

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