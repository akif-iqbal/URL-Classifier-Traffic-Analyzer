import pickle
from sre_parse import Tokenizer
from tkinter import N
import numpy as np
#import matplotlib.pyplot as plt
import pandas as pd

from sklearn.model_selection import train_test_split, RandomizedSearchCV
from sklearn.preprocessing import StandardScaler
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import confusion_matrix, accuracy_score
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction.text import TfidfVectorizer

def makeTokens(f):
    tkns_BySlash = str(f.encode('utf-8')).split('/')	# make tokens after splitting by slash
    total_Tokens = []
    for i in tkns_BySlash:
        tokens = str(i).split('-')	# make tokens after splitting by dash
        tkns_ByDot = []
        for j in range(0,len(tokens)):
            temp_Tokens = str(tokens[j]).split('.')	# make tokens after splitting by dot
            tkns_ByDot = tkns_ByDot + temp_Tokens
        total_Tokens = total_Tokens + tokens + tkns_ByDot
    total_Tokens = list(set(total_Tokens))	#remove redundant tokens
    if 'com' in total_Tokens:
        total_Tokens.remove('com')	#removing .com since it occurs a lot of times and it should not be included in our features
    return total_Tokens

df = pd.read_csv('datasets/url_classification.csv')
urls = df['URL']
y = df['Category']

print('checkpoint-1')

vectorizer = TfidfVectorizer(tokenizer = makeTokens)
X = vectorizer.fit_transform(urls)

print('checkpoint-2')

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.25, random_state=0)
# X_train = vectorizer.fit_transform(X_train)
# X_test = vectorizer.fit_transform(X_test)

print('checkpoint-3')

param_grid = {  'n_estimators': np.arange(50, 200, 15),
                'max_features': np.arange(0.1, 1, 0.1),
                'max_depth': [3, 5, 7, 9],
                'max_samples': [0.3, 0.5, 0.8]}

# rf = RandomizedSearchCV(RandomForestClassifier(n_jobs=-1), param_grid, n_iter=15, error_score='raise')
rf = RandomForestClassifier(n_estimators=10, criterion = 'entropy', random_state = 5, n_jobs=-1, max_depth=100)
print('checkpoint-4')
rf.fit(X_train, y_train)
print('checkpoint-5')
with open('build/model.pkl', 'wb') as fid:
    pickle.dump(rf, fid)
# rf = rf.best_estimator_

# rf = RandomForestClassifier(n_estimators=10, criterion = 'entropy', random_state = 0, n_jobs=-1, max_depth=7)
# print('checkpoint-4')
# rf.fit(X_train, y_train)

# print('checkpoint-5')

# y_pred = rf.predict(X_test)
# print('checkpoint-6')
# cm = confusion_matrix(y_test, y_pred)
# print(cm)
# print(accuracy_score(y_test, y_pred))

load_model = pickle.load(open('build/model.pkl', 'rb'))
y_pred = load_model.predict(X_test)
cm = confusion_matrix(y_test, y_pred)
print(cm)
result = load_model.score(X_test, y_test)
print(result)

X_predict = ["google.com", "wikipedia.org", "friv.com"]
X_predict = vectorizer.transform(X_predict)
new_predict = load_model.predict(X_predict)
print(new_predict)