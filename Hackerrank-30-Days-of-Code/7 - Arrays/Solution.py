#!/bin/python3

import math
import os
import random
import re
import sys

def reverse_array(arr):
    for i in range(len(arr)):                           # range(len(arr), -1, -1) would be the reverse array traverse. # Till -1 cause exclusive = till 0
        print(arr[len(arr) - 1 - i], end= " ")


if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))
    
    reverse_array(arr)
