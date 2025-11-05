import pandas as pd 
import numpy as np 
import matplotlib.pyplot as plt
import seaborn as sns
import time
import janitor
from sklearn.preprocessing import StandardScaler


train = pd.read_csv("C:/Users/USER/Desktop/train.csv")
valid = pd.read_csv("C:/Users/USER/Desktop/val.csv")
train = train.clean_names()
valid = valid.clean_names()
train = train.drop(['id'], axis = 1)
valid_x = valid.drop(['id', 'class'], axis = 1)
valid_y = valid['class']

train.columns
valid.columns


from sklearn.neighbors import LocalOutlierFactor

minpts = np.round(np.log(train.shape[0])).astype(int)
clf = LocalOutlierFactor(n_neighbors = minpts, contamination = 0.001, novelty = True)
clf.fit(train)

from sklearn.metrics import confusion_matrix, classification_report
from sklearn import set_config

pred_val = clf.predict(valid_x)


valid_y.replace(1, -1, inplace = True)
valid_y.replace(0, 1, inplace = True)
result = pd.DataFrame({'real' : valid_y, 'pred' : pred_val})
confusion_matrix(result.real, result.pred)


from sklearn.ensemble import IsolationForest
clf = IsolationForest(random_state=0, contamination = 0.001)
clf.fit(train)

pred_val = clf.predict(valid_x)
valid_y.replace(1, -1, inplace = True)
valid_y.replace(0, 1, inplace = True)
result = pd.DataFrame({'real' : valid_y, 'pred' : pred_val})
confusion_matrix(result.real, result.pred)

print(classification_report(result.real, result.pred))