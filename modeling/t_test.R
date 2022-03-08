# Read in data
df <- read.csv('complete_data_sentiment.csv')

# Index where mask mandate's are enforced
mask_ind_yes <- which(df$Face_Masks_Required_in_Public == 'Yes')

x <- df[mask_ind_yes, "polarity_compound"]
y <- df[-mask_ind_yes, "polarity_compound"]

# T-test between the polarity [-1, 1] and whether there is a mask mandate or not
t.test(x, y)

# Gives a p-value of 4.271e-13 -> significant difference between means



