import pickle
import os
# from sre_parse import Tokenizer
# from tkinter import N
# import numpy as np
# import pandas as pd
# from scipy import sparse

# from sklearn.pipeline import Pipeline
# from sklearn.model_selection import train_test_split, RandomizedSearchCV
# from sklearn.preprocessing import StandardScaler, LabelEncoder, MinMaxScaler, label_binarize, OneHotEncoder
# from sklearn.ensemble import RandomForestClassifier
# from sklearn.multiclass import OneVsRestClassifier
# from sklearn.naive_bayes import MultinomialNB, GaussianNB, BernoulliNB
# from sklearn.neighbors import KNeighborsClassifier
# from sklearn.metrics import confusion_matrix, accuracy_score, roc_curve, auc
# from sklearn.feature_extraction.text import CountVectorizer
# from sklearn.feature_extraction.text import TfidfVectorizer, TfidfTransformer

filename = 'svm_stem(3,3).pkl'
loaded_model = pickle.load(open('build/'+filename, 'rb'))
_ = os.system('cls')
print('business today: ', loaded_model.predict(['http://www.businesstoday.net/']))
print('miniclip: ', loaded_model.predict(['http://www.miniclip.com/']))
print('friv: ', loaded_model.predict(['http://www.friv.com/']))
print('pesuacademy: ', loaded_model.predict(['http://www.pesuacademy.com/']))
print('bbc: ', loaded_model.predict(['http://www.bbc.com/']))
print('jbl: ', loaded_model.predict(['http://www.jbl.com/']))
print('croma: ', loaded_model.predict(['http://www.croma.com/']))
print('google: ', loaded_model.predict(['http://www.google.com/']))