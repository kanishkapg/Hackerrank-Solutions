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
    arr = list(s)
    if(arr[-2] == 'A'):
        if(int(''.join([arr[0], arr[1]])) == 12):
            arr[0] = '0'
            arr[1] = '0'
            time_new = ''.join(arr[:-2])
        else:
            time_new = ''.join(arr[:-2])
    elif(arr[-2] == 'P'):
        time_hr = int(''.join([arr[0], arr[1]]))
        if(time_hr != 12):
            time_hr = int(''.join([arr[0], arr[1]])) + 12
            temp_l2 = list(str(time_hr))
            arr[0] = temp_l2[0]
            arr[1] = temp_l2[1]
            time_new = ''.join(arr[:-2])
        else:
            time_new = ''.join(arr[:-2])
    return (time_new)
        
    
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = timeConversion(s)

    fptr.write(result + '\n')

    fptr.close()
