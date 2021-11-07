#!/bin/python3

import math
import os
import random
import re
import sys

if __name__ == '__main__':
    n = int(input().strip())

def multiples(x):
    for i in range(1, 11, 1):        #here 1 is inclusive, 11 exclusive so 1-10
        print(x,'x', i, '=', x * i)

multiples(n)
