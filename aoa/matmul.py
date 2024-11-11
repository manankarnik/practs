from timeit import timeit
from typing import List
from itertools import chain

def matrix_multiply(m1: List[List[int]], m2: List[List[int]]) -> List[List[int]] | None:
    if len(m1) != len(m2[0]): return None
    result = [[0 for _ in range(len(m1))] for _ in range(len(m1))]

    for i in range(len(m1)):
        for j in range(len(m1)):
            for k in range(len(m2)):
                result[i][j] += m1[i][k] * m2[k][j]
    return result


def strassen_multiply(m1: List[List[int]], m2: List[List[int]]) -> List[List[int]] | None:
    a, b, c, d = chain.from_iterable(m1)
    e, f, g, h = chain.from_iterable(m2)

    p1 = a * (f - h)
    p2 = (a + b) * h
    p3 = (c + d) * e
    p4 = d * (g - e)
    p5 = (a + d) * (e + h)
    p6 = (a - c) * (g + h)
    p7 = (b - d) * (e + f)

    return [[p5 + p4 -p2 + p6, p1 + p2], [p3 + p4, p1 + p5 - p3 - p7]]

m1 = [[1, 2], [3, 4]]
m2 = [[1, 2], [3, 4]]
print(matrix_multiply(m1, m2))
print(strassen_multiply(m1, m2))

mat_time = timeit(lambda: matrix_multiply(m1, m2), number=100000)
str_time = timeit(lambda: strassen_multiply(m1, m2), number=100000)
print(mat_time)
print(str_time)

