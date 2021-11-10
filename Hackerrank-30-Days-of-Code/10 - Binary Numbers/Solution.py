#!/bin/python3

import math
import os
import random
import re
import sys



if __name__ == '__main__':
    n = int(input().strip())
    b_str = bin(n)[2:]
    b_lst = b_str.split('0')
    lst= []
    
    for element in b_lst:
        lst.append(len(element))

    print(max(lst))
