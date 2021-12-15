#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Nov  2 07:54:53 2020

@author: piaoruilin
"""

import csv
import operator

#Sorting out drugs symptoms and putting them into an array
drugs_list = []
drugs = open("/Users/piaoruilin/Desktop/python/Hackathon Data - Drug Symptom-2.csv", 'r')
csv1 = csv.reader(drugs, delimiter=',')
sort = sorted(csv1, key=operator.itemgetter(0))
for eachline in sort :
    drug_array = eachline
    drugs_list.append(drug_array)
    
#Sorting out cancer symptoms and putting them into an array
cancer_list = []
cancer = open("/Users/piaoruilin/Desktop/python/Hackathon Data - Cancer Symptom.csv", 'r')
csv2 = csv.reader(cancer, delimiter=',')
sort2 = sorted(csv2, key=operator.itemgetter(0))
for eachline_1 in sort2 :
    cancer_array = eachline_1
    cancer_list.append(cancer_array)
    
#Sorting out other symptoms and putting them into an array
others_list = []
others = open("/Users/piaoruilin/Desktop/python/Hackathon Data - Other Symptom.csv", 'r')
csv3 = csv.reader(others, delimiter=',')
sort3 = sorted(csv3, key=operator.itemgetter(0))
for eachline_2 in sort3 :
    others_array = eachline_2
    others_list.append(others_array)

#Trying to get rid of 1st and 2nd element in each array
test1 = [0, 'Male', 'Breast', ['Breast, HER2 Positive'], ['Perjeta'], 7]
test2 = [0, 'Male', 'Breast', ["Lymphoma, non-Hodgkin's"], ['Rituximab'], 12]
test3 = [0, 'Male', 'Brain ', ['Glioblastoma'], ['Avastin'], 4]
test4 = [0, 'Female', 'Breast', ['Breast, Metastatic'], ['Avastin', 'Herceptin', 'Xeloda'], 1]
index = [0,1,5]
newtest = [i for i in test1 if test1.index(i) not in index]

#Trying to imitate GUI
cancer_symptom = []
overall_symptom = ['Blood', 'Brain', 'Breast', 'Colorectal', 'Esophagus', 'Kidney', 'Liver', 'Lungs', 'Neuroendocrine', 'Ovary', 'Pancreas', 'Peritoneum', 'Skin', 'Stomach']

new_cancer_list=[[],[],[],[]]
new_drugs_list = []

'''
for i in range(len(cancer_list)) :
    if cancer_list[i][0]==newtest[0]:
        new_cancer_list[0].append(cancer_list[i])
    elif new_cancer_list[i][0]==newtest[1] :
        new_cancer_list[1].append(cancer_list[i])
    if drugs_list[i][0]==newtest[0]:
        new_drugs_list.append(drugs_list[i])
print(new_cancer_list)'''

array1 = [['a','b','c','d'],['e','b','f','g'],['a','c','e','f']]
mostfrequentsymptom = []
target_value = 'b'
for array in array1:
    for i in range(len(array)):
        if array[i] == target_value:
            wanted_array=array
            mostfrequentsymptom.append(wanted_array)


for i in range(len(cancer_list)) :
    if newtest[0]=='Breast' and cancer_list[i][0]=='Breast' :
        new_cancer_list[0].append(cancer_list[i])


new_drugs_list = []
for n in range(len(drugs_list)) :
    if newtest[0]=='Breast' and drugs_list[n][0]=='Breast' :
        new_drugs_list.append(drugs_list[n])
        
