#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'timeConversion' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING s as parameter.
#

def timeConversion(s):
    # Write your code here
     
    if s[-2:] == 'AM':                              # for AM 

        if s[:2] == '12':                           # if 12 AM --> 00:x:x
            print('00',s[2:-2], sep='')
        else:
            print(s[:-2])

    elif s[-2:] == 'PM':                            # for PM
        
        if s[:2] == '12':                           # if 12 PM --> 12:x:x       
            print(s[:-2])
        else:
            hour = 12 + int(s[:2])                  # if 1-11 PM --> (12+ 1-11):x:x
            print(hour, s[2:-2], sep='')
            

if __name__ == '__main__':

    s = input()
    
    timeConversion(s)
