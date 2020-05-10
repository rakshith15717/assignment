# -*- coding: utf-8 -*-
"""
Created on Sun May 10 18:40:31 2020

@author: rakshith
"""

#!/usr/bin/env python
import sys

# TF-IDF computation: Phase Two
# Mapper output: <document_name, <word, word_count>>

for line in sys.stdin:
    line = line.strip('\n')
    (key, word_count) = line.split('\t', 1)
    (word, doc_name) = key.split(",", 1)
    print_value = word + "," + word_count
    print ('%s\t%s' % (doc_name, print_value))
