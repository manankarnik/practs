install.packages("tm")
install.packages("topicmodels")
install.packages("stopwords")
library("tm")
library("topicmodels")
library("stopwords")

filenames <- list.files(path="~/college/amt/british-fiction-corpus")
filenames
filetext <- lapply(filenames, readLines)

mycorpus <- Corpus(VectorSource(filetext))
mycorpus <- tm_map(mycorpus, tolower)
mycorpus <- tm_map(mycorpus, removeNumbers)
mycorpus <- tm_map(mycorpus, removePunctuation)
mycorpus <- tm_map(mycorpus, removeWords, stopwords())

dtm <- DocumentTermMatrix(mycorpus)
dtm

k <- 3
lda <- LDA(dtm, k, method="VEM")
terms(lda, 5)
topics(lda)
