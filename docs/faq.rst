Frequently Asked Questions
----------------------------


How do I test the code and run the test suite?
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

This package comes with test suite to ensure functionality of the package.
To run the tests, you should clone the repository, then install the package using:

.. code-block::
   
   pip install -e .[style,tests]
   pip install -r tests/requirements.txt

This will install the required dependencies for running test as well as packages for linting. These are specified in the :code:`pyproject.toml` file.
Following this installation you can run the test suite using:

.. code-block::
   
    pytest

which will run all the test in the :code:`tests` folder.

Specific tests can be run using:

.. code-block::

   python -m pytest tests/desired_test.py


If you want to check code coverage you can run the following:

.. code-block::

   python -m pytest --cov=.


Does this package run on X?
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

This package is intended to run on all major OS, this includes Windows (latest version), MacOS (latest) and the latest version of Linux (Ubuntu). 
Similarly it also tested on python 3.7, 3.8, and 3.9.
Please note these are only the systems this package is being actively tested on, if you run on a similar system (e.g. an earlier version of Linux) this package
will likely run there as well, if not please create an issue.

How is the documentation generated?
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

This package uses `sphinx <https://www.sphinx-doc.org/en/master/index.html>`__ to generate documentation. It uses the `Furo <https://github.com/pradyunsg/furo>`__ theme with custom styling.

To make the documentation you can run:

.. code-block::

  # install sphinx, themes and extensions
  pip install ".[docs]"

  # generate html from documentations

  make -C docs html
