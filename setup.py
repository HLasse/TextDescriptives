import setuptools

with open("textdescriptives/about.py") as f:
    v = f.read()
    for l in v.split("\n"):
        if l.startswith("__version__"):
            __version__ = l.split('"')[-2]

with open("README.md", encoding="utf-8") as f:
    long_description = f.read()

with open("requirements.txt", encoding="utf-8") as f:
    requirements = f.read().split("\n")

setuptools.setup(
    name="textdescriptives",
    version=__version__,
    description="A library for calculating a variety of features from text using spaCy",
    license="Apache License 2.0",
    long_description=long_description,
    long_description_content_type="text/markdown",
    author="Lasse Hansen",
    author_email="lasseh0310@gmail.com",
    url="https://github.com/HLasse/textdescriptives",
    packages=["textdescriptives"],
    install_requires=[
        "spacy>=3.0.3",
        "numpy>=1.20.0",
        "pandas>=1.0.0",
        "pyphen>=0.11.0",
    ],
    # See https://pypi.python.org/pypi?%3Aaction=list_classifiers
    classifiers=[
        # How mature is this project? Common values are
        #   3 - Alpha
        #   4 - Beta
        #   5 - Production/Stable
        "Development Status :: 4 - Beta",
        # Indicate who your project is intended for
        "Intended Audience :: Science/Research",
        "Topic :: Scientific/Engineering",
        "Topic :: Text Processing",
        # Specify the Python versions you support here. In particular, ensure
        # that you indicate whether you support Python 2, Python 3 or both.
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
    ],
    keywords="NLP",
)
