df <- read.csv('merged_data_with_sentiment.csv')

length(which(df$location == 'Los Angeles, CA'))

library(stringr)

ca_ind <- numeric(0)
for (i in 1:nrow(df)) {
  if (str_detect(df[i, 2], 'CA')) {
    ca_ind <- c(ca_ind, i)
  }
}

