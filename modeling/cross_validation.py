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


# read data:
df = pd.read_csv("C:/ucla/m148/SM148_project/complete_data.csv")
len(df.index)

pd.set_option('display.max_columns', None) # <- just to display all the columes

df.head()

# Split Polarity into three categories, save as a addition column (-1 to 0: negative; 0 to 1: positive):
df['Pol_cat'] = 0 # neutral
df.loc[df['Polarity'] < 0, 'Pol_cat'] = -1 # negative
df.loc[df['Polarity'] > 0, 'Pol_cat'] = 1 # positive
df.head()

df['masks_num'] = 0
df.loc[df['mentions_mask'] == True, 'masks_num'] = 1 
df['required_masks'] = 0
df.loc[df['Face_Masks_Required_in_Public'] == 'Yes', 'required_masks'] = 1 

x, y = df[['masks_num', 'required_masks']], df['Pol_cat']
x.shape



x_train, x_test, y_train, y_test = train_test_split(x,y, test_size = 0.4, random_state =0)
clf = svm.SVC(kernel = 'linear', C = 1).fit(x_train, y_train)
clf.score(x_test, y_test)


# try SVM for cross validation:
clf = svm.SVC(kernel = 'linear', C = 1, random_state = 42)
scores = cross_val_score(clf, x, y, cv = 5)
scores.mean()

# cross validation mean score for SVM is only 0.44607794717460314.



# trying logistic regression model.

