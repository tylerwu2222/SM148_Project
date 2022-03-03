from pyexpat import model
import tweepy
import pandas as pd
import numpy as np
import os
import shutil
import glob
from datetime import datetime as dt
import re
import random
import os
from sklearn import svm
from sklearn.model_selection import cross_val_score
from sklearn import datasets
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression


# read data:
df = pd.read_csv("C:/ucla/m148/SM148_project/complete_data/complete_data_sentiment.csv")
len(df.index)

pd.set_option('display.max_columns', None) # <- just to display all the columes

df.head()


df['masks_num'] = 0
df.loc[df['mentions_mask'] == True, 'masks_num'] = 1 
df['required_masks'] = 0
df.loc[df['Face_Masks_Required_in_Public'] == 'Yes', 'required_masks'] = 1 

x, y = df[['masks_num', 'required_masks']], df['polarity_classif']
x.shape



x_train, x_test, y_train, y_test = train_test_split(x,y, test_size = 0.4, random_state =0)
clf = svm.SVC(kernel = 'linear', C = 1).fit(x_train, y_train)
clf.score(x_test, y_test)


# try SVM for cross validation:
clf = svm.SVC(kernel = 'linear', C = 1, random_state = 42)
scores = cross_val_score(clf, x, y, cv = 5)
scores.mean()
# cross validation mean score for SVM is only 0.44607794717460314.


# add the "likes" as one of the predictors.
x, y = df[['masks_num', 'required_masks', 'likes']], df['Pol_cat']

# trying logistic regression model.
model = LogisticRegression()
scores = cross_val_score(model, x, y, scoring = 'accuracy', cv =10)
scores.mean()
# cross validation mean score for SVM is only 0.4460779473034691.
