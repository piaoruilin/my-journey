test_sheet = "/Users/piaoruilin/Desktop/hacky test - Sheet2.csv"

import csv
import operator

sample = open('/Users/piaoruilin/Desktop/hacky test - Sheet2.csv', 'r')
csv1 = csv.reader(sample, delimiter=',')     
sort = sorted(csv1,key=operator.itemgetter(0))

for eachline in sort :
    print(eachline)
