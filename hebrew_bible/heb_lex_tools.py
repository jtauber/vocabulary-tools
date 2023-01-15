import os
import sys


class HEBLEX():
    def __init__(self):
        self.data = {}
        self.strongs = {}
        self.lemmas = {}
        with open(os.path.join(os.path.dirname(__file__),'heb_lex.txt'), 'r', encoding="UTF-8") as f:
            for line in f:
                strong, index, bdb, form, gloss = line.replace('\n', '').split("\t", maxsplit=4)
                self.data[form] = gloss
                self.strongs[strong] = gloss
                self.lemmas[strong] = form
    
    
    def strongs_to_gloss(self,i):
        if i in self.strongs:
            return self.strongs[i]
        else:
            print(f"{i} not in Strongs->gloss data", file=sys.stderr)
            return '??'
            
            
    def lemma_to_gloss(self,i):
        if i in self.data:
            return self.data[i]
        else:
            print(f"{i} not in lemma->gloss data", file=sys.stderr)
            return '??'
            
            
    def strongs_to_lemma(self,i):
        if i in self.lemmas:
            return self.lemmas[i]
        else:
            print(f"{i} not in Strongs->lemma data", file=sys.stderr)
            return '??'
            
    


