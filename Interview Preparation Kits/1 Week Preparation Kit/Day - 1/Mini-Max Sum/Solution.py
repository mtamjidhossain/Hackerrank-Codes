#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'miniMaxSum' function below.
#
# The function accepts INTEGER_ARRAY arr as parameter.
#

def miniMaxSum(arr):
    # Write your code here

    sums = []

    for i in range(len(arr)):         # ignoring i in the iteration
        itr_sum = 0                         # sum for each iteration  
        for j in range(len(arr)):     # Iterations: j traversing from first to last element                 
            if i != j:                # if 1 != 1 then s += 2,3,4,5
                itr_sum += arr[j]
                
        sums.append(itr_sum)

    print(min(sums), max(sums))
    
if __name__ == '__main__':

    arr = list(map(int, input().rstrip().split()))

    miniMaxSum(arr)
