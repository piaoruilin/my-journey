#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Nov  1 19:33:28 2020

@author: piaoruilin
"""

import csv

with open('/Users/piaoruilin/Desktop/python/Hackathon Data - Cancer Symptom.csv', 'rb') as cancer_symptom :
    cancer_trial = dict(str((r[3], i) for i, r in enumerate(csv.reader(cancer_symptom))))

with open('/Users/piaoruilin/Desktop/python/Hackathon Data - Drug Symptom.csv', 'rb') as drugs_symptom :
    with open('/Users/piaoruilin/Desktop/python/Hackathon Data - RL Testing.csv', 'wb') as results:    
        reader = csv.reader(drugs_symptom)
        writer = csv.writer(results)

        writer.writerow(next(reader, []) + ['RESULTS'])

        for row in reader:
            index = cancer_trial.get(row[3])
            if index is not None:
                message = 'FOUND in master list (row {})'.format(index)
            else:
                message = 'NOT FOUND in master list'
            writer.writerow(row + [message])
