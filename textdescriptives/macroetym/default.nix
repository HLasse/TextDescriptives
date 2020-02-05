with import <nixpkgs> {};

((python37.withPackages (ps: with ps; [
  pandas
  matplotlib
  click
  numpy
  nltk
  pycountry
])).override({ignoreCollisions=true;})).env
