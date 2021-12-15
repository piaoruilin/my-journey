#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Nov  2 07:55:36 2020

@author: piaoruilin
"""

list1 = ["a","b","c","d"]
list2 = ["a","c","e","f",'e']
total = []
def add_list(a,b):
    total.extend(a)
    total.extend(b)
    return total 
add_list(list1,list2)
def convert(sett):
    return list(sett)
def list_duplicates(seq):
    seen = set()
    seen_add = seen.add
    # adds all elements it doesn't know yet to seen and all other to seen_twice
    seen_twice = set( x for x in seq if x in seen or seen_add(x))
    # turn the set into a list (as requested)
    x = convert(seen_twice)
    return x

print(list_duplicates(total)) # yields [1, 2, 5]