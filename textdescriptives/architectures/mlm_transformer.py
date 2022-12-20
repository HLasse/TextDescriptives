"""
Copyright (C) 2022 Explosion AI and Kenneth Enevoldsen - All Rights Reserved
You may use, distribute and modify this code under the
terms of the MIT license.

Original code from:
https://github.com/explosion/spacy-transformers/blob/master/spacy_transformers/architectures.py


The following functions are modified:
- create_SequenceClassificationTransformerModel_v1. Changed to call
ClassificationTransformerModel instead of TransformerModel
- create_TokenClassificationTransformerModel_v1. Changed to call
ClassificationTransformerModel instead of TransformerModel
"""


from typing import Callable, List

from spacy.tokens import Doc
from spacy_transformers import FullTransformerBatch
from spacy_transformers.util import registry
from spacy_wrap.layers.clf_transformer_model import ClassificationTransformerModel
from thinc.api import Model
from transformers import (
    AutoModelForSequenceClassification,
    AutoModelForTokenClassification,
)


@registry.architectures.register("spacy-wrap.SequenceClassificationTransformerModel.v1")
def create_SequenceClassificationTransformerModel_v1(
    name: str,
    get_spans: Callable,
    tokenizer_config: dict = {},
    transformer_config: dict = {},
    mixed_precision: bool = False,
    grad_scaler_config: dict = {},
) -> Model[List[Doc], "FullTransformerBatch"]:
    """Initialize a ClassificationTransformerModel using the
    AutoModelForSequenceClassification from transformers. This model is used
    for sequence classification tasks, such as sentiment analysis or hate
    speech detection.

    Args:
        name (str): Name of the Huggingface model to use.
        get_spans (Callable[[List[Doc]], List[List[Span]]]): A function to extract
            spans from the batch of Doc objects. See the "TransformerModel" layer
            for details.
        tokenizer_config (dict): Settings to pass to the transformers tokenizer.
        transformers_config (dict): Settings to pass to the transformers forward pass
            of the transformer.
        mixed_precision (bool): Enable mixed-precision. Mixed-precision replaces
            whitelisted ops to half-precision counterparts. This speeds up training
            and prediction on modern GPUs and reduces GPU memory use.
        grad_scaler_config (dict): Configuration for gradient scaling in mixed-precision
            training. Gradient scaling is enabled automatically when mixed-precision
            training is used.
            Setting `enabled` to `False` in the gradient scaling configuration disables
            gradient scaling. The `init_scale` (default: `2 ** 16`) determines the
            initial scale. `backoff_factor` (default: `0.5`) specifies the factor
            by which the scale should be reduced when gradients overflow.
            `growth_interval` (default: `2000`) configures the number of steps
            without gradient overflows after which the scale should be increased.
            Finally, `growth_factor` (default: `2.0`) determines the factor by which
            the scale should be increased when no overflows were found for
            `growth_interval` steps.
    """
    model = ClassificationTransformerModel(
        name=name,
        get_spans=get_spans,
        model_cls=AutoModelForSequenceClassification,
        tokenizer_config=tokenizer_config,
        transformer_config=transformer_config,
        mixed_precision=mixed_precision,
        grad_scaler_config=grad_scaler_config,
    )
    return model


@registry.architectures.register("spacy-wrap.TokenClassificationTransformerModel.v1")
def create_TokenClassificationTransformerModel_v1(
    name: str,
    get_spans: Callable,
    tokenizer_config: dict = {},
    transformer_config: dict = {},
    mixed_precision: bool = False,
    grad_scaler_config: dict = {},
) -> Model[List[Doc], "FullTransformerBatch"]:
    """Initialize a ClassificationTransformerModel using the
    AutoModelForTokenClassification from transformers. This model is used for
    token classification tasks, such as named entity recognition.

    Args:
        name (str): Name of the Huggingface model to use.
        get_spans (Callable[[List[Doc]], List[List[Span]]]): A function to extract
            spans from the batch of Doc objects. See the "TransformerModel" layer
            for details.
        tokenizer_config (dict): Settings to pass to the transformers tokenizer.
        transformers_config (dict): Settings to pass to the transformers forward pass
            of the transformer.
        mixed_precision (bool): Enable mixed-precision. Mixed-precision replaces
            whitelisted ops to half-precision counterparts. This speeds up training
            and prediction on modern GPUs and reduces GPU memory use.
        grad_scaler_config (dict): Configuration for gradient scaling in mixed-precision
            training. Gradient scaling is enabled automatically when mixed-precision
            training is used.
            Setting `enabled` to `False` in the gradient scaling configuration disables
            gradient scaling. The `init_scale` (default: `2 ** 16`) determines the
            initial scale. `backoff_factor` (default: `0.5`) specifies the factor
            by which the scale should be reduced when gradients overflow.
            `growth_interval` (default: `2000`) configures the number of steps
            without gradient overflows after which the scale should be increased.
            Finally, `growth_factor` (default: `2.0`) determines the factor by which
            the scale should be increased when no overflows were found for
            `growth_interval` steps.
    """
    model = ClassificationTransformerModel(
        name=name,
        get_spans=get_spans,
        model_cls=AutoModelForTokenClassification,
        tokenizer_config=tokenizer_config,
        transformer_config=transformer_config,
        mixed_precision=mixed_precision,
        grad_scaler_config=grad_scaler_config,
    )
    return model
