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
from scipy.stats import chi2_contingency








# for data merged_test_data_with_sentiment:
df = pd.read_csv("C:/ucla/m148/SM148_project/merged_test_data_with_sentiment.csv")
len(df.index)

df.head()


# try only positive and negative: (significant)
# Split Polarity into three categories, save as a addition column (-1 to 0: negative; 0 to 1: positive):
df['Pol_cat'] = 'neutral'
df.loc[df['Polarity'] < 0, 'Pol_cat'] = 'negative'
df.loc[df['Polarity'] > 0, 'Pol_cat'] = 'positive'
df.head()

# Create a contigency table
contigency = pd.crosstab(df['Face_Masks_Required_in_Public'], df['Pol_cat'])
contigency

# Chi-square:
c, p, dof, expected = chi2_contingency(contigency)
p
# p-value in this case is 0.006674082539693579, we reject null hypothesis; there is a relationship between mask mandates and sentiment.




# try chi-square in diff time:
df['date'] = pd.to_datetime(df['date'], errors='coerce')
df['year'] = '2020'
df.loc[df['date'].dt.year == 2021, 'year'] = '2021'
df.head()
# in 2020
df_20 = df[df['date'].dt.year == 2020]
df_20['Pol_cat'] = 'neutral'
df_20.loc[df_20['Polarity'] < 0, 'Pol_cat'] = 'negative'
df_20.loc[df_20['Polarity'] > 0, 'Pol_cat'] = 'positive'
df_20.head()
# Create a contigency table
contigency = pd.crosstab(df_20['Face_Masks_Required_in_Public'], df_20['Pol_cat'])
contigency

# Chi-square:
c, p, dof, expected = chi2_contingency(contigency)
p
# p-value in this case is 0.01913496283688589, we reject null hypothesis; there is a relationship between mask mandates and sentiment.



# in 2021
df_21 = df[df['date'].dt.year == 2021]
df_21['Pol_cat'] = 'neutral'
df_21.loc[df_21['Polarity'] < 0, 'Pol_cat'] = 'negative'
df_21.loc[df_21['Polarity'] > 0, 'Pol_cat'] = 'positive'
df_21.head()
# Create a contigency table
contigency = pd.crosstab(df_21['Face_Masks_Required_in_Public'], df_21['Pol_cat'])
contigency

# Chi-square:
c, p, dof, expected = chi2_contingency(contigency)
p
# p-value in this case is 0.1702182371989688, we do not reject null hypothesis; there is no relationship between mask mandates and sentiment.








# subjectivity(score_cat) and mask mandates:
df['score_cat'] = 'high'
df.loc[df['Subjectivity'] < 0.5, 'score_cat'] = 'low'
# Create a contigency table
contigency = pd.crosstab(df['Face_Masks_Required_in_Public'], df['score_cat'])
contigency

# Chi-square:
c, p, dof, expected = chi2_contingency(contigency)
p
# p-value in this case is 0.47194439132077526, we do not reject null hypothesis; there is a no relationship between mask mandates and subjectivity.













# testing other values to split polarity column:
# Split Polarity into three categories, save as a addition column (-1 to -0.5: negative; -0.5 to 0.5: neutral; 0.5 to 1: positive):
# check the summary of "Polarity" 
df.describe()
# the addition column "Pol_cat"
df['Pol_cat'] = 'neutral'
df.loc[df['Polarity'] <= -0.5, 'Pol_cat'] = 'negative'
df.loc[df['Polarity'] >= 0.5, 'Pol_cat'] = 'positive'
df.head()

# Create a contigency table
contigency = pd.crosstab(df['Face_Masks_Required_in_Public'], df['Pol_cat'])
contigency

# Chi-square:
c, p, dof, expected = chi2_contingency(contigency)
p
# p_value is 0.14230417805646303, which is less than 0.05, do not reject null hypothesis;









# for data merged_data_with_sentiment_and_CA_LA.csv:
df = pd.read_csv("C:/ucla/m148/SM148_project/merged_data_with_sentiment_and_CA_LA.csv")
len(df.index)

# try only positive and negative: (significant)
# Split Polarity into three categories, save as a addition column (-1 to 0: negative; 0 to 1: positive):
df['Pol_cat'] = 'neutral'
df.loc[df['Polarity'] < 0, 'Pol_cat'] = 'negative'
df.loc[df['Polarity'] > 0, 'Pol_cat'] = 'positive'
df.head()

# Create a contigency table
contigency = pd.crosstab(df['Face_Masks_Required_in_Public'], df['Pol_cat'])
contigency

# Chi-square:
c, p, dof, expected = chi2_contingency(contigency)
p
# p-value in this case is 0.031708755291222995, we reject null hypothesis; there is a relationship between mask mandates and sentiment.





# By CA:
CA = df[df['CA'] =="Yes"]
CA.head()
CA['Pol_cat'] = 'neutral'
CA.loc[CA['Polarity'] < 0, 'Pol_cat'] = 'negative'
CA.loc[CA['Polarity'] > 0, 'Pol_cat'] = 'positive'
CA.head()

# Create a contigency table
contigency = pd.crosstab(CA['Face_Masks_Required_in_Public'], CA['Pol_cat'])
contigency

# Chi-square:
c, p, dof, expected = chi2_contingency(contigency)
p
# p-value in this case is 0.997104260516142, we do not reject null hypothesis; 
# there is no relationship between mask mandates and sentiment in CA.


# By LA:
la = df[df['LA'] =="Yes"]
la.head()
la['Pol_cat'] = 'neutral'
la.loc[la['Polarity'] < 0, 'Pol_cat'] = 'negative'
la.loc[la['Polarity'] > 0, 'Pol_cat'] = 'positive'
la.head()

# Create a contigency table
contigency = pd.crosstab(la['Face_Masks_Required_in_Public'], la['Pol_cat'])
contigency

# Chi-square:
c, p, dof, expected = chi2_contingency(contigency)
p
# p-value in this case is 0.6907777601096385, we do not reject null hypothesis; 
# there is no relationship between mask mandates and sentiment in LA.






























# the following code are only for testing
mod_test = pd.read_csv("C:/ucla/m148/SM148_project/tweet_data/model_test_data_with_sentiment.csv")
len(mod_test.index)



pd.set_option('display.max_columns', None) # <- just to display all the columes
mod_test.head()
mod_test.info()

mod_test.describe()



# filter data for LA:
LA_df = mod_test[mod_test.city_and_state == "Los Angeles, California"]

LA_df['score_cat'] = 'high'
LA_df.loc[LA_df['Subjectivity'] < 0.5, 'score_cat'] = 'low'

LA_df['date'] = pd.to_datetime(LA_df['date'], errors='coerce')
LA_df['year'] = '2020'
LA_df.loc[LA_df['date'].dt.year == 2021, 'year'] = '2021'


# Create a table to show the frequency of score rate in different year in LA
contigency = pd.crosstab(LA_df['year'], LA_df['score_cat'])
contigency

# Chi-square test of independence:
c, p, dof, expected = chi2_contingency(contigency)
p
# p-value is 0.7 greater than 0.05 do not reject H0



# testing code(
# filter data to 2020:
LA_df_20 = LA_df[LA_df['date'].dt.year == 2020]
LA_df_21 = LA_df[LA_df['date'].dt.year == 2021]

# seperate subjectivity score into two part:
LA_20_high = len(LA_df_20[LA_df_20.Subjectivity >= 0.5]) 
LA_20_low =len(LA_df_20[LA_df_20.Subjectivity < 0.5])

LA_21_high = len(LA_df_21[LA_df_21.Subjectivity >= 0.5]) 
LA_21_low =len(LA_df_21[LA_df_21.Subjectivity < 0.5])
# )








# filter data for NY:
NY_df = mod_test[mod_test.city_and_state == "New York, New York"]

NY_df['score_cat'] = 'high'
NY_df.loc[NY_df['Subjectivity'] < 0.5, 'score_cat'] = 'low'

NY_df['date'] = pd.to_datetime(NY_df['date'], errors='coerce')
NY_df['year'] = '2020'
NY_df.loc[NY_df['date'].dt.year == 2021, 'year'] = '2021'

# Create a table to show the frequency of score rate in different year in NY
contigency_NY = pd.crosstab(NY_df['year'], NY_df['score_cat'])
contigency_NY

# Chi-square test of independence:
c, p, dof, expected = chi2_contingency(contigency_NY)
p
# p-value is 0.63 greater than 0.05 do not reject H0














# filter data for Houston:
H_df = mod_test[mod_test.city_and_state == "Houston, Texas"]

H_df['score_cat'] = 'high'
H_df.loc[H_df['Subjectivity'] < 0.5, 'score_cat'] = 'low'

H_df['date'] = pd.to_datetime(H_df['date'], errors='coerce')
H_df['year'] = '2020'
H_df.loc[H_df['date'].dt.year == 2021, 'year'] = '2021'

# Create a table to show the frequency of score rate in different year in Houston:
contigency_H = pd.crosstab(H_df['year'], H_df['score_cat'])
contigency_H

# Chi-square test of independence:
c, p, dof, expected = chi2_contingency(contigency_H)
p
# p-value is 0.08 greater than 0.05 do not reject H0 (closest to 0.05)











# filter data for Chicago:
C_df = mod_test[mod_test.city_and_state == "Chicago, Illinois"]

C_df['score_cat'] = 'high'
C_df.loc[C_df['Subjectivity'] < 0.5, 'score_cat'] = 'low'

C_df['date'] = pd.to_datetime(C_df['date'], errors='coerce')
C_df['year'] = '2020'
C_df.loc[C_df['date'].dt.year == 2021, 'year'] = '2021'

# Create a table to show the frequency of score rate in different year in Chicago
contigency_C = pd.crosstab(C_df['year'], C_df['score_cat'])
contigency_C

# Chi-square test of independence:
c, p, dof, expected = chi2_contingency(contigency_C)
p
# p-value is 0.39 greater than 0.05 do not reject H0







# same time diff location:
# filter by year:
mod_test['date'] = pd.to_datetime(mod_test['date'], errors='coerce')
mod_test['year'] = '2020'
mod_test.loc[mod_test['date'].dt.year == 2021, 'year'] = '2021'

# 2020 data:
df_20 = mod_test[mod_test['year'] == '2020']
# filter the 4 location we are focusing:
df_20 = df_20[df_20.city_and_state.isin(["Houston, Texas","Chicago, Illinois","New York, New York","Los Angeles, California"])]
    
    
df_20['score_cat'] = 'high'
df_20.loc[df_20['Subjectivity'] < 0.5, 'score_cat'] = 'low'
contigency_20 = pd.crosstab(df_20['city_and_state'], df_20['score_cat'])
contigency_20

# Chi-square test of independence:
c, p, dof, expected = chi2_contingency(contigency_20)
p
# p-value is 0.49 greater than 0.05 do not reject H0




# 2021 data:
df_21 = mod_test[mod_test['year'] == '2021']
# filter the 4 location we are focusing:
df_21 = df_21[df_21.city_and_state.isin(["Houston, Texas","Chicago, Illinois","New York, New York","Los Angeles, California"])]
    
    
df_21['score_cat'] = 'high'
df_21.loc[df_21['Subjectivity'] < 0.5, 'score_cat'] = 'low'
contigency_21 = pd.crosstab(df_21['city_and_state'], df_21['score_cat'])
contigency_21

# Chi-square test of independence:
c, p, dof, expected = chi2_contingency(contigency_21)
p
# p-value is 0.09 greater than 0.05 do not reject H0 (higher than 2020 but still not reject)






















