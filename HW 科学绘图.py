#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Oct  1 20:00:46 2018

@author: davidxiong
"""
import time
import random
import matplotlib.pyplot as plt
import numpy as np



def listt(x):
    listtt = []
    while x>0:
        listtt.append(random.randint(0,100000))
        x-=1
    return listtt

# selection sort

start = time.clock()

def selectionsort(x):
    a = []
    while len(x)!=0:
        minn = x[0]
        for i in range(len(x)):
            if x[i]<minn:
                minn = x[i]
        a.append(minn)
        x.remove(minn)
    return a



import time

def record_selectiona(x):
    running_time = []
    length_of_step = []
    for i in range(0,x,2000):
        start = time.clock()
        selectionsort(listt(i))
        timee = (time.clock()-start)
        length_of_step.append(i)
        running_time.append(timee)
    return running_time

def record_selectionb(x):
    running_time = []
    length_of_step = []
    for i in range(0,x,2000):
        start = time.clock()
        selectionsort(listt(i))
        timee = (time.clock()-start)
        length_of_step.append(i)
        running_time.append(timee)
    return length_of_step







def merge(left,right):
    result = []
    i,j=0,0
    while i<len(left) and j<len(right):
        if left[i]<right[j]:
            result.append(left[i])
            i+=1
        else:
            result.append(right[j])
            j+=1
    while i<len(left):
        result.append(left[i])
        i+=1
    while j<len(right):
        result.append(right[j])
        j+=1
    return result

def merge_sort(L):
    if len(L)<2:
        return L[:]
    else:
        mid = int(len(L)/2)
        left = merge_sort(L[:mid])
        right = merge_sort(L[mid:])
        return merge(left,right)


def record_mergea(x):
    running_time = []
    length_of_step = []
    for i in range(0,x,2000):
        start = time.clock()
        merge_sort(listt(i))
        timee = (time.clock()-start)
        length_of_step.append(i)
        running_time.append(timee)
    return running_time

def record_mergeb(x):
    running_time = []
    length_of_step = []
    for i in range(0,x,2000):
        start = time.clock()
        merge_sort(listt(i))
        timee = (time.clock()-start)
        length_of_step.append(i)
        running_time.append(timee)
    return length_of_step




def insertionsort(A):
    for j in range(1,len(A)):
        key = A[j]
        i = j-1
        while i>=0 and A[i] > key:
            A[i+1] = A[i]
            
            i-=1
        A[i+1] = key
    return A

def record_inserta(x):
    running_time = []
    length_of_step = []
    for i in range(0,x,2000):
        start = time.clock()
        insertionsort(listt(i))
        timee = (time.clock()-start)
        length_of_step.append(i)
        running_time.append(timee)
    return running_time

def record_insertb(x):
    running_time = []
    length_of_step = []
    for i in range(0,x,2000):
        start = time.clock()
        insertionsort(listt(i))
        timee = (time.clock()-start)
        length_of_step.append(i)
        running_time.append(timee)
    return length_of_step



def bubblesort(a):
    length = len(a)
    while length>0:
        for i in range(len(a)-1):
            if a[i]>a[i+1]:
                a[i],a[i+1]=a[i+1],a[i]
                
        length-=1
    return a

def record_bubblea(x):
    running_time = []
    length_of_step = []
    for i in range(0,x,2000):
        start = time.clock()
        bubblesort(listt(i))
        timee = (time.clock()-start)
        length_of_step.append(i)
        running_time.append(timee)
    return running_time

def record_bubbleb(x):
    running_time = []
    length_of_step = []
    for i in range(0,x,2000):
        start = time.clock()
        bubblesort(listt(i))
        timee = (time.clock()-start)
        length_of_step.append(i)
        running_time.append(timee)
    return length_of_step







x = record_selectionb(5000)
y = record_selectiona(5000)
x1 = record_mergeb(5000)
y1 = record_mergea(5000)
x2 = record_insertb(5000)
y2 = record_inserta(5000)
x3 = record_bubbleb(5000)
y3 = record_bubblea(5000)




plt.plot(x, y, label='Selection Sort')
plt.plot(x1, y1, label='Merge Sort')
plt.plot(x2,y2,label='Insertion Sort')
plt.plot(x3,y3,label='Bubble Sort')
plt.ylabel('Time Taken(s)')
plt.xlabel('Number Of Step')
plt.title('Sorting Algorithm')
plt.legend()
plt.show()




        




