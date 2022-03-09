import numpy as np
import pandas as pd
from sklearn.linear_model import LinearRegression as lm

# Let try using all the numerical variables as predictors to 
# train data using linear regression

# read the data "complete_data_sentiment":
df = pd.read_csv("C:/ucla/m148/SM148_project/complete_data/complete_data_sentiment.csv")
pd.set_option('display.max_columns', None) # <- to display all the columes

df.head()

# linear regression with variable confirmed case, mask mandate, likes, and retweets:
# since categorical variable mentions_mask and Face_Masks_Required_in_Public are important
# in our observation, we coerce them to numerical variables:

sample = df[['Confirmed','Face_Masks_Required_in_Public', 'likes', 'retweets', 'mentions_mask', 'polarity_compound']]
sample = sample.dropna()
x = sample[['Confirmed', 'Face_Masks_Required_in_Public', 'likes', 'retweets', 'mentions_mask']]
x


# coerce Face_Masks_Required_in_Public variable to numerical as mask_mandate:
x['mask_mandate'] = 0
x.loc[x['Face_Masks_Required_in_Public'] == 'Yes', 'mask_mandate'] = 1
x = x[['Confirmed', 'mask_mandate', 'likes', 'retweets', 'mentions_mask']]
x
# coerce mask_mandate variable to numerical:
x['mentions_mask_num'] = 0
x.loc[x['mentions_mask'] == 'True', 'mentions_mask_num'] = 1
x = x[['Confirmed', 'mask_mandate', 'likes', 'retweets', 'mentions_mask_num']]
x

y = sample[['polarity_compound']]
y
model = lm().fit(x, y)
# show the R-square:
print("coefficient of determination (R-square): ", model.score(x, y))
# R-square is so low; Thu, sentiment(polarity_compound) cannot be explained by this model.
