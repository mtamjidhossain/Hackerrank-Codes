#!/bin/python3

import math
import os
import random
import re
import sys

def reverse_array(arr):
    for i in range(len(arr)):
        print(arr[len(arr) - 1 - i], end= " ")


if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))
    
    reverse_array(arr)
