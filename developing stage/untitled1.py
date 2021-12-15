#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Nov  1 19:39:33 2020

@author: piaoruilin
"""

import csv

drugs_sheet = "/Users/piaoruilin/Desktop/python/Hackathon Data - Drug Symptom-2.csv"

with open("/Users/piaoruilin/Desktop/python/Hackathon Data - Drug Symptom-2.csv", newline='') as cancerchart:
    reader = csv.reader(cancerchart)
    cancer_csv = [tuple(row) for row in reader]
print(cancer_csv)