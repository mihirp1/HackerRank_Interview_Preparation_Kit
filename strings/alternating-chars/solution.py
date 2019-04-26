#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the alternatingCharacters function below.
def alternatingCharacters(s):
    list_reject = []
    for iter1,let in enumerate(s):
        if(iter1 < len(s) - 1):
           if(s[iter1] == s[iter1+1]):
             list_reject.append(iter1+1)
             #s[iter1+1] = 'C'
    return len(list_reject)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input())

    for q_itr in range(q):
        s = input()

        result = alternatingCharacters(s)

        fptr.write(str(result) + '\n')

    fptr.close()

