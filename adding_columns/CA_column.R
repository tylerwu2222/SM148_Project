df <- read.csv('merged_data_with_sentiment.csv')
# install.packages('vscDebugger')
library(stringr)
head(df)
la_ind <- character(nrow(df))
ca_ind <- character(nrow(df))
for (i in 1:nrow(df)) {
  if (str_detect(df[i, 2], 'Los Angeles')) {
    la_ind[i] <- 'Yes'
    ca_ind[i] <- 'Yes'
  } else if (str_detect(df[i, 2], 'CAMPO') | str_detect(df[i, 2], 'AMERICA') | str_detect(df[i, 2], 'CAMBRIDGE')){
    la_ind[i] <- 'No'
    ca_ind[i] <- 'No'
  } else if (str_detect(df[i, 2], 'CA') | str_detect(df[i, 2], 'California')) {
    la_ind[i] <- 'No'
    ca_ind[i] <- 'Yes'
  } else {
    la_ind[i] <- 'No'
    ca_ind[i] <- 'No'
  }
}

df['CA'] <- ca_ind
df['LA'] <- la_ind

write.csv(df, './merged_data_with_sentiment_and_CA_LA.csv', row.names = FALSE)


