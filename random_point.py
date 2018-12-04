# -*- coding: utf-8 -*-
"""
Created on Sun Dec  2 20:24:09 2018

@author: zoya
"""

from random import randint


len_answer = len(open("test.txt", "r").readlines())
colors = ['r','g','y']
t = 0
with open("test.txt", "w") as f:
    while t <= len_answer:        
        for color in colors:
            line = "{0} - ({1},{2})".format(color, randint(0,10), randint(0,8))
            f.write(line + "\n")    
            t+=1
        f.write("----------\n")
        t+=1