# -*- coding: utf-8 -*-
"""
Created on Sat May  9 13:50:29 2020

@author: rakshith
"""
#!/usr/bin/python
import sys
import os
for line in sys.stdin:
     line = line.strip()
     words = line.split()
     for word in words:
         print '%s\t%s' % (word, "1")


