
def lcs(a, b):
    m = len(a)
    n = len(b)
    M = [[0] * (n+1) for _ in range(m+1)]

    for i in range(1, m+1):
        for j in range(1, n+1):
            if a[i-1] == b[j-1]: M[i][j] = M[i-1][j-1] + 1
            else: M[i][j] = max(M[i-1][j], M[i][j-1])

    idx = M[m][n]
    subseq = [""] * idx
    i = m
    j = n
    while i > 0 and j > 0:
        if a[i-1] == b[j-1]:
            subseq[idx-1] = a[i-1]
            i -= 1
            j -= 1
            idx -= 1
        elif M[i-1][j] > M[i][j-1]: i -= 1
        else: j -= 1

    return M, "".join(subseq)


a = "GTAATCTAAC"
b = "GATTACA"
print(f"String 1: {a}")
print(f"String 2: {b}")
M, subseq = lcs(a, b)

for row in M:
    for item in row:
        print(item, end="\t")
    print()

print("\nSubsequence:", "".join(subseq))
