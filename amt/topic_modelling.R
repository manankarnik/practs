install.packages("tm")
install.packages("topicmodels")
install.packages("stopwords")
library("tm")
library("topicmodels")
library("stopwords")

setwd("~/college/amt/british-fiction-corpus")
filenames <- list.files(path="~/college/amt/british-fiction-corpus")
filenames

filetext <- lapply(filenames, readLines)

corpus <- Corpus(VectorSource(filetext))
corpus <- tm_map(corpus, tolower)
corpus <- tm_map(corpus, removePunctuation)
corpus <- tm_map(corpus, removeNumbers)
corpus <- tm_map(corpus, removeWords, stopwords())

dtm <- DocumentTermMatrix(corpus)
dtm

k <- 5
lda <- LDA(dtm, k, method="VEM")
terms(lda, 5)
topics(lda)