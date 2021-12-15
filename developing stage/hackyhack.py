#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Oct 29 21:31:35 2020

@author: piaoruilin
"""

import csv
import operator

#SECTION: IMPORT HACKATHON DATA 
#----------------------------------------------------------------------------------------------------------------------------------
#HACKATHON DATA CSV PATHWAY
symptomsheet = '/Users/piaoruilin/Desktop/python/Hackathon Data - Sympyom Chart.csv'
cancersheet = '/Users/piaoruilin/Desktop/python/Hackathon Data - Cancer Symptom.csv'
drugsheet = '/Users/piaoruilin/Desktop/python/Hackathon Data - Drug Symptom-2.csv'
othersheet = '/Users/piaoruilin/Desktop/python/Hackathon Data - Other Symptom.csv'

'''
#HACAKTHON DATA - LIST
symptom_list, description_list = ([] for i in range(2)) #SYMPTOM
cancer_area_list, cancer_symptom_list,cancer_description_list,cancer_fatal_freq = ([] for i in range(4)) #CANCER
cancer_area_drug_list,cancer_type_list,drug_name_list,drug_symptom_list,drug_description_list = ([] for i in range(5)) #CANCERFREQ
drug_normal_freq_list,drug_fatal_freqeuncy_list,drug_emergency_freq_list,drug_fatal_simul_list = ([] for i in range(4)) #DRUG
other_symptom_list,other_description_list,other_fatal_freq_list = ([] for i in range(3)) #OTHER

#This function sorts all Hackathon Data in to list in columns
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
                    

#SECTION: IMPORT TEST DATA
#-----------------------------------------------------------------------------------------------------------------------------------
january,february,march,april,may,june,july,august,september,october,november,december = ([] for i in range(12))
jancsv,febcsv,marcsv,aprcsv,maycsv,juncsv,julcsv,augcsv,sepcsv,octcsv,novcsv,deccsv = ([] for i in range(12))

#TEST DATA CSV PATHWAY
janpath = '/Users/piaoruilin/Desktop/python/months/Test - January.csv'
febpath = '/Users/piaoruilin/Desktop/python/months/Test - February.csv'
marpath = '/Users/piaoruilin/Desktop/python/months/Test - March.csv'
aprpath = '/Users/piaoruilin/Desktop/python/months/Test - April.csv'
maypath = '/Users/piaoruilin/Desktop/python/months/Test - May.csv'
junpath = '/Users/piaoruilin/Desktop/python/months/Test - June.csv'
julpath = '/Users/piaoruilin/Desktop/python/months/Test - July.csv'
augpath = '/Users/piaoruilin/Desktop/python/months/Test - August.csv'
seppath = '/Users/piaoruilin/Desktop/python/months/Test - September.csv'
octpath = '/Users/piaoruilin/Desktop/python/months/Test - October.csv'
novpath = '/Users/piaoruilin/Desktop/python/months/Test - November.csv'
decpath = '/Users/piaoruilin/Desktop/python/months/Test - December.csv'
yearpath = [janpath,febpath,marpath,aprpath,maypath,junpath,julpath,augpath,seppath,octpath,novpath,decpath]

#This function sorts test data into lists so it can be plot
def sort_test_into_list():
    
    def test_get_january(jan):
        with open(str(jan), newline='') as file:
            reader = csv.reader(file)
            jancsv = [row for row in reader]
     
        for i in range(31):
            for j in range(534):
                january.append(jancsv[j][i])
    
    def test_get_february(feb):
        with open(str(feb), newline='') as file:
            reader = csv.reader(file)
            febcsv = [row for row in reader]
        
        for i in range(29):
            for j in range(534):
                february.append(febcsv[j][i])
    
    def test_get_march(mar):
        with open(str(mar), newline='') as file:
            reader = csv.reader(file)
            marcsv = [row for row in reader]
        
        for i in range(31):
            for j in range(534):
                march.append(marcsv[j][i])
                          
    def test_get_april(apr):
        with open(str(apr), newline='') as file:
            reader = csv.reader(file)
            aprcsv = [row for row in reader]
        
        for i in range(30):
            for j in range(534):
                april.append(aprcsv[j][i])
                
    def test_get_may(mayy):
        with open(str(mayy), newline='') as file:
            reader = csv.reader(file)
            maycsv = [row for row in reader]
        
        for i in range(31):
            for j in range(534):
                may.append(maycsv[j][i])
                
    def test_get_june(jun):
        with open(str(jun), newline='') as file:
            reader = csv.reader(file)
            juncsv = [row for row in reader]
        
        for i in range(30):
            for j in range(534):
                june.append(juncsv[j][i])
                
    def test_get_july(jul):
        with open(str(jul), newline='') as file:
            reader = csv.reader(file)
            julcsv = [row for row in reader]
        
        for i in range(31):
            for j in range(534):
                july.append(julcsv[j][i])
                
    def test_get_august(aug):
        with open(str(aug), newline='') as file:
            reader = csv.reader(file)
            augcsv = [row for row in reader]
        
        for i in range(31):
            for j in range(534):
                august.append(augcsv[j][i])
                
    def test_get_september(sep):
        with open(str(sep), newline='') as file:
            reader = csv.reader(file)
            aprcsv = [row for row in reader]
        
        for i in range(30):
            for j in range(534):
                september.append(aprcsv[j][i])
                       
    def test_get_october(octo):
        with open(str(octo), newline='') as file:
            reader = csv.reader(file)
            octcsv = [row for row in reader]
        
        for i in range(31):
            for j in range(534):
                october.append(octcsv[j][i])
                
    def test_get_november(nov):
        with open(str(nov), newline='') as file:
            reader = csv.reader(file)
            novcsv = [row for row in reader]
        
        for i in range(30):
            for j in range(534):
                november.append(novcsv[j][i])            
                
    def test_get_december(dec):
        with open(str(dec), newline='') as file:
            reader = csv.reader(file)
            deccsv = [row for row in reader]
        
        for i in range(31):
            for j in range(534):
                december.append(deccsv[j][i])            
                
    def test_get_year(year):
        test_get_january(year[0])
        test_get_february(year[1])
        test_get_march(year[2])
        test_get_april(year[3])
        test_get_may(year[4])
        test_get_june(year[5])
        test_get_july(year[6])
        test_get_august(year[7])
        test_get_september(year[8])
        test_get_october(year[9])
        test_get_november(year[10])
        test_get_december(year[11])
    
    test_get_year(yearpath)
    
sort_test_into_list()

#SECTION: SPLIT LIST INTO INDIVIDUAL DAYS FOR EACH MONTH
#------------------------------------------------------------------------------------------------------------------------------------

jan1,jan2,jan3,jan4,jan5,jan6,jan7,jan8,jan9,jan10,jan11,jan12,jan13,jan14,jan15 = ([] for i in range(15)) #Jan day 1-15
jan16,jan17,jan18,jan19,jan20,jan21,jan22,jan23,jan24,jan25,jan26,jan27,jan28,jan29,jan30,jan31 = ([] for i in range(16)) #Jan day 16-31

feb1,feb2,feb3,feb4,feb5,feb6,feb7,feb8,feb9,feb10,feb11,feb12,feb13,feb14,feb15 = ([] for i in range(15)) #Feb day 1-15
feb16,feb17,feb18,feb19,feb20,feb21,feb22,feb23,feb24,feb25,feb26,feb27,feb28,feb29 = ([] for i in range(14)) #Feb day 16-29

mar1,mar2,mar3,mar4,mar5,mar6,mar7,mar8,mar9,mar10,mar11,mar12,mar13,mar14,mar15 = ([] for i in range(15)) #Mar day 1-15
mar16,mar17,mar18,mar19,mar20,mar21,mar22,mar23,mar24,mar25,mar26,mar27,mar28,mar29,mar30,mar31 = ([] for i in range(16)) #Mar day 16-31

apr1,apr2,apr3,apr4,apr5,apr6,apr7,apr8,apr9,apr10,apr11,apr12,apr13,apr14,apr15= ([] for i in range(15)) #Apr day 1-15
apr16,apr17,apr18,apr19,apr20,apr21,apr22,apr23,apr24,apr25,apr26,apr27,apr28,apr29,apr30= ([] for i in range(15)) #Apr day 16-30

may1,may2,may3,may4,may5,may6,may7,may8,may9,may10,may11,may12,may13,may14,may15 = ([] for i in range(15)) #May day 1-15
may16,may17,may18,may19,may20,may21,may22,may23,may24,may25,may26,may27,may28,may29,may30,may31 = ([] for i in range(16)) #May day 16-31

jun1,jun2,jun3,jun4,jun5,jun6,jun7,jun8,jun9,jun10,jun11,jun12,jun13,jun14,jun15 = ([] for i in range(15)) #Jun day 1-15
jun16,jun17,jun18,jun19,jun20,jun21,jun22,jun23,jun24,jun25,jun26,jun27,jun28,jun29,jun30 = ([] for i in range(15)) #Jun day 16-30

jul1,jul2,jul3,jul4,jul5,jul6,jul7,jul8,jul9,jul10,jul11,jul12,jul13,jul14,jul15 = ([] for i in range(15)) #Jul day 1-15
jul16,jul17,jul18,jul19,jul20,jul21,jul22,jul23,jul24,jul25,jul26,jul27,jul28,jul29,jul30,jul31 = ([] for i in range(16)) #Jul day 16-31

aug1,aug2,aug3,aug4,aug5,aug6,aug7,aug8,aug9,aug10,aug11,aug12,aug13,aug14,aug15 = ([] for i in range(15)) #Aug day 1-15
aug16,aug17,aug18,aug19,aug20,aug21,aug22,aug23,aug24,aug25,aug26,aug27,aug28,aug29,aug30,aug31 = ([] for i in range(16)) #Aug day 16-31

sep1,sep2,sep3,sep4,sep5,sep6,sep7,sep8,sep9,sep10,sep11,sep12,sep13,sep14,sep15 = ([] for i in range(15)) #Sep day 1-15
sep16,sep17,sep18,sep19,sep20,sep21,sep22,sep23,sep24,sep25,sep26,sep27,sep28,sep29,sep30 = ([] for i in range(15)) #Sep day 16-30

oct1,oct2,oct3,oct4,oct5,oct6,oct7,oct8,oct9,oct10,oct11,oct12,oct13,oct14,oct15 = ([] for i in range(15)) #Oct day 1-15
oct16,oct17,oct18,oct19,oct20,oct21,oct22,oct23,oct24,oct25,oct26,oct27,oct28,oct29,oct30,oct31 = ([] for i in range(16)) #Oct day 16-31

nov1,nov2,nov3,nov4,nov5,nov6,nov7,nov8,nov9,nov10,nov11,nov12,nov13,nov14,nov15 = ([] for i in range(15)) #Nov day 1-15
nov16,nov17,nov18,nov19,nov20,nov21,nov22,nov23,nov24,nov25,nov26,nov27,nov28,nov29,nov30 = ([] for i in range(15)) #Nov day 16-30

dec1,dec2,dec3,dec4,dec5,dec6,dec7,dec8,dec9,dec10,dec11,dec12,dec13,dec14,dec15 = ([] for i in range(15)) #Dec day 1-15
dec16,dec17,dec18,dec19,dec20,dec21,dec22,dec23,dec24,dec25,dec26,dec27,dec28,dec29,dec30,dec31 = ([] for i in range(16)) #Dec day 16-31

def sort_months_into_days():
    a=534
    def sort_jan_into_days(jan):
        jan1.extend(jan[0:a])
        jan2.extend(jan[a:2*a])
        jan3.extend(jan[2*a:3*a])
        jan4.extend(jan[3*a:4*a])
        jan5.extend(jan[4*a:5*a])
        jan6.extend(jan[5*a:6*a])
        jan7.extend(jan[6*a:7*a])
        jan8.extend(jan[7*a:8*a])        
        jan9.extend(jan[8*a:9*a])
        jan10.extend(jan[9*a:10*a])
        jan11.extend(jan[10*a:11*a])
        jan12.extend(jan[11*a:12*a])
        jan13.extend(jan[12*a:13*a])
        jan14.extend(jan[13*a:14*a])
        jan15.extend(jan[14*a:15*a])
        jan16.extend(jan[15*a:16*a])
        jan17.extend(jan[16*a:17*a])
        jan18.extend(jan[17*a:18*a])
        jan19.extend(jan[18*a:19*a])
        jan20.extend(jan[19*a:20*a])
        jan21.extend(jan[20*a:21*a])
        jan22.extend(jan[21*a:22*a])
        jan23.extend(jan[22*a:23*a])
        jan24.extend(jan[23*a:24*a])    
        jan25.extend(jan[24*a:25*a])
        jan26.extend(jan[25*a:26*a])
        jan27.extend(jan[26*a:27*a])
        jan28.extend(jan[27*a:28*a])
        jan29.extend(jan[28*a:29*a])
        jan30.extend(jan[29*a:30*a])
        jan31.extend(jan[30*a:31*a])        
    def sort_feb_into_days(feb):
        feb1.extend(feb[0:a])
        feb2.extend(feb[a:2*a])
        feb3.extend(feb[2*a:3*a])
        feb4.extend(feb[3*a:4*a])
        feb5.extend(feb[4*a:5*a])
        feb6.extend(feb[5*a:6*a])
        feb7.extend(feb[6*a:7*a])
        feb8.extend(feb[7*a:8*a])
        feb9.extend(feb[8*a:9*a])
        feb10.extend(feb[9*a:10*a])
        feb11.extend(feb[10*a:11*a])
        feb12.extend(feb[11*a:12*a])
        feb13.extend(feb[12*a:13*a])
        feb14.extend(feb[13*a:14*a])
        feb15.extend(feb[14*a:15*a])
        feb16.extend(feb[15*a:16*a])        
        feb17.extend(feb[16*a:17*a])
        feb18.extend(feb[17*a:18*a])
        feb19.extend(feb[18*a:19*a])
        feb20.extend(feb[19*a:20*a])
        feb21.extend(feb[20*a:21*a])
        feb22.extend(feb[21*a:22*a])
        feb23.extend(feb[22*a:23*a])
        feb24.extend(feb[23*a:24*a])      
        feb25.extend(feb[24*a:25*a])
        feb26.extend(feb[25*a:26*a])
        feb27.extend(feb[26*a:27*a])
        feb28.extend(feb[27*a:28*a])
        feb29.extend(feb[28*a:29*a])
    def sort_mar_into_days(mar):
        mar1.extend(mar[0:a])
        mar2.extend(mar[a:2*a])
        mar3.extend(mar[2*a:3*a])
        mar4.extend(mar[3*a:4*a])
        mar5.extend(mar[4*a:5*a])
        mar6.extend(mar[5*a:6*a])
        mar7.extend(mar[6*a:7*a])
        mar8.extend(mar[7*a:8*a])
        mar9.extend(mar[8*a:9*a])
        mar10.extend(mar[9*a:10*a])
        mar11.extend(mar[10*a:11*a])
        mar12.extend(mar[11*a:12*a])
        mar13.extend(mar[12*a:13*a])
        mar14.extend(mar[13*a:14*a])
        mar15.extend(mar[14*a:15*a])
        mar16.extend(mar[15*a:16*a])   
        mar17.extend(mar[16*a:17*a])
        mar18.extend(mar[17*a:18*a])
        mar19.extend(mar[18*a:19*a])
        mar20.extend(mar[19*a:20*a])
        mar21.extend(mar[20*a:21*a])
        mar22.extend(mar[21*a:22*a])
        mar23.extend(mar[22*a:23*a])
        mar24.extend(mar[23*a:24*a])     
        mar25.extend(mar[24*a:25*a])
        mar26.extend(mar[25*a:26*a])
        mar27.extend(mar[26*a:27*a])
        mar28.extend(mar[27*a:28*a])
        mar29.extend(mar[28*a:29*a])
        mar30.extend(mar[29*a:30*a])
        mar31.extend(mar[30*a:31*a])
    def sort_apr_into_days(apr):
        apr1.extend(apr[0:a])
        apr2.extend(apr[a:2*a])
        apr3.extend(apr[2*a:3*a])
        apr4.extend(apr[3*a:4*a])
        apr5.extend(apr[4*a:5*a])
        apr6.extend(apr[5*a:6*a])
        apr7.extend(apr[6*a:7*a])
        apr8.extend(apr[7*a:8*a])   
        apr9.extend(apr[8*a:9*a])
        apr10.extend(apr[9*a:10*a])
        apr11.extend(apr[10*a:11*a])
        apr12.extend(apr[11*a:12*a])
        apr13.extend(apr[12*a:13*a])
        apr14.extend(apr[13*a:14*a])
        apr15.extend(apr[14*a:15*a])
        apr16.extend(apr[15*a:16*a])   
        apr17.extend(apr[16*a:17*a])
        apr18.extend(apr[17*a:18*a])
        apr19.extend(apr[18*a:19*a])
        apr20.extend(apr[19*a:20*a])
        apr21.extend(apr[20*a:21*a])
        apr22.extend(apr[21*a:22*a])
        apr23.extend(apr[22*a:23*a])
        apr24.extend(apr[23*a:24*a])    
        apr25.extend(apr[24*a:25*a])
        apr26.extend(apr[25*a:26*a])
        apr27.extend(apr[26*a:27*a])
        apr28.extend(apr[27*a:28*a])
        apr29.extend(apr[28*a:29*a])
        apr30.extend(apr[29*a:30*a])
    def sort_may_into_days(may):
        may1.extend(may[0:a])
        may2.extend(may[a:2*a])
        may3.extend(may[2*a:3*a])
        may4.extend(may[3*a:4*a])
        may5.extend(may[4*a:5*a])
        may6.extend(may[5*a:6*a])
        may7.extend(may[6*a:7*a])
        may8.extend(may[7*a:8*a])
        may9.extend(may[8*a:9*a])
        may10.extend(may[9*a:10*a])
        may11.extend(may[10*a:11*a])
        may12.extend(may[11*a:12*a])
        may13.extend(may[12*a:13*a])
        may14.extend(may[13*a:14*a])
        may15.extend(may[14*a:15*a])
        may16.extend(may[15*a:16*a])   
        may17.extend(may[16*a:17*a])
        may18.extend(may[17*a:18*a])
        may19.extend(may[18*a:19*a])
        may20.extend(may[19*a:20*a])
        may21.extend(may[20*a:21*a])
        may22.extend(may[21*a:22*a])
        may23.extend(may[22*a:23*a])
        may24.extend(may[23*a:24*a])   
        may25.extend(may[24*a:25*a])
        may26.extend(may[25*a:26*a])
        may27.extend(may[26*a:27*a])
        may28.extend(may[27*a:28*a])
        may29.extend(may[28*a:29*a])
        may30.extend(may[29*a:30*a])
        may31.extend(may[30*a:31*a])
    def sort_jun_into_days(jun):
        jun1.extend(jun[0:a])
        jun2.extend(jun[a:2*a])
        jun3.extend(jun[2*a:3*a])
        jun4.extend(jun[3*a:4*a])
        jun5.extend(jun[4*a:5*a])
        jun6.extend(jun[5*a:6*a])
        jun7.extend(jun[6*a:7*a])
        jun8.extend(jun[7*a:8*a])
        jun9.extend(jun[8*a:9*a])
        jun10.extend(jun[9*a:10*a])
        jun11.extend(jun[10*a:11*a])
        jun12.extend(jun[11*a:12*a])
        jun13.extend(jun[12*a:13*a])
        jun14.extend(jun[13*a:14*a])
        jun15.extend(jun[14*a:15*a])
        jun16.extend(jun[15*a:16*a])    
        jun17.extend(jun[16*a:17*a])
        jun18.extend(jun[17*a:18*a])
        jun19.extend(jun[18*a:19*a])
        jun20.extend(jun[19*a:20*a])
        jun21.extend(jun[20*a:21*a])
        jun22.extend(jun[21*a:22*a])
        jun23.extend(jun[22*a:23*a])
        jun24.extend(jun[23*a:24*a])  
        jun25.extend(jun[24*a:25*a])
        jun26.extend(jun[25*a:26*a])
        jun27.extend(jun[26*a:27*a])
        jun28.extend(jun[27*a:28*a])
        jun29.extend(jun[28*a:29*a])
        jun30.extend(jun[29*a:30*a])
    def sort_jul_into_days(jul):
        jul1.extend(jul[0:a])
        jul2.extend(jul[a:2*a])
        jul3.extend(jul[2*a:3*a])
        jul4.extend(jul[3*a:4*a])
        jul5.extend(jul[4*a:5*a])
        jul6.extend(jul[5*a:6*a])
        jul7.extend(jul[6*a:7*a])
        jul8.extend(jul[7*a:8*a])
        jul9.extend(jul[8*a:9*a])
        jul10.extend(jul[9*a:10*a])
        jul11.extend(jul[10*a:11*a])
        jul12.extend(jul[11*a:12*a])
        jul13.extend(jul[12*a:13*a])
        jul14.extend(jul[13*a:14*a])
        jul15.extend(jul[14*a:15*a])
        jul16.extend(jul[15*a:16*a])  
        jul17.extend(jul[16*a:17*a])
        jul18.extend(jul[17*a:18*a])
        jul19.extend(jul[18*a:19*a])
        jul20.extend(jul[19*a:20*a])
        jul21.extend(jul[20*a:21*a])
        jul22.extend(jul[21*a:22*a])
        jul23.extend(jul[22*a:23*a])
        jul24.extend(jul[23*a:24*a])   
        jul25.extend(jul[24*a:25*a])
        jul26.extend(jul[25*a:26*a])
        jul27.extend(jul[26*a:27*a])
        jul28.extend(jul[27*a:28*a])
        jul29.extend(jul[28*a:29*a])
        jul30.extend(jul[29*a:30*a])
        jul31.extend(jul[30*a:31*a])
    def sort_aug_into_days(aug):
        aug1.extend(aug[0:a])
        aug2.extend(aug[a:2*a])
        aug3.extend(aug[2*a:3*a])
        aug4.extend(aug[3*a:4*a])
        aug5.extend(aug[4*a:5*a])
        aug6.extend(aug[5*a:6*a])
        aug7.extend(aug[6*a:7*a])
        aug8.extend(aug[7*a:8*a])
        aug9.extend(aug[8*a:9*a])
        aug10.extend(aug[9*a:10*a])
        aug11.extend(aug[10*a:11*a])
        aug12.extend(aug[11*a:12*a])
        aug13.extend(aug[12*a:13*a])
        aug14.extend(aug[13*a:14*a])
        aug15.extend(aug[14*a:15*a])
        aug16.extend(aug[15*a:16*a])     
        aug17.extend(aug[16*a:17*a])
        aug18.extend(aug[17*a:18*a])
        aug19.extend(aug[18*a:19*a])
        aug20.extend(aug[19*a:20*a])
        aug21.extend(aug[20*a:21*a])
        aug22.extend(aug[21*a:22*a])
        aug23.extend(aug[22*a:23*a])
        aug24.extend(aug[23*a:24*a])
        aug25.extend(aug[24*a:25*a])
        aug26.extend(aug[25*a:26*a])
        aug27.extend(aug[26*a:27*a])
        aug28.extend(aug[27*a:28*a])
        aug29.extend(aug[28*a:29*a])
        aug30.extend(aug[29*a:30*a])
        aug31.extend(aug[30*a:31*a])
    def sort_sep_into_days(sep):
        sep1.extend(sep[0:a])
        sep2.extend(sep[a:2*a])
        sep3.extend(sep[2*a:3*a])
        sep4.extend(sep[3*a:4*a])
        sep5.extend(sep[4*a:5*a])
        sep6.extend(sep[5*a:6*a])
        sep7.extend(sep[6*a:7*a])
        sep8.extend(sep[7*a:8*a])
        sep9.extend(sep[8*a:9*a])
        sep10.extend(sep[9*a:10*a])
        sep11.extend(sep[10*a:11*a])
        sep12.extend(sep[11*a:12*a])
        sep13.extend(sep[12*a:13*a])
        sep14.extend(sep[13*a:14*a])
        sep15.extend(sep[14*a:15*a])
        sep16.extend(sep[15*a:16*a])      
        sep17.extend(sep[16*a:17*a])
        sep18.extend(sep[17*a:18*a])
        sep19.extend(sep[18*a:19*a])
        sep20.extend(sep[19*a:20*a])
        sep21.extend(sep[20*a:21*a])
        sep22.extend(sep[21*a:22*a])
        sep23.extend(sep[22*a:23*a])
        sep24.extend(sep[23*a:24*a])      
        sep25.extend(sep[24*a:25*a])
        sep26.extend(sep[25*a:26*a])
        sep27.extend(sep[26*a:27*a])
        sep28.extend(sep[27*a:28*a])
        sep29.extend(sep[28*a:29*a])
        sep30.extend(sep[29*a:30*a])
    def sort_oct_into_days(octo):
        oct1.extend(octo[0:a])
        oct2.extend(octo[a:2*a])
        oct3.extend(octo[2*a:3*a])
        oct4.extend(octo[3*a:4*a])
        oct5.extend(octo[4*a:5*a])
        oct6.extend(octo[5*a:6*a])
        oct7.extend(octo[6*a:7*a])
        oct8.extend(octo[7*a:8*a])   
        oct9.extend(octo[8*a:9*a])
        oct10.extend(octo[9*a:10*a])
        oct11.extend(octo[10*a:11*a])
        oct12.extend(octo[11*a:12*a])
        oct13.extend(octo[12*a:13*a])
        oct14.extend(octo[13*a:14*a])
        oct15.extend(octo[14*a:15*a])
        oct16.extend(octo[15*a:16*a])      
        oct17.extend(octo[16*a:17*a])
        oct18.extend(octo[17*a:18*a])
        oct19.extend(octo[18*a:19*a])
        oct20.extend(octo[19*a:20*a])
        oct21.extend(octo[20*a:21*a])
        oct22.extend(octo[21*a:22*a])
        oct23.extend(octo[22*a:23*a])
        oct24.extend(octo[23*a:24*a])     
        oct25.extend(octo[24*a:25*a])
        oct26.extend(octo[25*a:26*a])
        oct27.extend(octo[26*a:27*a])
        oct28.extend(octo[27*a:28*a])
        oct29.extend(octo[28*a:29*a])
        oct30.extend(octo[29*a:30*a])
        oct31.extend(octo[30*a:31*a])
    def sort_nov_into_days(nov):
        nov1.extend(nov[0:a])
        nov2.extend(nov[a:2*a])
        nov3.extend(nov[2*a:3*a])
        nov4.extend(nov[3*a:4*a])
        nov5.extend(nov[4*a:5*a])
        nov6.extend(nov[5*a:6*a])
        nov7.extend(nov[6*a:7*a])
        nov8.extend(nov[7*a:8*a])
        nov9.extend(nov[8*a:9*a])
        nov10.extend(nov[9*a:10*a])
        nov11.extend(nov[10*a:11*a])
        nov12.extend(nov[11*a:12*a])
        nov13.extend(nov[12*a:13*a])
        nov14.extend(nov[13*a:14*a])
        nov15.extend(nov[14*a:15*a])
        nov16.extend(nov[15*a:16*a])
        nov17.extend(nov[16*a:17*a])
        nov18.extend(nov[17*a:18*a])
        nov19.extend(nov[18*a:19*a])
        nov20.extend(nov[19*a:20*a])
        nov21.extend(nov[20*a:21*a])
        nov22.extend(nov[21*a:22*a])
        nov23.extend(nov[22*a:23*a])
        nov24.extend(nov[23*a:24*a])   
        nov25.extend(nov[24*a:25*a])
        nov26.extend(nov[25*a:26*a])
        nov27.extend(nov[26*a:27*a])
        nov28.extend(nov[27*a:28*a])
        nov29.extend(nov[28*a:29*a])
        nov30.extend(nov[29*a:30*a])
    def sort_dec_into_days(dec):
        dec1.extend(dec[0:a])
        dec2.extend(dec[a:2*a])
        dec3.extend(dec[2*a:3*a])
        dec4.extend(dec[3*a:4*a])
        dec5.extend(dec[4*a:5*a])
        dec6.extend(dec[5*a:6*a])
        dec7.extend(dec[6*a:7*a])
        dec8.extend(dec[7*a:8*a])
        dec9.extend(dec[8*a:9*a])
        dec10.extend(dec[9*a:10*a])
        dec11.extend(dec[10*a:11*a])
        dec12.extend(dec[11*a:12*a])
        dec13.extend(dec[12*a:13*a])
        dec14.extend(dec[13*a:14*a])
        dec15.extend(dec[14*a:15*a])
        dec16.extend(dec[15*a:16*a])
        dec17.extend(dec[16*a:17*a])
        dec18.extend(dec[17*a:18*a])
        dec19.extend(dec[18*a:19*a])
        dec20.extend(dec[19*a:20*a])
        dec21.extend(dec[20*a:21*a])
        dec22.extend(dec[21*a:22*a])
        dec23.extend(dec[22*a:23*a])
        dec24.extend(dec[23*a:24*a])
        dec25.extend(dec[24*a:25*a])
        dec26.extend(dec[25*a:26*a])
        dec27.extend(dec[26*a:27*a])
        dec28.extend(dec[27*a:28*a])
        dec29.extend(dec[28*a:29*a])
        dec30.extend(dec[29*a:30*a])
        dec31.extend(dec[30*a:31*a])
    sort_jan_into_days(january)
    sort_feb_into_days(february)
    sort_mar_into_days(march)
    sort_apr_into_days(april)
    sort_may_into_days(may)
    sort_jul_into_days(june)
    sort_jul_into_days(july)
    sort_aug_into_days(august)
    sort_sep_into_days(september)
    sort_oct_into_days(october)
    sort_nov_into_days(november)
    sort_dec_into_days(december)

sort_months_into_days() #Now you can access each day and compare it to symptom or cancer list

jan_month = [jan1,jan2,jan3,jan4,jan5,jan6,jan7,jan8,jan9,jan10,jan11,jan12,jan13,jan14,jan15,jan16,jan17,jan18,jan19,jan20,jan21,jan22,jan23,jan24,jan25,jan26,jan27,jan28,jan29,jan30,jan31]
feb_month = [feb1,feb2,feb3,feb4,feb5,feb6,feb7,feb8,feb9,feb10,feb11,feb12,feb13,feb14,feb15,feb16,feb17,feb18,feb19,feb20,feb21,feb22,feb23,feb24,feb25,feb26,feb27,feb28,feb29]
mar_month = [mar1,mar2,mar3,mar4,mar5,mar6,mar7,mar8,mar9,mar10,mar11,mar12,mar13,mar14,mar15,mar16,mar17,mar18,mar19,mar20,mar21,mar22,mar23,mar24,mar25,mar26,mar27,mar28,mar29,mar30,mar31]
apr_month = [apr1,apr2,apr3,apr4,apr5,apr6,apr7,apr8,apr9,apr10,apr11,apr12,apr13,apr14,apr15,apr16,apr17,apr18,apr19,apr20,apr21,apr22,apr23,apr24,apr25,apr26,apr27,apr28,apr29,apr30]
may_month = [may1,may2,may3,may4,may5,may6,may7,may8,may9,may10,may11,may12,may13,may14,may15,may16,may17,may18,may19,may20,may21,may22,may23,may24,may25,may26,may27,may28,may29,may30,may31]
jun_month = [jun1,jun2,jun3,jun4,jun5,jun6,jun7,jun8,jun9,jun10,jun11,jun12,jun13,jun14,jun15,jun16,jun17,jun18,jun19,jun20,jun21,jun22,jun23,jun24,jun25,jun26,jun27,jun28,jun29,jun30]
jul_month = [jul1,jul2,jul3,jul4,jul5,jul6,jul7,jul8,jul9,jul10,jul11,jul12,jul13,jul14,jul15,jul16,jul17,jul18,jul19,jul20,jul21,jul22,jul23,jul24,jul25,jul26,jul27,jul28,jul29,jul30,jul31]
aug_month = [aug1,aug2,aug3,aug4,aug5,aug6,aug7,aug8,aug9,aug10,aug11,aug12,aug13,aug14,aug15,aug16,aug17,aug18,aug19,aug20,aug21,aug22,aug23,aug24,aug25,aug26,aug27,aug28,aug29,aug30,aug31]
sep_month = [sep1,sep2,sep3,sep4,sep5,sep6,sep7,sep8,sep9,sep10,sep11,sep12,sep13,sep14,sep15,sep16,sep17,sep18,sep19,sep20,sep21,sep22,sep23,sep24,sep25,sep26,sep27,sep28,sep29,sep30]
oct_month = [oct1,oct2,oct3,oct4,oct5,oct6,oct7,oct8,oct9,oct10,oct11,oct12,oct13,oct14,oct15,oct16,oct17,oct18,oct19,oct20,oct21,oct22,oct23,oct24,oct25,oct26,oct27,oct28,oct29,oct30,oct31]
nov_month = [nov1,nov2,nov3,nov4,nov5,nov6,nov7,nov8,nov9,nov10,nov11,nov12,nov13,nov14,nov15,nov16,nov17,nov18,nov19,nov20,nov21,nov22,nov23,nov24,nov25,nov26,nov27,nov28,nov29,nov30]
dec_month = [dec1,dec2,dec3,dec4,dec5,dec6,dec7,dec8,dec9,dec10,dec11,dec12,dec13,dec14,dec15,dec16,dec17,dec18,dec19,dec20,dec21,dec22,dec23,dec24,dec25,dec26,dec27,dec28,dec29,dec30,dec31]
'''

#ruilin trying :')
with open('/Users/piaoruilin/Desktop/python/Hackathon Data - Sympyom Chart.csv', 'r') as symptom_chart :
    symptom_chart_array = []
    csv_symptom_chart = csv.reader(symptom_chart, delimiter=',')
    sort_symptom_chart = sorted(csv_symptom_chart, key=operator.itemgetter(1))
    for line_symptom_chart in sort_symptom_chart :
        symptom_array = line_symptom_chart
        symptom_chart_array.append(symptom_array) #with this im done with sorting only the description of symptom 
'''
janshow = []
for i in range(len(symptom_chart_array)) :
    if jan_month[0][i] == '1':
        jan_symptoms = jan_month[0]
        janshow.append(jan_symptoms)

print(janshow)'''


