
import math
import os
import random
import re
import sys



def plusMinus(arr):
    pos = 0
    neg = 0
    zer = 0
    
    for i in arr:
        if i > 0:
            pos += 1
        elif i == 0:
            zer += 1
        else:
            neg += 1
    
    pos_ratio = round( pos/len(arr), 6)
    neg_ratio = round( neg/len(arr), 6)
    zer_ratio = round( zer/len(arr), 6)
    print(pos_ratio)
    print(neg_ratio)
    print(zer_ratio)

if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    plusMinus(arr)
