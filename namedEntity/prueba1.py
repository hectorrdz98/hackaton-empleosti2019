import pandas as pd
import numpy as np

data = pd.read_csv("ner_dataset.csv", encoding="latin1")
data = data.fillna(method="ffill")
data.tail(10)

words = list(set(data["Word"].values))
n_words = len(words); print(n_words)

class SentenceGetter(object):
    
    def __init__(self, data):
        self.n_sent = 1
        self.data = data
        self.empty = False
    
    def get_next(self):
        try:
            s = self.data[self.data["Sentence #"] == "Sentence: {}".format(self.n_sent)]
            self.n_sent += 1
            return s["Word"].values.tolist(), s["POS"].values.tolist(), s["Tag"].values.tolist()    
        except:
            self.empty = True
            return None, None, None

getter = SentenceGetter(data)

sent, pos, tag = getter.get_next()
print(sent); print(pos); print(tag)




from sklearn.base import BaseEstimator, TransformerMixin

class MemoryTagger(BaseEstimator, TransformerMixin):
    
    def fit(self, X, y):
        '''
        Expects a list of words as X and a list of tags as y.
        '''
        voc = {}
        self.tags = []
        for x, t in zip(X, y):
            if t not in self.tags:
                self.tags.append(t)
            if x in voc:
                if t in voc[x]:
                    voc[x][t] += 1
                else:
                    voc[x][t] = 1
            else:
                voc[x] = {t: 1}
        self.memory = {}
        for k, d in voc.items():
            self.memory[k] = max(d, key=d.get)
    
    def predict(self, X, y=None):
        '''
        Predict the the tag from memory. If word is unknown, predict 'O'.
        '''
        return [self.memory.get(x, 'O') for x in X]

tagger = MemoryTagger()

tagger.fit(sent, tag)

print(tagger.predict(sent))

print(tagger.tags)


from sklearn.model_selection import cross_val_predict
from sklearn.metrics import classification_report

words = data["Word"].values.tolist()
tags = data["Tag"].values.tolist()

pred = cross_val_predict(estimator=MemoryTagger(), X=words, y=tags, cv=5)
report = classification_report(y_pred=pred, y_true=tags)
print(report)



from sklearn.ensemble import RandomForestClassifier

def feature_map(word):
    '''Simple feature map.'''
    return np.array([word.istitle(), word.islower(), word.isupper(), len(word),
                     word.isdigit(),  word.isalpha()])

words = [feature_map(w) for w in data["Word"].values.tolist()]

pred = cross_val_predict(RandomForestClassifier(n_estimators=20),
                         X=words, y=tags, cv=5)

report = classification_report(y_pred=pred, y_true=tags)
print(report)