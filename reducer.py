# -*- coding: utf-8 -*-
"""
Created on Sun May 10 16:22:26 2020

@author: rakshith
"""

#!/usr/bin/python
import sys
import os
wordcount = {}

# Get input from stdin
for line in sys.stdin:

    line = line.strip()

    # parse the input from mapper.py
    word, count = line.split('\t', 1)
    # convert count (currently a string) to int
    try:
        count = int(count)
    except ValueError:
        continue

    try:
        wordcount[word] = wordcount[word] + count
    except:
        wordcount[word] = count

# Write the tuples to stdout
# Currently tuples are unsorted
for word in wordcount.keys():
    print '%s\t%s' % (word, wordcount[word])