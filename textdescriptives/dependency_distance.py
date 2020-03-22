import os
import stanfordnlp
import numpy as np
import pandas as pd

class DepDistance():
    def __init__(self, text, lang, snlp_path):
        self.text = text
        self.lang = lang
        if snlp_path is None:
            self.snlp_path = os.getcwd() + '/snlp_resources'
        else:
            self.snlp_path = snlp_path

        self.__dep_dist()
        self.__describe_distances()

    def get_sentence_distances(self):
        return self.__sentence_distances

    def get_text_distances(self):
        return self.__text_distances

    def __dl_missing_langs_snlp(self):
        """
        Downloads any missing languages from Stanford NLP resources
        """
        import stanfordnlp
        
        if not os.path.exists(self.snlp_path):
            os.makedirs(self.snlp_path)

        dl_langs = [folder[:2] for folder in os.listdir(self.snlp_path)]

        if self.lang not in dl_langs:
            stanfordnlp.download(self.lang, resource_dir=self.snlp_path)

    def __dep_dist(self):
        """
        Calculates dependency distance of the text on sentence level

        """
        #Check if snlp language resources are installed, otherwise download them
        try: 
            self.__dl_missing_langs_snlp()
            # If the specified language is not in SNLP, throw error and stop the function
        except ValueError:
            ValueError(f"Language '{self.lang}' does not exist in stanford NLP. Try specifying another language")
                
        if 's_nlp' not in globals():
            global s_nlp
            s_nlp = stanfordnlp.Pipeline(lang = self.lang, models_dir = self.snlp_path, 
                    processors="tokenize,pos,depparse")
        
        def score_token(dep_relation, governor, idx):
            dep_dist = 0
            adj_rel = 0
            if dep_relation != 'root':
                dep_dist = abs(governor - int(idx))
                if dep_dist == 1:
                    adj_rel = 1
            return pd.Series([dep_dist, adj_rel])
        
        def score_sentence(df):
            res = df.apply(
                lambda r: score_token(r["dep_rel"], r["governor"], r["word_id"]), 
                axis = 1)  
            token_dep_dists = res[0]
            token_adj_rels = res[1]
            dep_dist = np.mean(token_dep_dists)
            prop_adjacent = np.mean(token_adj_rels)
            return pd.Series([dep_dist, prop_adjacent])

        def calc_for_text(txt, txt_id):
            doc = s_nlp(txt)
            parsed = [(sent_n, word.index, word.governor, word.dependency_relation) \
                for sent_n, sent in enumerate(doc.sentences) for word in sent.words]
            parsed = pd.DataFrame(parsed, columns = ["sent_id", "word_id", "governor", "dep_rel"])
            res = parsed.groupby("sent_id").apply(score_sentence).reset_index()
            res.columns = ["sent_id", "dep_dist", "prop_adjacent"]
            res["text_id"] = txt_id
            return res

        self.__sentence_distances = pd.concat(
            [calc_for_text(txt, txt_id) \
                for txt_id, txt in enumerate(self.text)]
            )
        
    def __describe_distances(self):
        """
        Calculates: 
          Average dependency distance
          Standard deviation of the sentence level dependency distances
          Average proportion of adjacent dependency relations on sentence level
          Standard deviation of the proportion of adjacent dependency relations on sentence level
        """
        def summarizer(df):
            dep_dist, prop_adjacent = (df["dep_dist"], df["prop_adjacent"])
            avg_dd = np.mean(dep_dist)
            std_dd = np.std(dep_dist)
            avg_prop_adj_dep = np.mean(prop_adjacent)
            std_prop_adj_dep = np.std(prop_adjacent)
            return pd.DataFrame({
                "mean_dependency_distance" : avg_dd,
                "std_dependency_distance" : std_dd,
                "mean_prop_adjacent_dependency_relation" : avg_prop_adj_dep,
                "std_prop_adjacent_dependency_relation" : std_prop_adj_dep
            }, index=[0])

        self.__text_distances = self.__sentence_distances.groupby("text_id").apply(
            summarizer).reset_index(drop=True)




#texts = ["Her er et par sætninger på dansk. Der er bare to. Måske er der tre, men de er ret korte",
#        "Endnu en lille hyggesætning her, der dog er noget længere og med en lang referent. Det må jeg nok sige, sikke dog en lang sætning."]

#text = ["Bare en enkelt sætning for lige at teste"]

#dep = DepDistance(texts, 'da', snlp_path)
