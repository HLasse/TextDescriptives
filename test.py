import spacy
import textdescriptives as td
nlp = spacy.load("en_core_web_sm")
nlp.add_pipe("textdescriptives") 
doc = nlp("The world is changed. I feel it in the water. I feel it in the earth. I smell it in the air. Much that once was is lost, for none now live who remember it.")

print(td.extract_df(doc).to_markdown())