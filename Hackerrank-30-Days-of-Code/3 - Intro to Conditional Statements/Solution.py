#!/bin/python3

import math
import os
import random
import re
import sys

if __name__ == '__main__':
    N = int(input().strip())
       
def even_odd(x):       
    if (x % 2) == 0:
        if 2 <= x <= 5:
            print("Not Weird")
        elif 6 <= x <= 20:
            print("Weird")
        elif x > 20:
            print("Not Weird")                  
    else :
        print("Weird")

even_odd(N)
