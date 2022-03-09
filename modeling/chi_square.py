import pandas as pd
import numpy as np
from scipy.stats import chi2_contingency



# Chi-square test if Mask mandate and sentiment(polarity_classif2) are significant

# read the data "complete_data_sentiment":
df = pd.read_csv("C:/ucla/m148/SM148_project/complete_data/complete_data_sentiment.csv")
pd.set_option('display.max_columns', None) # <- to display all the columes

df.head()
# create a contigency(frequency) table for chi-square test
contigency = pd.crosstab(df['Face_Masks_Required_in_Public'], df['polarity_classif2'])
# display the contigency table
contigency

# Apply Chi-square test:
c, p, dof, expected = chi2_contingency(contigency)
print("The p-value for Chi-square test is:", p)
# p-value in this case is 8.07234507356557e-05, we reject the null hypothesis; 
# there is a relationship between mask mandates and sentiment in the U.S.



# (optional test)

# trying for data in CA:
CA = df[df['CA'] =="Yes"]
CA.head()
# if Face_Masks_Required_in_Public and mentions_mask together would affect polarity significantlly in CA
contigency = pd.crosstab(CA['Face_Masks_Required_in_Public'], CA['polarity_classif2'])
contigency

# Chi-square:
c, p, dof, expected = chi2_contingency(contigency)
p
# p-value in this case is 0.1846491084529554, we do not reject null hypothesis; there is no
# significant relationship between mask mandates and sentiment in CA.



# trying data in LA:
LA = df[df.city_and_state =="Los Angeles, California"]
LA.head()
contigency = pd.crosstab(LA['Face_Masks_Required_in_Public'], LA['polarity_classif2'])
contigency
# Chi-square:
c, p, dof, expected = chi2_contingency(contigency)
p
# p-value in this case is 0.8776033668473593, we do not reject null hypothesis; 
# there is no relationship between mask mandates and sentiment in LA.






















