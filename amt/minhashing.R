install.packages("textreuse")
library(textreuse)

minhash <- minhash_generator(n=240, seed=1111)

dir <- system.file("extdata/ats", package="textreuse")
corpus <- TextReuseCorpus(dir=dir, tokenizer=tokenize_ngrams, n=5, keep_tokens=TRUE, minhash_func=minhash)

head(minhashes(corpus[[1]]))
length(minhashes(corpus[[1]]))

lsh_threshold(h=200, b=50)
lsh_threshold(h=240, b=80)
lsh_probability(h=240, b=80, s=0.25)
lsh_probability(h=240, b=80, s=0.75)

buckets <- lsh(corpus, bands=80)
buckets

baxter_matches <- lsh_query(buckets, "calltounconv00baxt")
baxter_matches

candidates <- lsh_candidates(buckets)
candidates