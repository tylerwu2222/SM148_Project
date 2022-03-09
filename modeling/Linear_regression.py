import numpy as np
import pandas as pd
from sklearn.linear_model import LinearRegression as lm

# read the data "complete_data_sentiment":
df = pd.read_csv("C:/ucla/m148/SM148_project/complete_data/complete_data_sentiment.csv")
pd.set_option('display.max_columns', None) # <- just to display all the columes

df.head()

# linear regression with variable confirmed case, mask mandate:
sample = df[['Confirmed','Face_Masks_Required_in_Public', 'Polarity']]
sample = sample.dropna()
x = sample[['Confirmed','Face_Masks_Required_in_Public']]
x
# transform mask_mandate variable to numerical:
x['mask_mandate'] = 0
x.loc[x['Face_Masks_Required_in_Public'] == 'Yes', 'mask_mandate'] = 1
x = x[['Confirmed', 'mask_mandate']]
x
y = sample[['Polarity']]
y
model = lm().fit(x, y)
# show the R-square:
print("coefficient of determination (R-square): ", model.score(x, y))
# R-square is so low. Its cannot explained by this model.
