#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the activityNotifications function below.
def getMed(TRAIL,d):
     count_dict = {}
     #count_dict = Counter()
     #TRAIL = sorted(TRAIL)
     

     if(d%2!=0):
       med = TRAIL[d//2]
     else:
       med = float( (TRAIL[int(d/2)] + TRAIL[int(d/2) - 1] )/2)
       #print(int(d/2),int(d/2 - 1))
     return med


def activityNotifications(expenditure,n, d):

    length = len(expenditure)
    trail = []
    spend = []
    #trail = expenditure[:d]
    #spend = (expenditure[d:])
    med = 0
    iter1 = 0
    value = 0
    day_spend = 0
    spend_counter = 0
    TRAIL = []
    
    for iter1 in range(n) :
        if(iter1 < d ):
            #trail = TRAIL
            #med = getMed(trail)  
            #if(expenditure[iter1] == 2 * med or expenditure[iter1] > 2 * med):
            #spend_counter+=1
            pass
        if(iter1 >=d):
            trail = expenditure[iter1-d:iter1]
            #trail = sorted(trail)
            med = getMed(trail,d)  
            #print(trail,med)
            #print(expenditure[iter1])
            if (expenditure[iter1] >= (2*med)):
                spend_counter+=1
             
    
    #print("Spend_counter : ",spend_counter)
    return (spend_counter)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nd = input().split()

    n = int(nd[0])

    d = int(nd[1])

    expenditure = list(map(int, input().rstrip().split()))

    result = activityNotifications(expenditure,n,d)
    #print("Spend_counter : ",result)

    fptr.write(str(result) + '\n')

    fptr.close()

