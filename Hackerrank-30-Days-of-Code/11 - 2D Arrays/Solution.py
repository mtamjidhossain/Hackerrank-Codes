#!/bin/python3

import math
import os
import random
import re
import sys

def max_hglass_sum(arr):
    
    hg_sums = []

    for i in range(len(arr)):
        for j in range(len(arr[i])):
          
            if j+2 >= len(arr[i]) or i+2 >= len(arr):
                break
            else:
                hg_sum = arr[i][j] + arr[i][j+1] + arr[i][j+2] + arr[i+1][j+1] + arr[i+2][j] + arr[i+2][j+1] + arr[i+2][j+2]

            hg_sums.append(hg_sum)

    return max(hg_sums)
  

if __name__ == '__main__':

    arr = []

    for _ in range(6):
        arr.append(list(map(int, input().rstrip().split())))
    
    print(max_hglass_sum(arr))
