#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'factorial' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER n as parameter.
#
#f = 0
def factorial(n):
    # Write your code here+
    
    if n-1 <= 0:                        # n-1 <= 0 then returns 1 as it is the end of the recursion : 3*2*1*1
        return 1
    else:
        result = n * factorial(n-1)
        return result

n = int(input().strip())
result = factorial(n)
print(result)
