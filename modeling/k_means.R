# Import libraries
library(caret)
library("cluster")
library("factoextra")
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

# Sample 10,000 tweets since there are too many to run K-means clustering
set.seed(12)
sample_ind <- sample(proper_mask_ind, 10000, replace = FALSE)
sample_df <- df[sample_ind, ]

# Get polarity and mask mandates
col_ind <- c(38, 35)

# Normalize data
library(caret)
normalized <- scale(sample_df[ , col_ind])

# Run K-means with 3 clusters
km <- kmeans(normalized, centers = 3, nstart = 25)

## Visualize results for K-means
fviz_cluster(km, data = sample_df[, col_ind],
             geom = "point",
             ellipse.type = "convex", 
             ggtheme = theme_bw())
