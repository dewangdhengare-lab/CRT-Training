#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'insertionSort1' function below.
#
# The function accepts following parameters:
#  1. INTEGER n
#  2. INTEGER_ARRAY arr
#

# def insertionSort1(n, arr):
#     key=arr[-1]
#     i=len(arr)-2
#     while i>=0 and arr[i]>key:
#         arr[i+1]=arr[i]
#         print(*arr)
#         i-=1
#     arr[i+1]=key
#     print(*arr)


  
    key=arr[i]
    i=len(arr)-2
    pos=i
    while pos>=0 and arr[pos]>key:
        arr[pos+1]=arr[pos]
        print(*arr)
        pos-=1

if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    insertionSort2(n, arr)
