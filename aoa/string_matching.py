def naive_search(text, pattern):
    for i in range(len(text) - len(pattern) + 1):
        if text[i: i + len(pattern)] == pattern:
            print(f"Pattern found at index {i}")


def rabin_karp(text, pattern):
    d, q, m, n = 256, 101, len(pattern), len(text)
    p, t, h = 0, 0, pow(d, m-1) % q

    for i in range(m):
        p = (d * p + ord(pattern[i])) % q
        t = (d * t + ord(text[i])) % q

    for i in range(n - m + 1):
        if p == t and text[i:i+m] == pattern:
            print(f"Pattern found at index {i}")
        if i < n - m:
            t = (d * (t - ord(text[i]) * h) + ord(text[i+m])) % q


def kmp(text, pattern):
    m, n = len(pattern), len(text)
    lps = [0] * m
    
    j = 0
    for i in range(1, m):
        while j > 0 and pattern[i] != pattern[j]:
            j = lps[j - 1]
        if pattern[i] == pattern[j]:
            j += 1
            lps[i] = j

    j = 0
    for i in range(n):
        while j > 0 and text[i] != pattern[j]:
            j = lps[j - 1]
        if text[i] == pattern[j]:
            j += 1
        if j == m:
            print(f"Pattern found at index {i-m+1}")
            j = lps[j - 1]


def boyer_moore(text, pattern):
    m, n = len(pattern), len(text)
    last = {c: -1 for c in set(pattern)}

    for i in range(m):
        last[pattern[i]] = i

    s = 0
    while s <= n - m:
        j = m - 1
        while j >= 0 and pattern[j] == text[s+j]:
            j -= 1
        if j < 0:
            print(f"Pattern found at index {s}")
            s += (s + m < n) and (m - last.get(text[s+m], -1) or 1) or 1
        else: s += max(1, j - last.get(text[s+j], -1))

            


            
text = "Hello world world world"
pattern = "world"
boyer_moore(text, pattern)
