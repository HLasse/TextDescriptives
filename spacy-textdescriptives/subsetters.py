"""Helpers to subset an extracted dataframe"""

readability_cols = [
    "flesch_reading_ease",
    "flesch_kincaid_grade",
    "smog",
    "gunning_fog",
    "automated_readability_index",
    "coleman_liau_index",
    "lix",
    "rix",
]

dependency_cols = [
    "dependency_distance_mean",
    "dependency_distance_std",
    "prop_adjacent_dependency_relation_mean",
    "prop_adjacent_dependency_relation_std",
]

descriptive_stats_cols = [
    "token_length_mean",
    "token_length_median",
    "token_length_std",
    "sentence_length_mean",
    "sentence_length_median",
    "sentence_length_std",
    "syllables_per_token_mean",
    "syllables_per_token_median",
    "syllables_per_token_std",
    "n_tokens",
    "n_unique_tokens",
    "percent_unique_tokens",
    "n_sentences",
    "n_characters",
]
