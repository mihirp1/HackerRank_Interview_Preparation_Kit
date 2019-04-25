#!/bin/python3

import math
import os
import random
import re
import sys



# Complete the stepPerms function below.
def stepPerms(n):
    #dict exist

    if(n==1):
        #sum1 = 0
        exist[1] = 1
        return 1
    if(n == 2):
        exist[2] = 2
        return 2
    if(n==3):
        exist[3] = 4
        return 4

    if(n > 3):
        if n not in exist.keys():
           exist[n] = (stepPerms(n-1) + stepPerms(n-2) + stepPerms(n-3))
           return exist[n]

        if n in exist.keys():   
           return exist[n]

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = int(input())
    #global sum1
    exist = {}
#
    for s_itr in range(s):
        n = int(input())

        res = stepPerms(n)

        fptr.write(str(res) + '\n')

    fptr.close()

