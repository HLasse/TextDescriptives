import os
import stanfordnlp
import numpy as np

class Dep_distance():
    def __init__(self, text, lang, snlp_path):
        self.text = text
        self.lang = lang
        if snlp_path is None:
            self.snlp_path = os.getcwd() + '/snlp_resources'
        else:
            self.snlp_path = snlp_path

        self.dep_dist()

    def dl_missing_langs_snlp(self):
        """
        Downloads any missing languages from Stanford NLP resources
        """
        import stanfordnlp
        
        if not os.path.exists(self.snlp_path):
            os.makedirs(self.snlp_path)

        dl_langs = [folder[:2] for folder in os.listdir(self.snlp_path)]

        if self.lang not in dl_langs:
            stanfordnlp.download(self.lang, resource_dir=self.snlp_path)

    def dep_dist(self):
        """
        Calculates dependency distance of the text on sentence level

        """
        #Check if snlp language resources are installed, otherwise download them
        try: 
            self.dl_missing_langs_snlp()
            # If the specified language is not in SNLP, throw error and stop the function
        except ValueError:
            ValueError(f"Language '{self.lang}' does not exist in stanford NLP. Try specifying another language")
                
        if 's_nlp' not in globals():
            global s_nlp
            s_nlp = stanfordnlp.Pipeline(lang = self.lang, models_dir = self.snlp_path, 
                    processors="tokenize,pos,depparse")

        # Calculating DD for each text
        list_sent_dep_dist = []
        list_sent_prop_adj_rel = []
        for txt in self.text:
            doc = s_nlp(txt)

            parsed = [(sent_n, word.index, word.governor, word.dependency_relation) for sent_n, sent in enumerate(doc.sentences) for word in sent.words]

            n_sentences = set([token[0] for token in parsed])

            sent_dep_dist = []
            sent_prop_adjacent_relation = []
            for sentence in n_sentences:
                dep_dists = []
                adj_rel = 0
                tokens = 0
                for sent_n, idx, governor, dep_relation in parsed:
                    if sent_n == sentence:
                        if dep_relation != 'root':
                            dist = abs(governor - int(idx))
                            dep_dists.append(dist)
                            if dist == 1:
                                adj_rel += 1
                        else:
                            dep_dists.append(0)
                        tokens += 1
                sent_dep_dist.append(sum(dep_dists) / len(dep_dists))
                prop_adjacent =  adj_rel / tokens

                sent_prop_adjacent_relation.append(prop_adjacent)
            
            list_sent_dep_dist.append(sent_dep_dist)
            list_sent_prop_adj_rel.append(sent_prop_adjacent_relation)

        self.sent_dep_dist = list_sent_dep_dist
        self.sent_prop_adjacent_relation = list_sent_prop_adj_rel

    def mean_dep_dist(self):
        """
        Calculates mean dependency distance
        """
        mdd = [np.mean(text) for text in self.sent_dep_dist]

        return mdd

    def std_dep_dist(self):
        """
        Calculates the standard deviation of the sentence level mean dependency distance
        """
        std_dd = [np.std(text) for text in self.sent_dep_dist]

        return std_dd
    
    def proportion_adjacent_dep(self):
        """
        Calculates the average proportion of adjacent dependency relations on sentence level
        """
        prop_adj_dep = [np.mean(prop_adj) for prop_adj in self.sent_prop_adjacent_relation]
        
        return prop_adj_dep

    def std_proportion_adjacent_dep(self):
        """
        Calculates the standard deviation of the proportion of adjacent dependency relations on sentence level
        """
        std_prop_adj_dep = [np.std(prop_adj) for prop_adj in self.sent_prop_adjacent_relation]

        return std_prop_adj_dep


#texts = ["Her er et par sætninger på dansk. Der er bare to. Måske er der tre, men de er ret korte",
#        "Endnu en lille hyggesætning her, der dog er noget længere og med en lang referent. Det må jeg nok sige, sikke dog en lang sætning."]

#text = ["Bare en enkelt sætning for lige at teste"]

#dep = Dep_distance(texts, 'da', snlp_path)
