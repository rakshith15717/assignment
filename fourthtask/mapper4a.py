# -*- coding: utf-8 -*-
"""
Created on Sun May 10 18:37:41 2020

@author: rakshith
"""

#!/usr/bin/env python
from string import punctuation
import sys

# Mapper output: <<word, document_name>   1>

for line in sys.stdin:
    line = line.translate(None, punctuation).strip('\t')
    line_contents = line.split(" ")
    doc_name = line_contents[0]
    line_contents.remove(doc_name)
    for content in line_contents:
      content = content.rstrip()
      key = content + "," + doc_name
      print ('%s\t%s' % (key, 1))