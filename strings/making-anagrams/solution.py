#!/bin/python3

import math
import os
import random
import re
import sys
from collections import Counter

# Complete the makeAnagram function below.
def getSum(temp):
    sum1 = 0
    for key,value in temp.items():
        sum1 += temp[key]
    return sum1 


def makeAnagram(a, b):
    c_a = Counter(a)
    c_b = Counter(b)
    a1 = set(a)
    a2 = set(b)
    print(Counter(a))
    print(Counter(b))
    print(Counter(a) - Counter(b))
    print("a - b :")
    print(Counter(a) - Counter(b))
    print(" b - a : ")
    print(Counter(b) - Counter(a))
    #one = Counter(a) - diff
    #two = Counter(b)- diff
    #print(one)
    #print(two)
    return (getSum(Counter(a) - Counter(b)) + getSum(Counter(b) - Counter(a)))

    #return(Counter(a) - Counter(b))

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    a = input()

    b = input()

    res = makeAnagram(a, b)

    fptr.write(str(res) + '\n')

    fptr.close()

