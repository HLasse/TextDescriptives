Installation
==================
To get started using TextDescriptives you can install it using pip by running the following line in your terminal. Optional dependendices for running the tutorials, buildings docs, running tests, or linting can be installed using the optional dependencies. 

.. code-block::

   pip install textdescriptives

Development Installation
^^^^^^^^^^^^^^^^^^^^^^^^^

To install TextDescriptives for development, clone the repository and install the
package using the following commands:

.. code-block::

   git clone https://github.com/hlasse/TextDescriptives

   pip install -e ".[style,tests,docs,tutorials]"
   
   # pip install specific dependencies for each
   # as not e.g. links currently can't be included in extra
   # dependencies
   pip install -r tests/requirements.txt
   pip install -r docs/tutorials/requirements.txt
