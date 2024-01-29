""" Calculation of statistics related to dependency distance."""

from typing import Callable

import numpy as np
from spacy.language import Language
from spacy.tokens import Doc, Span, Token


class DependencyDistance:
    """spaCy v.3.0 component that adds attributes to `Doc`, `Span`, and `Token`
    objects relating to dependency distance.

    Dependency distance can be used as a measure of syntactic complexity, and
    measures the distance from a word to its head word. For `Doc` objects,
    dependency distance is calculated on the sentence level.
    """

    def __init__(self, nlp: Language):
        """Initialise components."""
        if not Token.has_extension("dependency_distance"):
            Token.set_extension("dependency_distance", getter=self.token_dependency)
        if not Span.has_extension("dependency_distance"):
            Span.set_extension("dependency_distance", getter=self.span_dependency)
        if not Doc.has_extension("dependency_distance"):
            Doc.set_extension("dependency_distance", getter=self.doc_dependency)

    def token_dependency(self, token: Token) -> dict:
        """Calculate token level dependency distance, i.e. the distance from a
        token to its head token. Also returns a boolean indicating whether the
        dependency relation is adjacent to the token.

        Returns:
            dict: Dictionary with the following keys:
                - dependency_distance: Dependency distance
                - adjacent_dependency: Boolean indicating whether the dependency
                  relation is adjacent to the token
        """
        dep_dist = 0
        ajd_dep = False
        if token.dep_ != "ROOT":
            dep_dist = abs(token.head.i - token.i)
            if dep_dist == 1:
                ajd_dep = True
        return {"dependency_distance": dep_dist, "adjacent_dependency": ajd_dep}

    def span_dependency(self, span: Span) -> dict:
        """Aggregates token level dependency distance on the span level by
        taking the mean of the dependency distance and the proportion of
        adjacent dependency relations.

        Returns:
            dict: Dictionary with the following keys: dependency_distance_mean:
                Mean dependency distance and prop_adjacent_dependency_relation:
                Proportion of adjacent dependency relations
        """
        dep_dists, adj_deps = zip(
            *[token._.dependency_distance.values() for token in span],
        )
        return {
            "dependency_distance_mean": np.mean(dep_dists),
            "prop_adjacent_dependency_relation": np.mean(adj_deps),
        }

    def doc_dependency(self, doc: Doc) -> dict:
        """Aggregates token level dependency distance on the document level by
        taking the mean of the dependency distance and the proportion of
        adjacent dependency relations on the sentence level.

        Returns:
            dict: Dictionary with the following keys:
                - dependency_distance_mean: Mean dependency distance on the sentence
                  level
                - dependency_distance_std: Standard deviation of dependency distance on
                  the sentence level
                - prop_adjacent_dependency_relation_mean: Mean proportion of adjacent
                  dependency relations on the sentence level
                - prop_adjacent_dependency_relation_std: Standard deviation of
                  proportion of adjacent dependency relations on the sentence level
        """
        if len(doc) == 0:
            return {
                "dependency_distance_mean": np.nan,
                "dependency_distance_std": np.nan,
                "prop_adjacent_dependency_relation_mean": np.nan,
                "prop_adjacent_dependency_relation_std": np.nan,
            }
        dep_dists, adj_deps = zip(
            *[sent._.dependency_distance.values() for sent in doc.sents],
        )
        return {
            "dependency_distance_mean": np.mean(dep_dists),
            "dependency_distance_std": np.std(dep_dists),
            "prop_adjacent_dependency_relation_mean": np.mean(adj_deps),
            "prop_adjacent_dependency_relation_std": np.std(adj_deps),
        }

    def __call__(self, doc: Doc):
        """Run the pipeline component."""
        return doc


@Language.factory(
    "textdescriptives/dependency_distance",
    assigns=[
        "token._.dependency_distance",
        "span._.dependency_distance",
        "doc._.dependency_distance",
    ],
)
def create_dependency_distance_component(
    nlp: Language,
    name: str,
) -> Callable[[Doc], Doc]:
    """Create spaCy language factory that allows DependencyDistance attributes
    to be added to a pipe using
    nlp.add_pipe("textdescriptives/dependency_distance")

    Adding this component to a pipeline sets the following attributes:
        - `token._.dependency_distance`
        - `span._.dependency_distance`
        - `doc._.dependency_distance`

    Args:
        nlp (Language): spaCy language object, does not need to be specified in the
            nlp.add_pipe call.
        name (str): name of the component. Can be optionally specified in the
            nlp.add_pipe call, using the name argument.

    Returns:
        Callable[[Doc], Doc]: The DependencyDistance component

    Example:
        >>> import spacy
        >>> nlp = spacy.load("en_core_web_sm")
        >>> nlp.add_pipe("textdescriptives/dependency_distance")
        >>> # apply the pipeline to a text
        >>> doc = nlp("This is a sentence.")
        >>> # access the dependency distance attributes
        >>> doc._.dependency_distance
    """
    return DependencyDistance(nlp)
