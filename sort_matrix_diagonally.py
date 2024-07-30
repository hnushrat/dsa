'''

A matrix diagonal is a diagonal line of cells starting from some cell in either the topmost row or leftmost column
and going in the bottom-right direction until reaching the matrix's end.

For example, the matrix diagonal starting from mat[2][0], where mat is a 6 x 3 matrix, includes cells mat[2][0], mat[3][1], and mat[4][2].

Given an m x n matrix mat of integers, sort each matrix diagonal in ascending order and return the resulting matrix.

'''

import numpy as np

import random

seed = 42
random.seed(seed)
np.random.seed(seed)

rows, cols = 5,5
lower_range = 1
upper_range = 9

mat = np.random.randint(lower_range, upper_range + 1, size = (rows, cols))

print(f'Original Matrix:\n\n{mat}')

# Store the values for the difference of indices
maps = {}
for i in range(rows):
    for j in range(cols):
        if maps.get(i-j):
            maps[i - j].append(mat[i, j])
        else:
            maps[i - j] = [mat[i, j]]

# now sort these lists inside these maps
for i in maps:
    maps[i] = sorted(maps[i]) # ascending order sort

# print(maps)

# now push these sorted maps to the matrix from the bottom right end, for reducing time complexity by not filling from the front and switching pointer

for i in range(rows - 1, -1, -1):
    for j in range(cols - 1, -1, -1):
        mat[i, j] = maps[i - j][-1] # fill with the last element
        maps[i - j].pop() # after filling remove this element

print(f"\n\nUpdated Matrix:\n\n{mat}")