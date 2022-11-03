import pickle
from sre_parse import Tokenizer
from tkinter import N
import numpy as np
import pandas as pd

from sklearn.model_selection import train_test_split, RandomizedSearchCV
from sklearn.preprocessing import StandardScaler, LabelEncoder, MinMaxScaler, label_binarize, OneHotEncoder
from sklearn.ensemble import RandomForestClassifier
from sklearn.multiclass import OneVsRestClassifier
from sklearn.metrics import confusion_matrix, accuracy_score, roc_curve, auc
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction.text import TfidfVectorizer

cat_df = pd.read_csv('datasets/url_classification_random.csv')
print(f'No. of categories: {len(set(cat_df.Category))}')
print(f'Categories are : {set(cat_df.Category)}')
print(f'Total no. of records: {len(cat_df)}')
print(cat_df['Category'].value_counts())

X = cat_df.iloc[:,:-1]
y = cat_df.iloc[:,-1]

label_encoder = LabelEncoder()
label_encoder.fit(X.iloc[:,1])
X.iloc[:,1] = label_encoder.transform(X.iloc[:,1])
# label_encoder.fit(X.iloc[:,0])
# X.iloc[:,0] = label_encoder.transform(X.iloc[:,0])
# print(X)

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

min_max_scaler = MinMaxScaler()
X_train_norm = min_max_scaler.fit_transform(X_train)
print(X_train)
X_test_norm = min_max_scaler.fit_transform(X_test)

rf = RandomForestClassifier(n_jobs = -1)
print('Starting....')
rf.fit(X_train_norm, y_train)

y_pred = rf.predict(X_test_norm)
print(accuracy_score(y_test, y_pred))

print(confusion_matrix(y_test, y_pred))

X_predict = [['0', 'http://www.liquidgeneration.com/']]
X_predict = pd.DataFrame(X_predict)
# label_encoder.fit(X_predict.iloc[:,0])
label_encoder.fit(X_predict.iloc[:,1])
# X_predict.iloc[:,0] = label_encoder.transform(X_predict.iloc[:,0])
X_predict.iloc[:,1] = label_encoder.transform(X_predict.iloc[:,1])

X_predict_norm = min_max_scaler.fit_transform(X_predict)
print(X_predict_norm)

new_pred = rf.predict(X_predict_norm)
print(new_pred)