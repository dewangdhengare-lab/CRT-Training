#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'diagonalDifference' function below.
#
# The function is expected to return an INTEGER.
# The function accepts 2D_INTEGER_ARRAY arr as parameter.
#

def diagonalDifference(arr):
    n = len(arr)
    left_right = 0
    right_left = 0
    for i in range(n):
                left_right = arr[i][i] + left_right
                right_left = right_left +arr[i][n-1-i]
    return abs(left_right-right_left)

if __name__ == '__main__':

    n = int(input().strip())

    arr = []

    for _ in range(n):
        arr.append(list(map(int, input().rstrip().split())))

    print(result = diagonalDifference(arr))
