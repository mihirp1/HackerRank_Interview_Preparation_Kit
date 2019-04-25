#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the countSwaps function below.
def countSwaps(a):
    length = len(a)
    swaps = 0
    sorted_array = []
    flag = 0
    iter2 = 0

    if(sorted(a) == a):
        flag = 1;
  
    for iter2 in range(0,length - 1):
     for iter1,value in enumerate(a):
        #print("For",a[iter1])
        if(iter1 < length - 1 and flag == 0):
          if(a[iter1] > a[iter1 + 1]):
            temp = a[iter1]
            a[iter1] = a[iter1+1]
            a[iter1+1] = temp
            #print("Each swap : ")
            #print(a)
            swaps += 1
     #print(a)
    print("Array is sorted in",swaps,"swaps.")
    #print(a)
    print("First Element:",a[0])
    print("Last Element:",a[length-1])
    #print(a[0]) 


if __name__ == '__main__':
    n = int(input())

    a = list(map(int, input().rstrip().split()))

    countSwaps(a)

