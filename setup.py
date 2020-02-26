from setuptools import setup

setup(name='textdescriptives',
      version='0.1',
      author='Lasse Hansen',
      author_email='placeholder@placeholder.com',
      description='A package for calculating a wide variety of features from text',
      long_description=open('README.md', encoding='utf-8').read(),
      long_description_content_type='text/markdown',
      url='https://github.com/HLasse/TextDescriptives',
      license='MIT',
      packages=['textdescriptives'],
      classifiers=[
            "Programming Language :: Python :: 3",
            "License :: OSI Approved :: MIT License",
            "Operating System :: OS Independent",
            "Topic :: Text Processing",
            "Topic :: NLP"
      ]
      install_requires=['pandas','numpy', 'pyphen', 'pycountry'],
      python_requires='>=3.6'
      zip_safe=False,
      include_package_data=True)

