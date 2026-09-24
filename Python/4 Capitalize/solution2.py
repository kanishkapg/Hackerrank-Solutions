import math
import os
import random
import re
import sys

# Complete the solve function below.
def solve(s):
    words = s.split(' ')
    new_list = []
    for word in words:
        if word and word[0].isalpha():
            word = str(word[0].upper()) + str(word[1:])
            new_list.append(word)
        else:
            new_list.append(word)
    name = " ".join(new_list)
    return  name

            

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    s = input()
    result = solve(s)
    fptr.write(result + '\n')
    fptr.close()
