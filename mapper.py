# -*- coding: utf-8 -*-
"""
Created on Sat May  9 13:24:56 2020

@author: rakshith
"""
import sys
 
#--- get all lines from stdin ---
for line in sys.stdin:
    #--- remove leading and trailing whitespace---
    line = line.strip()

    #--- split the line into words ---
    words = line.split()

    #--- output tuples [word, 1] in tab-delimited format---
    for word in words: 
        print ('%s\t%s' % (word, "1"))

#!/usr/bin/env python
import sys
 
# maps words to their counts
word2count = {}
 
# input comes from STDIN
for line in sys.stdin:
    # remove leading and trailing whitespace
    line = line.strip()
 
    # parse the input we got from mapper.py
    word, count = line.split('\t', 1)
    # convert count (currently a string) to int
    try:
        count = int(count)
    except ValueError:
        continue

    try:
        word2count[word] = word2count[word]+count
    except:
        word2count[word] = count
 
# write the tuples to stdout
# Note: they are unsorted
for word in word2count.keys():
    print % ( word, word2count[word] )
