import pickle
from sre_parse import Tokenizer
from tkinter import N
import numpy as np
import pandas as pd
from pandas import read_csv

from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics import confusion_matrix, accuracy_score

def modifiedTokenizer(f):
        tokensBySlash = str(f.encode('utf-8')).split('/')
        totalTokens = []
        for i in tokensBySlash:
            tokens = str(i).split('-')
            tokensByDot = []
            for j in range(0,len(tokens)):
                tokensTemp = str(tokens[j]).split('.')
                tokensByDot = tokensByDot + tokensTemp
            totalTokens = totalTokens + tokens + tokensByDot
        totalTokens = list(set(totalTokens))
        if 'com' in totalTokens:
            totalTokens.remove('com')
        return totalTokens

vectorizer = TfidfVectorizer(tokenizer=modifiedTokenizer)

class LogisReg(object):

    def process(self):
        urls_data = pd.read_csv('datasets/mal_legit_classification.csv')
        y = urls_data["label"]
        url_list = urls_data["url"]
        X = vectorizer.fit_transform(url_list)
        self.X_train, self.X_test, self.y_train, self.y_test = train_test_split(X, y, test_size=0.3, random_state=42)
        return self.X_train, self.X_test, self.y_train, self.y_test


    def training(self):
        self.Xtrain,self.X_test,self.y_train,self.y_test=self.process()
        self.logit = LogisticRegression(solver='lbfgs', max_iter=500)	
        self.logit.fit(self.X_train, self.y_train)
        pickle.dump(self.logit, open('build/logistic.pkl', 'wb'))
        return self.logit

    def testing(self,website):
        load_model = pickle.load(open('build/logistic.pkl', 'rb'))
        X_predict = website
        X_predict = vectorizer.transform(X_predict)
        new_predict = load_model.predict(X_predict)
        return new_predict

if __name__=="__main__":
    s=LogisReg()
    data=s.process()
    #train=s.training()
    test=s.testing()
    print("Output: ", test)
