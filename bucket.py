# -*- coding: utf-8 -*-
"""
Created on Sun May 10 21:19:14 2020

@author: rakshith
"""
import re
import pymongo
from pymongo import MongoClient
import pandas as pd
from pprint import pprint
import numpy as np


cluster = MongoClient("mongodb+srv://rakshith:rakshith1234@cluster0-crxst.mongodb.net/test?retryWrites=true&w=majority")
db = cluster["tweetsClean"]
collection = db["ass2"]


def insertionSort(b): 
    for i in range(1, len(b)): 
        up = b[i] 
        j = i - 1
        while j >=0 and b[j] > up:  
            b[j + 1] = b[j] 
            j -= 1
        b[j + 1] = up      
    return b      
              
def bucketSort(x): 
    arr = [] 
    slot_num = 10 # 10 means 10 slots, each 
                  # slot's size is 0.1 
    for i in range(slot_num): 
        arr.append([]) 
          
    # Put array elements in different buckets  
    for j in x: 
        index_b = int(slot_num * j)  
        arr[index_b].append(j) 
      
    # Sort individual buckets  
    for i in range(slot_num): 
        arr[i] = insertionSort(arr[i]) 
          
    # concatenate the result 
    k = 0
    for i in range(slot_num): 
        for j in range(len(arr[i])): 
            x[k] = arr[i][j] 
            k += 1
    return x 

df.to_csv(r'/Users/rakshith/Assignment 2/firsttask/3btask.csv', encoding='utf-8', index=False)