# in each of the variables below, copy paste the file from your computer folder (the path) as as string so the conmputer can read it
# paste them according to the variable names

symptomsheet = '/Users/piaoruilin/Desktop/python/Hackathon Data - Sympyom Chart.csv'
cancersheet = '/Users/piaoruilin/Desktop/python/Hackathon Data - Cancer Symptom.csv'
drugsheet = '/Users/piaoruilin/Desktop/python/Hackathon Data - Drug Symptom.csv'
othersheet = '/Users/piaoruilin/Desktop/python/Hackathon Data - Other Symptom.csv'

import csv

symptom_list = []
description_list = []
cancer_area_list = []
cancer_symptom_list = []
cancer_description_list = []
cancer_fatal_freq = []
cancer_area_drug_list = []
cancer_type_list = []
drug_name_list = []
drug_symptom_list = []
drug_description_list = []
drug_normal_freq_list = []
drug_fatal_freqeuncy_list= []
drug_emergency_freq_list = []
drug_fatal_simul_list = []
other_symptom_list = []
other_description_list = []
other_fatal_freq_list = []

def open_sort_csv(b,c,d,e):
    #SYMPTOM
    with open(str(b), newline='') as symptomchart:
        reader = csv.reader(symptomchart)
        symptom_csv = [tuple(row) for row in reader]


    for i in range(len(symptom_csv)):
        symptom_list.append(symptom_csv[i][0])
        description_list.append(symptom_csv[i][1])

    #CANCER
    with open(str(c), newline='') as cancerchart:
        reader = csv.reader(cancerchart)
        cancer_csv = [tuple(row) for row in reader] 
        

    for i in range(len(cancer_csv)):
        cancer_area_list.append(cancer_csv[i][0])
        cancer_symptom_list.append(cancer_csv[i][1])
        cancer_description_list.append(cancer_csv[i][2])
        cancer_fatal_freq.append(cancer_csv[i][3])

    #DRUG
    with open(str(d), newline='') as f:  
        reader = csv.reader(f)
        drug_csv = [tuple(row) for row in reader]
        

    for i in range(len(drug_csv)):
        cancer_area_drug_list.append(drug_csv[i][0])
        cancer_type_list.append(drug_csv[i][1])
        drug_name_list.append(drug_csv[i][2])
        drug_symptom_list.append(drug_csv[i][3])
        drug_description_list.append(drug_csv[i][4])
        drug_normal_freq_list.append(drug_csv[i][5])
        drug_fatal_freqeuncy_list.append(drug_csv[i][6])
        drug_emergency_freq_list.append(drug_csv[i][7])
        drug_fatal_simul_list.append(drug_csv[i][8])
        
    #OTHER
    with open(str(e), newline='') as otherchart:
        reader = csv.reader(otherchart)
        other_csv = [tuple(row) for row in reader]
        
 #compare 
    for i in range(len(other_csv)):
        other_symptom_list.append(other_csv[i][0])
        other_description_list.append(other_csv[i][1])
        other_fatal_freq_list.append(other_csv[i][2])
    return(symptom_list,description_list,cancer_area_list,cancer_symptom_list,cancer_description_list,cancer_fatal_freq,cancer_area_drug_list,cancer_type_list,drug_name_list,drug_symptom_list,drug_description_list,drug_normal_freq_list,drug_fatal_freqeuncy_list,drug_emergency_freq_list,drug_fatal_simul_list)

open_sort_csv(symptomsheet,cancersheet,drugsheet,othersheet)

test_symptom_list = []
test_description_list = []
day1,day2,day3,day4 = ([] for i in range(4))
month=[day1,day2,day3,day4]
def user_csv_sort(usercsv):
    with open(str(usercsv), newline='') as testsheet:
        reader = csv.reader(testsheet)
        testcsv = list(reader)

    for i in range(len(testcsv)):
        test_symptom_list.append(testcsv[i][0])
        test_description_list.append(testcsv[i][1])

    for x in range(len(month)):
        for n in range(len(testcsv)):
            month[x].append(testcsv[n][x+2])

    return(test_symptom_list,test_description_list,month)
                            


