
def rod_cutting(prices):
    n = len(prices)
    matrix = [[0] * (n + 1) for _ in range(n + 1)]
    s = [0] * (n + 1)


    for i in range(1, n + 1):
        for j in range(1, n + 1):
            if i == 1:
                matrix[i][j] = j * prices[i - 1]
                s[j] = 1
            elif i > j: matrix[i][j] = matrix[i - 1][j]
            elif prices[i - 1] + matrix[i][j - i] > matrix[i - 1][j]:
                matrix[i][j] = prices[i - 1] + matrix[i][j - i]
                s[j] = i
            else: 
                matrix[i][j] = matrix[i - 1][j]

    pieces = []
    length = n
    while length > 0:
        pieces.append(s[length])
        length -= s[length]

    return matrix, pieces

prices = [1, 5, 8, 9, 10, 17, 17, 22]
matrix, pieces = rod_cutting(prices)

for row in matrix:
    for item in row:
        print(item, end="\t")
    print()

print("\nPieces:", pieces)
