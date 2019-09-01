# -*- coding: utf-8 -*-
"""
Created on Wed Aug 28 15:16:48 2019

@author: scott
"""
import re
import collections
import sys

my = str(sys.argv[1])
out = str(sys.argv[2])

myFile = open("my", "r")
outPut = open("out", "w+")

punctuations = '''!(),-[]{}.'"/\<>;:`@#$%^&*_'''

d1 = {}  

with myFile as f:
    file = f.read()
    words = re.split(" ", file)
    for w in words:
        for character in w.lower():
            if character in punctuations:
                w = w.replace(character, " ")
        if w.lower() != d1.keys():
            d1.update({w.lower() : 1})
        
        
    d1 = collections.OrderedDict(sorted(d1.items()))
    del d1['']
    for(key, value) in d1.items():
        for w in words:
           if key.lower() == w.lower():
               d1[key] += 1
        out = (key + " " + str(d1[key]))
        outPut.write(out)
        outPut.write("\n")
           
            
myFile.close()


