# Import libraries
library(caret)
library("cluster")
library("factoextra")
library(dplyr)
library(ggplot2)

# Read in data
df <- read.csv('complete_data_sentiment.csv')

# Encode mask_mandate to numeric
new_mask <- numeric(nrow(df))
for (i in 1:nrow(df)){
  if (df$Face_Masks_Required_in_Public[i] == 'Yes'){
    new_mask[i] <- 1
  } else if (df$Face_Masks_Required_in_Public[i] == 'No'){
    new_mask[i] <- 0
  } else {
    new_mask[i] <- -1
  }
}

# Make it a new column
df$new_mask <- new_mask

# Discard entries where the mask mandate is missing
proper_mask_ind <- which(df$new_mask >= 0)

# Sample 10,000 tweets since there are too many to run hierarchical clustering
set.seed(123)
sample_ind <- sample(proper_mask_ind, 10000, replace = FALSE)
sample_df <- df[sample_ind, ]

# Get polarity compound and Mask Mandate
col_ind <- c(35, 38)

# Normalize data
normalized <- scale(sample_df[ , col_ind])

# Compute euclidean distance between normalized data
d <- dist(normalized, method = "euclidean")

# Use average linkage
hc <- hclust(d, method = "average")

# Graph dendogram
plot(hc, cex = 0.6)
rect.hclust(hc, k = 4, border = 1:4)

# Plot Face Masks vs Polarity coloring each data point by cluster
cut_avg <- cutree(hc, k = 4)
new_df <- mutate(sample_df, cluster = cut_avg)
ggplot(new_df, aes(x = Face_Masks_Required_in_Public, y = polarity_compound, color = factor(cluster))) + 
  geom_point() +
  labs(x = 'Face Masks Required', y = 'Polarity', title = 'Polarity vs. Face Masks Required Grouped by Cluster')
