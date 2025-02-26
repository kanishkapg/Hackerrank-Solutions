#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the solve function below.
def solve(s):
    splitted_str = s.split(" ")
    capitalized_str = [word.capitalize() for word in splitted_str]
    rejoined_str = " ".join(capitalized_str)
    return rejoined_str
"""
instead of upper() function, capitalize() function can be used to capitalize 
the first letter of each word in a string.
strings in python are immutable, which means that they cannot be changed. 
So, we cannot change the string in place.
"""
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = solve(s)

    fptr.write(result + '\n')

    fptr.close()