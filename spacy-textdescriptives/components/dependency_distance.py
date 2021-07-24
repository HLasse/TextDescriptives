"""Calculation of statistics related to dependency distance"""
from spacy.tokens import Doc
from spacy.language import Language

import numpy as np
import pandas as pd


@Language.factory("dependency_distance")
def create_dependency_distance_component(nlp: Language, name: str):
    return DependencyDistance(nlp)


class DependencyDistance:
    def __init__(self, nlp: Language):
        """Initialise components"""
        if not Doc.has_extension("dependency_distance"):
            Doc.set_extension("dependency_distance", getter=self.dependency_distance)

    def __call__(self, doc: Doc):
        """Run the pipeline component"""
        return doc

    def dependency_distance(self, doc: Doc):
        """Returns:
        Average sentence level dependency distance
        Standard deviation of the sentence level dependency distances
        Average proportion of adjacent dependency relations on sentence level
        Standard deviation of the proportion of adjacent dependency relations on sentence level"""

        def score_token(dep_relation: str, head: int, idx: int):
            dep_dist = 0
            adj_rel = 0
            if dep_relation != "ROOT":
                dep_dist = abs(head - int(idx))
                if dep_dist == 1:
                    adj_rel = 1
            return pd.Series([dep_dist, adj_rel])

        def score_sentence(df: pd.DataFrame):
            res = df.apply(
                lambda r: score_token(r["dep_rel"], r["head"], r["token_id"]), axis=1
            )
            token_dep_dists = res[0]
            token_adj_rels = res[1]
            dep_dist = np.mean(token_dep_dists)
            prop_adjacent = np.mean(token_adj_rels)
            return pd.Series([dep_dist, prop_adjacent])

        def score_text(doc: Doc):
            parsed = [
                (sent_n, word.i, word.head.i, word.dep_)
                for sent_n, sent in enumerate(doc.sents)
                for word in sent
            ]
            parsed = pd.DataFrame(
                parsed, columns=["sent_id", "token_id", "head", "dep_rel"]
            )
            res = parsed.groupby("sent_id").apply(score_sentence).reset_index()
            res.columns = ["sent_id", "dep_dist", "prop_adjacent"]
            return res

        df = score_text(doc)
        dep_dist, prop_adjacent = (df["dep_dist"], df["prop_adjacent"])
        avg_dd = np.mean(dep_dist)
        std_dd = np.std(dep_dist)
        avg_prop_adj_dep = np.mean(prop_adjacent)
        std_prop_adj_dep = np.std(prop_adjacent)
        return {
            "dependency_distance_mean": avg_dd,
            "dependency_distance_std": std_dd,
            "prop_adjacent_dependency_relation_mean": avg_prop_adj_dep,
            "prop_adjacent_dependency_relation_std": std_prop_adj_dep,
        }
