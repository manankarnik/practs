shingles <- function() {
  n <- readline(prompt="Enter value of k: ")
  k <- as.integer(n)
  text <- readLines("~/college/amt/shingling.txt")
  shingle <- vector(mode="character", length=nchar(text) - k)
  
  i = 0
  while (i < nchar(text) - k) {
    shingle[i] <- substr(text, start=i, stop=i+k)
    print(shingle[i])
    i = i + 1
  }
}
shingles()