import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler 
from sklearn.svm import SVC
from sklearn.metrics import confusion_matrix, accuracy_score
import pickle


class SVM(object):

  def process(self):
    dataset = pd.read_csv('ids.csv')
    dataset.drop("Timestamp",axis=1,inplace=True)
    dataset["Flow Pkts/s"]=pd.to_numeric(dataset["Flow Pkts/s"],errors="coerce")
    dataset.dropna(inplace=True)
    dataset.replace([np.inf, -np.inf, np.nan], -1, inplace=True)
    X = dataset.iloc[:, :-1].values
    y = dataset.iloc[:, -1].values
    self.X_train, self.X_test, self.y_train, self.y_test = train_test_split(X, y, test_size = 0.20, random_state = 0)
    self.X_train = np.nan_to_num(self.X_train)
    self.X_test = np.nan_to_num(self.X_test)
    sc=StandardScaler()
    self.X_train = sc.fit_transform(self.X_train)
    self.X_test = sc.transform(self.X_test)
    return self.X_train,self.X_test,self.y_train,self.y_test

  def training(self):
    self.Xtrain,self.X_test,self.y_train,self.y_test=self.process()
    self.classifier = SVC(kernel = 'linear', random_state = 0)
    self.classifier.fit(self.X_train,self.y_train)
    pickle.dump(self.classifier, open('svm_model.pkl', 'wb'))
    return self.classifier

 
  
  def testing(self):
    self.X_train,self.X_test,self.y_train,self.y_test=self.process()
    y_pred = self.classifier.predict(self.X_test)
    print(self.classifier.predict([[11,1,1,1,1,0,0,0,0,0,0,0,0,0,0,0,2000000,1,0,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,40,200,1000000,1000000,0,0,0,0,0,0,0,0,1,0,0,0,0,1,0,0,0,0,0,0,0,0,0,1,0,2,0,26883,0,0,80,0,0,0,0,0,0,0,0]]))
    
    cm = confusion_matrix(self.y_test, y_pred)
    print(cm)
    self.score=accuracy_score(self.y_test, y_pred)
    return self.score
  


if __name__=="__main__":
  s=SVM()
  data=s.process()
  train=s.training()
  test=s.testing()
  # svm=pickle.load(open('svm_model.pkl','rb'))
  # print(svm.predict([[11,1,1,1,1,0,0,0,0,0,0,0,0,0,0,0,2000000,1,0,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,40,200,1000000,1000000,0,0,0,0,0,0,0,0,1,0,0,0,0,1,0,0,0,0,0,0,0,0,0,1,0,2,0,26883,0,0,80,0,0,0,0,0,0,0,0]]))
 

