# -*- coding: utf-8 -*-
"""
Created on Sun Oct 18 18:39:22 2020

@author: Rohan Prateek
"""
def lucky_count(b):
    kick_list = list()
    start_list=list()
    start = 0
    i = 0
    count = 0
    while (i != -1):
        i = b.find('KICK',start)
        if i == -1:
            break
        kick_list.append(i)
        start = i+3
    start = 0
    i=0
    while (i != -1):
        i = b.find('START',start)
        if i == -1:
            break
        start_list.append(i)
        start=i+4
    for i in kick_list:
        for j in start_list:
            if i<j:
                count = count+1
    return count
    
    
input_list = list()
input_string=''

n=int(input())
for t in range(0,n):
    input_string = str(input())
    input_list.append(input_string)    

for q in range(0,n):
    y=lucky_count(input_list[q])
    print('Case #',q,': ',y)
    

    
    
