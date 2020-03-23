
import numpy as np
import pandas as pd

def call_by_language(clss, texts, langs, **kwargs, ):
    """
    Processes the texts grouped by their each language.
    We there only call n_languages times.
    Restores order to fit the passed texts.
    """

    def call_for_lang(lang, inds = None):
        if inds is not None:
            current_texts = [texts[i] for i in inds]
        else:
            current_texts = texts
        df = clss(
            current_texts, lang = lang, **kwargs).df
        if inds is not None:
            df["text_index"] = inds
        return df

    unique_langs = list(set(langs))
    if len(unique_langs) == 1:
        return call_for_lang(langs[0])
    langs = np.asarray(langs)
    lang_inds = {la:np.argwhere(langs == la).flatten() \
        for la in np.asarray(unique_langs)}
    results = pd.concat([call_for_lang(language, indices) \
        for language,indices in lang_inds.items()], 
        axis = 0).sort_values(by="text_index").drop(columns = ["text_index"])
    return results
    

    