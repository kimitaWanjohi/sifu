'''
54. Spiral Matrix
Given an m x n matrix, return all elements of the matrix in spiral order.
https://leetcode.com/problems/spiral-matrix/
'''


def spiralOrder(matrix):
    res = []

    if not len(matrix):
        return res

    while matrix:
        # first row
        res += matrix.pop(0)
        # res.extend(matrix.pop(0))

        # last column
        if matrix and matrix[0]:
            for row in matrix:
                res.append(row.pop())
        # last row
        if matrix:
            res += matrix.pop()[::-1]
            # res.extend(reversed(matrix[-1]))

        # first column
        if matrix and matrix[0]:
            for row in matrix[::-1]:
                # for row in reversed(matrix):
                res.append(row.pop(0))

    return res


b = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

c = [
    [1,  2,  3,   4],
    [5,  6,  7,   8],
    [9,  10, 11, 12],
    [13, 14, 15, 16]
]
assert spiralOrder([[1]]) == [1]
assert spiralOrder([[7], [9], [6]]) == [[7], [9], [6]]
assert spiralOrder(b) == [1, 2, 3, 6, 9, 8, 7, 4, 5]
assert spiralOrder(c) == [
    1, 2, 3, 4, 8, 12, 16,
    15, 14, 13, 9, 5, 6, 7, 11, 10
]


def spiralOrderIter(matrix):
    res = []

    if not matrix:
        return res

    top, down = 0, len(matrix)-1
    left, right = 0, len(matrix[0])-1

    while (top <= down and left <= right):
        for i in range(left, right+1):
            res.append(matrix[top][i])
        top += 1

        for i in range(top, down+1):
            res.append(matrix[i][right])
        right -= 1

        if (top <= down):
            for i in range(right, left-1, -1):
                res.append(matrix[down][i])
            down -= 1

        if (left <= right):
            for i in range(down, top-1, -1):
                res.append(matrix[i][left])
            left += 1

    return res


def spiralOrder2(matrix):
    res = []

    if not matrix:
        return res

    top, down = 0, len(matrix) - 1
    left, right = 0, len(matrix[0]) - 1

    while (top <= down and left <= right):
        # first row
        res.extend(matrix[top][left:right+1])
        top += 1

        # last column
        for i in range(top, down+1):
            res.append(matrix[i][right])
        right -= 1

        # last row
        if (top <= down):
            last_row = matrix[down][left:right+1]
            res.extend(last_row[::-1])
            down -= 1

        # first column
        if (left <= right):
            for i in range(down, top-1, -1):
                res.append(matrix[i][left])
            left += 1

    return res
