#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Oct 29 21:55:56 2020

@author: piaoruilin
"""

from itertools import groupby
list1 = [0,1,1,1,1,0,0,0,1,1,1,0,0,0,0,0,0,0,0,0,1,1,1,1,1,1,1,1]
list2 = [0,1,1,1,1,0,0,0,1,1,1,0,0,0,0,0,0,0,0,0,1,1,1,1,1,1,1,1]
totallist =[list1,list2]
for x in range(len(totallist)):
    sortedlist = [[i, len([*group])] for i, group in groupby(totallist[x])]
print(sortedlist)
