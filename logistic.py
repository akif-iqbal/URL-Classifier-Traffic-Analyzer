import pickle
import pandas as pd
from pandas import read_csv
import sklearn.metrics as metrics

from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.feature_extraction.text import TfidfVectorizer

def modifiedTokenizer(f):
        tokensBySlash = str(f.encode('utf-8')).split('/')
        totalTokens = []
        for i in tokensBySlash:
            tokensByHyphen = str(i).split('-')
            tokensByDot = []
            for j in range(0,len(tokensByHyphen)):
                tokensTemp = str(tokensByHyphen[j]).split('.')
                tokensByDot = tokensByDot + tokensTemp
            totalTokens = totalTokens + tokensByHyphen + tokensByDot
        totalTokens = list(set(totalTokens))
        if 'com' in totalTokens:
            totalTokens.remove('com')
        return totalTokens


class LogisReg(object):

    def process(self):
        urls_data = pd.read_csv('datasets/mal_legit_classification.csv')
        y = urls_data["label"]
        url_list = urls_data["url"]
        self.vectorizer = TfidfVectorizer(tokenizer=modifiedTokenizer)
        X = self.vectorizer.fit_transform(url_list)
        self.X_train, self.X_test, self.y_train, self.y_test = train_test_split(X, y, test_size=0.3, random_state=42)
        pickle.dump(self.vectorizer, open('build/vecto.pkl', 'wb'))
        return self.X_train, self.X_test, self.y_train, self.y_test
 

    def training(self):
        self.X_train,self.X_test,self.y_train,self.y_test=self.process()
        self.logit = LogisticRegression(random_state=0, solver='sag')	
        self.logit.fit(self.X_train, self.y_train)
        print(metrics.accuracy_score(self.y_train,self.logit.predict(self.X_train)))
        print(metrics.accuracy_score(self.y_test,self.logit.predict(self.X_test)))
        pickle.dump(self.logit, open('build/logistic.pkl', 'wb'))
        return self.logit

    def testing(self,website):
        self.process()
        load_model = pickle.load(open('build/logistic.pkl', 'rb'))
        vectori = pickle.load(open('build/vecto.pkl', 'rb'))
        X_predict = website
        X_predict = vectori.transform(X_predict)
        new_predict = load_model.predict(X_predict)
        return new_predict

if __name__=="__main__":
    s=LogisReg()
    data=s.process()
    train=s.training()
    test=s.testing()
    print("Output: ", test)
