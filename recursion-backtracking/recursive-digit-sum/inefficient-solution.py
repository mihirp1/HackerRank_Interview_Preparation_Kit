#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the superDigit function below.
def superDigit(n, k):
    string = ''
    for i in range(k):
        if(i != "0"):
           string += str(n)

    print(string)

    if len(string) == 1:
        return (string)

    if len(string) > 1:
        num = str(string)
        num1 = 0
        for string1 in num:
            num1 += int(string1)        
        return superDigit(num1,1)
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nk = input().split()

    n = nk[0]

    k = int(nk[1])

    result = superDigit(n, k)

    fptr.write(str(result) + '\n')

    fptr.close()

