#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Nov  5 00:21:33 2020

@author: piaoruilin
"""

import csv
import numpy as np
'''
import matplotlib.pyplot as plt 
from itertools import groupby
import tkinter as tk 
import time
from tkinter import *

#SECTION: GETTING JUDGES INFO FROM GUI
#----------------------------------------------------------------------------------------------------------------------------------------
user_choice = []
def get_user_info():
    gui_1 = tk.Tk()
    gui_1.title("Getting user information")
    gui_1.geometry("1000x850")
#Tkinter Variables
    age_user,drug_1,drug_2,drug_3,month_user,treatment_user_2,treatment_user_1 = tk.IntVar(),tk.IntVar(),tk.IntVar(),tk.IntVar(),tk.IntVar(),tk.IntVar(),tk.IntVar()
    gender_user,cancer_location_user,cancer_type_user = tk.StringVar(),tk.StringVar(),tk.StringVar()
#Global List
    drug_user_input = []
    cancer_type_user_input = []
    
#LABELS----------------------------------------------------------------------------------------------------------------------------------------
    q1 = tk.Label(gui_1,
                  text="""What is the age of patient?""",
                  font=('Imago',13,'bold'),
                  justify = 'left')
    q2 = tk.Label(gui_1,
                  text="""Please select patient's gender""",
                  font=('Imago',13,'bold'),
                  anchor = 'w')
    q3 = tk.Label(gui_1,
                  text="""Where is the patient's cancer located?""",
                  font=('Imago',13,'bold'),
                  anchor = 'w')
    q4_1 = tk.Label(gui_1,
                  text="""What type of cancer is the patient experiencing?""",
                  font=('Imago',13,'bold'),
                  anchor = 'w')
    q4_2 = tk.Label(gui_1,
                  text="""The type of cancer patient is experiencing:""",
                  font=('Imago',13,'bold'),
                  anchor = 'w')
    q5_1 = tk.Label(gui_1,
                  text="""Which drugs are currently used to treat patient?""",
                  font=('Imago',13,'bold'),
                  anchor = 'w')
    q5_2 = tk.Label(gui_1,
                  text="""Drug used to treat patient:""",
                  font=('Imago',13,'bold'),
                  anchor = 'w')
    q6 = tk.Label(gui_1,
                  text="Select any process patient is going through below:",
                  font=('Imago',13,'bold'),
                  anchor = 'w')
    q7 = tk.Label(gui_1,
                  text="Select the month your patient is visitng:",
                  font=('Imago',13,'bold'),
                  anchor = 'w')
    p = tk.Label(gui_1,
                  text="""Progress 0/7""",
                  font=('Imago',17,'bold'),
                  anchor = 'w',
                  fg='#0066CC')
    
#QUESTION 1----------------------------------------------------------------------------------------------------------------------------------------
    age_enter = tk.Entry(gui_1,
                         textvariable = age_user,
                         width = 30,
                         font=('Imaho',13))
    age_enter.place(x=40,y=60)
    def store_age():
        user_age = age_user.get()
        user_choice.append(user_age)
        print(user_choice)
        def store_gender():
            user_gender = gender_user.get()
            user_choice.append(user_gender)
            print(user_choice)
            def store_cancer_location():
                user_cancer_location = cancer_location_user.get()
                user_choice.append(user_cancer_location)
                print(user_choice)
                #START OF Q4
                if user_choice[2] == 'Blood':
                    btn4_1,btn4_2,btn4_3= '','',''
                    buttons4 = [btn4_1,btn4_2,btn4_3]
                    buttons4_options = ['Leukemia, Chronic Lymphocytic','Lymphoma',"Lymphoma, non-Hodgkin's"]        
                    def store_cancer_type():
                        user_cancer_type = cancer_type_user.get()
                        cancer_type_user_input.append(user_cancer_type)
                        user_choice.append(cancer_type_user_input)
                        print(user_choice)
                        #START Q5
                        if user_choice[3][0] == 'Leukemia, Chronic Lymphocytic':
                            options = ['Gazyva','Rituximab']
                            def store_drug_options():
                                option1 = drug_1.get()
                                option2 = drug_2.get()
                                if option1 == 1:
                                    drug_user_input.append("Gazyva")
                                if option2 == 1:
                                    drug_user_input.append("Rituximab")
                                user_choice.append(drug_user_input)
                                print(user_choice)
                                drugoptions ='Kadcyla'
                                toptions = ['Metastatic, Prior Treatment','Recurrance Treatment','None']
                                def store_treament():
                                    option1 = treatment_user_1.get()
                                    option2 = treatment_user_2.get()
                                    if option2 ==1 and option1==2:
                                        user_choice[3].append('Metastatic, Prior Treatment')   
                                        user_choice[3].append('Recurrance Treatment')
                                        user_choice[4].append(drugoptions)   
                                    elif option1 ==1:
                                        user_choice[3].append('Metastatic, Prior Treatment')
                                        user_choice[4].append(drugoptions)
                                    elif option2 ==1:
                                        user_choice[3].append('Recurrance Treatment')
                                        user_choice[4].append(drugoptions)  

                                    print(user_choice)
                                    def store_show_month():
                                        user_month = month_user.get()
                                        user_choice.append(user_month)
                                        print(user_choice)
                                        def close_window():
                                            gui_1.destroy()
                                        def change_label():
                                            p.destroy()
                                            pfinal = tk.Label(gui_1,text="""Complete!""",width =30,font=('Imago',17,'bold'),anchor = 'w',fg='#0066CC')
                                            pfinal.place(x=400,y=775)
                                        change_label()
                                        close_window()
                                    btn6_1,btn6_2,btn6_3,btn6_4,btn6_5,btn6_6,btn6_7,btn6_8,btn6_9,btn6_10,btn6_11,btn6_12 = '','','','','','','','','','','',''
                                    bttn6 = [btn6_1,btn6_2,btn6_3,btn6_4,btn6_5,btn6_6,btn6_7,btn6_8,btn6_9,btn6_10,btn6_11,btn6_12]
                                    optionm = [("January"),("February"),("March"),("April"),("May"),("June"),("July"),("August"),("September"),("October"),("November"),("December")]
                                    array = [1,2,3,4,5,6,7,8,9,10,11,12]
                                    for i in range(6):
                                        yval = 555 + 30*(i)
                                        bttn6[i] = tk.Radiobutton(gui_1,
                                                                text = optionm[i],
                                                                variable = month_user,
                                                                width = 15,
                                                                font=('Imago',13),
                                                                command = store_show_month,
                                                                value = array[i],
                                                                anchor = 'w')
                                        bttn6[i].place(x=500,y=yval)
                                    for i in range(6):
                                        yval = 555 + 30*(i)
                                        bttn6[i] = tk.Radiobutton(gui_1,
                                                                text = optionm[i+6],
                                                                variable = month_user,
                                                                width = 15,
                                                                font=('Imago',13),
                                                                command = store_show_month,
                                                                value = array[i+6],
                                                                anchor = 'w')
                                        bttn6[i].place(x=700,y=yval)
                                    q7.place(x=500,y=525)
                                    p.config(text = "Progress: 6/7")                                
                                btn1 = tk.Checkbutton(gui_1, text=toptions[0], variable=treatment_user_1, width = 30,font=('Imago',13),anchor ='w')
                                btn1.place(x=500,y=375)
                                btn2 = tk.Checkbutton(gui_1, text=toptions[1], variable=treatment_user_2, width = 30,font=('Imago',13),anchor ='w')
                                btn2.place(x=500,y=405)  
                                btn3 = tk.Checkbutton(gui_1, text=toptions[2], width = 20,font=('Imago',13),anchor ='w')
                                btn3.place(x=500,y=435) 
                                enter = tk.Button(gui_1, text='Select Treatment', font=('Imago',13), command = store_treament)
                                enter.place(x=500,y=465)
                                q6.place(x=500,y=345)
                                p.config(text="Progress: 5/7")                               
                            #INSERT Q6 HERE
                            btn1 = tk.Checkbutton(gui_1, text=options[0], variable=drug_1, width = 25,font=('Imago',13),anchor ='w')
                            btn1.place(x=500,y=215)
                            btn2 = tk.Checkbutton(gui_1, text=options[1], variable=drug_2, width = 25,font=('Imago',13),anchor ='w')
                            btn2.place(x=500,y=245)
                            enter = tk.Button(gui_1, text='Select Drug', font=('Imago',13), command = store_drug_options)
                            enter.place(x=500,y=280)
                            q5_1.place(x=500,y=185)
                            p.config(text="Progress: 4/7")
                        
                        if user_choice[3][0] == 'Lymphoma':
                            options ='Gazyva'
                            def store_drug_options():
                                drug_user_input.append(options)
                                user_choice.append(drug_user_input)
                                print(user_choice)
                                drugoptions ='Kadcyla'
                                toptions = ['Metastatic, Prior Treatment','Recurrance Treatment','None']
                                def store_treament():
                                    option1 = treatment_user_1.get()
                                    option2 = treatment_user_2.get()
                                    if option2 ==1 and option1==2:
                                        user_choice[3].append('Metastatic, Prior Treatment')   
                                        user_choice[3].append('Recurrance Treatment')
                                        user_choice[4].append(drugoptions)   
                                    elif option1 ==1:
                                        user_choice[3].append('Metastatic, Prior Treatment')
                                        user_choice[4].append(drugoptions)
                                    elif option2 ==1:
                                        user_choice[3].append('Recurrance Treatment')
                                        user_choice[4].append(drugoptions)  

                                    print(user_choice)
                                    def store_show_month():
                                        user_month = month_user.get()
                                        user_choice.append(user_month)
                                        print(user_choice)
                                        def close_window():
                                            gui_1.destroy()
                                        def change_label():
                                            p.destroy()
                                            pfinal = tk.Label(gui_1,text="""Complete!""",width =30,font=('Imago',17,'bold'),anchor = 'w',fg='#0066CC')
                                            pfinal.place(x=400,y=775)
                                        change_label()
                                        close_window()
                                    btn6_1,btn6_2,btn6_3,btn6_4,btn6_5,btn6_6,btn6_7,btn6_8,btn6_9,btn6_10,btn6_11,btn6_12 = '','','','','','','','','','','',''
                                    bttn6 = [btn6_1,btn6_2,btn6_3,btn6_4,btn6_5,btn6_6,btn6_7,btn6_8,btn6_9,btn6_10,btn6_11,btn6_12]
                                    optionm = [("January"),("February"),("March"),("April"),("May"),("June"),("July"),("August"),("September"),("October"),("November"),("December")]
                                    array = [1,2,3,4,5,6,7,8,9,10,11,12]
                                    for i in range(6):
                                        yval = 480 + 30*(i)
                                        bttn6[i] = tk.Radiobutton(gui_1,
                                                                text = optionm[i],
                                                                variable = month_user,
                                                                width = 15,
                                                                font=('Imago',13),
                                                                command = store_show_month,
                                                                value = array[i],
                                                                anchor = 'w')
                                        bttn6[i].place(x=500,y=yval)
                                    for i in range(6):
                                        yval = 480 + 30*(i)
                                        bttn6[i] = tk.Radiobutton(gui_1,
                                                                text = optionm[i+6],
                                                                variable = month_user,
                                                                width = 15,
                                                                font=('Imago',13),
                                                                command = store_show_month,
                                                                value = array[i+6],
                                                                anchor = 'w')
                                        bttn6[i].place(x=700,y=yval)
                                    q7.place(x=500,y=450)
                                    p.config(text = "Progress: 6/7")                                
                                btn1 = tk.Checkbutton(gui_1, text=toptions[0], variable=treatment_user_1, width = 30,font=('Imago',13),anchor ='w')
                                btn1.place(x=500,y=290)
                                btn2 = tk.Checkbutton(gui_1, text=toptions[1], variable=treatment_user_2, width = 30,font=('Imago',13),anchor ='w')
                                btn2.place(x=500,y=320)  
                                btn3 = tk.Checkbutton(gui_1, text=toptions[2], width = 20,font=('Imago',13),anchor ='w')
                                btn3.place(x=500,y=350) 
                                enter = tk.Button(gui_1, text='Select Treatment', font=('Imago',13), command = store_treament)
                                enter.place(x=500,y=380)
                                q6.place(x=500,y=260)
                                p.config(text="Progress: 5/7")
                            ans = tk.Label(gui_1,
                                            text = options,
                                            font=('Imago',13),
                                            anchor = 'w')
                            ans.place(x=500,y=215)
                            q5_2.place(x=500,y=185)
                            p.config(text="Progress: 5/7") 
                            store_drug_options()   
                            
                        if user_choice[3][0] == 'Lymphoma, non-Hodgkin\'s':
                            options ='Rituximab'
                            def store_drug_options():
                                drug_user_input.append(options)
                                user_choice.append(drug_user_input)
                                print(user_choice)
                                drugoptions ='Kadcyla'
                                toptions = ['Metastatic, Prior Treatment','Recurrance Treatment','None']
                                def store_treament():
                                    option1 = treatment_user_1.get()
                                    option2 = treatment_user_2.get()
                                    if option2 ==1 and option1==2:
                                        user_choice[3].append('Metastatic, Prior Treatment')   
                                        user_choice[3].append('Recurrance Treatment')
                                        user_choice[4].append(drugoptions)   
                                    elif option1 ==1:
                                        user_choice[3].append('Metastatic, Prior Treatment')
                                        user_choice[4].append(drugoptions)
                                    elif option2 ==1:
                                        user_choice[3].append('Recurrance Treatment')
                                        user_choice[4].append(drugoptions)  

                                    print(user_choice)
                                    def store_show_month():
                                        user_month = month_user.get()
                                        user_choice.append(user_month)
                                        print(user_choice)
                                        def close_window():
                                            gui_1.destroy()
                                        def change_label():
                                            p.destroy()
                                            pfinal = tk.Label(gui_1,text="""Complete!""",width =30,font=('Imago',17,'bold'),anchor = 'w',fg='#0066CC')
                                            pfinal.place(x=400,y=775)
                                        change_label()
                                        close_window()
                                    btn6_1,btn6_2,btn6_3,btn6_4,btn6_5,btn6_6,btn6_7,btn6_8,btn6_9,btn6_10,btn6_11,btn6_12 = '','','','','','','','','','','',''
                                    bttn6 = [btn6_1,btn6_2,btn6_3,btn6_4,btn6_5,btn6_6,btn6_7,btn6_8,btn6_9,btn6_10,btn6_11,btn6_12]
                                    optionm = [("January"),("February"),("March"),("April"),("May"),("June"),("July"),("August"),("September"),("October"),("November"),("December")]
                                    array = [1,2,3,4,5,6,7,8,9,10,11,12]
                                    for i in range(6):
                                        yval = 490 + 30*(i)
                                        bttn6[i] = tk.Radiobutton(gui_1,
                                                                text = optionm[i],
                                                                variable = month_user,
                                                                width = 15,
                                                                font=('Imago',13),
                                                                command = store_show_month,
                                                                value = array[i],
                                                                anchor = 'w')
                                        bttn6[i].place(x=500,y=yval)
                                    for i in range(6):
                                        yval = 490 + 30*(i)
                                        bttn6[i] = tk.Radiobutton(gui_1,
                                                                text = optionm[i+6],
                                                                variable = month_user,
                                                                width = 15,
                                                                font=('Imago',13),
                                                                command = store_show_month,
                                                                value = array[i+6],
                                                                anchor = 'w')
                                        bttn6[i].place(x=700,y=yval)
                                    q7.place(x=500,y=460)
                                    p.config(text = "Progress: 6/7")                                
                                btn1 = tk.Checkbutton(gui_1, text=toptions[0], variable=treatment_user_1, width = 30,font=('Imago',13),anchor ='w')
                                btn1.place(x=500,y=295)
                                btn2 = tk.Checkbutton(gui_1, text=toptions[1], variable=treatment_user_2, width = 30,font=('Imago',13),anchor ='w')
                                btn2.place(x=500,y=325)  
                                btn3 = tk.Checkbutton(gui_1, text=toptions[2], width = 20,font=('Imago',13),anchor ='w')
                                btn3.place(x=500,y=355) 
                                enter = tk.Button(gui_1, text='Select Treatment', font=('Imago',13), command = store_treament)
                                enter.place(x=500,y=385)
                                q6.place(x=500,y=265)
                                p.config(text="Progress: 5/7")                                
                            ans = tk.Label(gui_1,
                                            text = options,
                                            font=('Imago',13),
                                            anchor = 'w')                            
                            ans.place(x=500,y=215)
                            q5_2.place(x=500,y=185)
                            p.config(text="Progress: 5/7") 
                            store_drug_options()
                    for i in range(3):
                        yval = 70 + (30*(i))
                        buttons4[i] = tk.Radiobutton(gui_1,
                                                     text = buttons4_options[i],
                                                     variable = cancer_type_user,
                                                     width = 30,
                                                     font=('Imago',13),
                                                     command = store_cancer_type,
                                                     value = buttons4_options[i],
                                                     anchor = 'w')
                        buttons4[i].place(x=500,y=yval)
                    q4_1.place(x=500,y=30)
                    p.config(text="Progress: 3/7")       
                    
                if user_choice[2] == 'Brain':
                    def store_cancer_type():
                        user_cancer_type = 'Glioblastoma'
                        cancer_type_user_input.append(user_cancer_type)
                        user_choice.append(cancer_type_user_input)
                        print(user_choice)
                        #Q5
                        if user_choice[3][0] == 'Glioblastoma':
                            options ='Avastin'
                            def store_drug_options():
                                drug_user_input.append(options)
                                user_choice.append(drug_user_input)
                                print(user_choice)
                                drugoptions ='Kadcyla'
                                toptions = ['Metastatic, Prior Treatment','Recurrance Treatment','None']
                                def store_treament():
                                    option1 = treatment_user_1.get()
                                    option2 = treatment_user_2.get()
                                    if option2 ==1 and option1==2:
                                        user_choice[3].append('Metastatic, Prior Treatment')   
                                        user_choice[3].append('Recurrance Treatment')
                                        user_choice[4].append(drugoptions)   
                                    elif option1 ==1:
                                        user_choice[3].append('Metastatic, Prior Treatment')
                                        user_choice[4].append(drugoptions)
                                    elif option2 ==1:
                                        user_choice[3].append('Recurrance Treatment')
                                        user_choice[4].append(drugoptions)  

                                    print(user_choice)
                                    def store_show_month():
                                        user_month = month_user.get()
                                        user_choice.append(user_month)
                                        print(user_choice)
                                        def close_window():
                                            gui_1.destroy()
                                        def change_label():
                                            p.destroy()
                                            pfinal = tk.Label(gui_1,text="""Complete!""",width =30,font=('Imago',17,'bold'),anchor = 'w',fg='#0066CC')
                                            pfinal.place(x=400,y=775)
                                        change_label()
                                        close_window()
                                    btn6_1,btn6_2,btn6_3,btn6_4,btn6_5,btn6_6,btn6_7,btn6_8,btn6_9,btn6_10,btn6_11,btn6_12 = '','','','','','','','','','','',''
                                    bttn6 = [btn6_1,btn6_2,btn6_3,btn6_4,btn6_5,btn6_6,btn6_7,btn6_8,btn6_9,btn6_10,btn6_11,btn6_12]
                                    optionm = [("January"),("February"),("March"),("April"),("May"),("June"),("July"),("August"),("September"),("October"),("November"),("December")]
                                    array = [1,2,3,4,5,6,7,8,9,10,11,12]
                                    for i in range(6):
                                        yval = 430 + 30*(i)
                                        bttn6[i] = tk.Radiobutton(gui_1,
                                                                text = optionm[i],
                                                                variable = month_user,
                                                                width = 15,
                                                                font=('Imago',13),
                                                                command = store_show_month,
                                                                value = array[i],
                                                                anchor = 'w')
                                        bttn6[i].place(x=500,y=yval)
                                    for i in range(6):
                                        yval = 430 + 30*(i)
                                        bttn6[i] = tk.Radiobutton(gui_1,
                                                                text = optionm[i+6],
                                                                variable = month_user,
                                                                width = 15,
                                                                font=('Imago',13),
                                                                command = store_show_month,
                                                                value = array[i+6],
                                                                anchor = 'w')
                                        bttn6[i].place(x=700,y=yval)
                                    q7.place(x=500,y=400)
                                    p.config(text = "Progress: 6/7")                                
                                btn1 = tk.Checkbutton(gui_1, text=toptions[0], variable=treatment_user_1, width = 30,font=('Imago',13),anchor ='w')
                                btn1.place(x=500,y=230)
                                btn2 = tk.Checkbutton(gui_1, text=toptions[1], variable=treatment_user_2, width = 30,font=('Imago',13),anchor ='w')
                                btn2.place(x=500,y=260)  
                                btn3 = tk.Checkbutton(gui_1, text=toptions[2], width = 20,font=('Imago',13),anchor ='w')
                                btn3.place(x=500,y=290) 
                                enter = tk.Button(gui_1, text='Select Treatment', font=('Imago',13), command = store_treament)
                                enter.place(x=500,y=330)
                                q6.place(x=500,y=200)
                                p.config(text="Progress: 5/7")
                            #Q6 INSERT HERE
                            ans = tk.Label(gui_1,
                                           text = options,
                                           font=('Imago',13),
                                           anchor = 'w')
                            ans.place(x=500,y=135)
                            q5_2.place(x=500,y=115)
                            p.config(text="Progress: 5/7") 
                            store_drug_options()
                    q4_2.place(x=500,y=30)
                    ans = tk.Label(gui_1,
                                   text = 'Glioblastoma',
                                   font=('Imago',13),
                                   anchor = 'w')
                    ans.place(x=500,y=55)
                    p.config(text="Progress: 3/6")
                    store_cancer_type()
                    
                if user_choice[2] == 'Breast':
                    btn4_1,btn4_2 = '',''
                    buttons4 = [btn4_1,btn4_2]
                    buttons4_options = ["Breast, HER2 Positive","Breast, Metastatic"]
                    def store_cancer_type():
                        user_cancer_type = cancer_type_user.get()
                        cancer_type_user_input.append(user_cancer_type)
                        user_choice.append(cancer_type_user_input)
                        print(user_choice)
                        if user_choice[3][0] == 'Breast, HER2 Positive':
                            options ='Perjeta'
                            def store_drug_options():
                                drug_user_input.append(options)
                                user_choice.append(drug_user_input)
                                print(user_choice)
                                drugoptions ='Kadcyla'
                                toptions = ['Metastatic, Prior Treatment','Recurrance Treatment','None']
                                def store_treament():
                                    option1 = treatment_user_1.get()
                                    option2 = treatment_user_2.get()
                                    if option2 ==1 and option1==2:
                                        user_choice[3].append('Metastatic, Prior Treatment')   
                                        user_choice[3].append('Recurrance Treatment')
                                        user_choice[4].append(drugoptions)   
                                    elif option1 ==1:
                                        user_choice[3].append('Metastatic, Prior Treatment')
                                        user_choice[4].append(drugoptions)
                                    elif option2 ==1:
                                        user_choice[3].append('Recurrance Treatment')
                                        user_choice[4].append(drugoptions)  
                                    print(user_choice)
                                    def store_show_month():
                                        user_month = month_user.get()
                                        user_choice.append(user_month)
                                        print(user_choice)
                                        def close_window():
                                            gui_1.destroy()
                                        def change_label():
                                            p.destroy()
                                            pfinal = tk.Label(gui_1,text="""Complete!""",width =30,font=('Imago',17,'bold'),anchor = 'w',fg='#0066CC')
                                            pfinal.place(x=400,y=775)
                                        change_label()
                                        close_window()
                                    btn6_1,btn6_2,btn6_3,btn6_4,btn6_5,btn6_6,btn6_7,btn6_8,btn6_9,btn6_10,btn6_11,btn6_12 = '','','','','','','','','','','',''
                                    bttn6 = [btn6_1,btn6_2,btn6_3,btn6_4,btn6_5,btn6_6,btn6_7,btn6_8,btn6_9,btn6_10,btn6_11,btn6_12]
                                    optionm = [("January"),("February"),("March"),("April"),("May"),("June"),("July"),("August"),("September"),("October"),("November"),("December")]
                                    array = [1,2,3,4,5,6,7,8,9,10,11,12]
                                    for i in range(6):
                                        yval = 450 + 30*(i)
                                        bttn6[i] = tk.Radiobutton(gui_1,
                                                                text = optionm[i],
                                                                variable = month_user,
                                                                width = 15,
                                                                font=('Imago',13),
                                                                command = store_show_month,
                                                                value = array[i],
                                                                anchor = 'w')
                                        bttn6[i].place(x=500,y=yval)
                                    for i in range(6):
                                        yval = 450 + 30*(i)
                                        bttn6[i] = tk.Radiobutton(gui_1,
                                                                text = optionm[i+6],
                                                                variable = month_user,
                                                                width = 15,
                                                                font=('Imago',13),
                                                                command = store_show_month,
                                                                value = array[i+6],
                                                                anchor = 'w')
                                        bttn6[i].place(x=700,y=yval)
                                    q7.place(x=500,y=420)
                                    p.config(text = "Progress: 6/7") 
                                btn1 = tk.Checkbutton(gui_1, text=toptions[0], variable=treatment_user_1, width = 30,font=('Imago',13),anchor ='w')
                                btn1.place(x=500,y=250)
                                btn2 = tk.Checkbutton(gui_1, text=toptions[1], variable=treatment_user_2, width = 30,font=('Imago',13),anchor ='w')
                                btn2.place(x=500,y=280)  
                                btn3 = tk.Checkbutton(gui_1, text=toptions[2], width = 20,font=('Imago',13),anchor ='w')
                                btn3.place(x=500,y=310) 
                                enter = tk.Button(gui_1, text='Select Treatment', font=('Imago',13), command = store_treament)
                                enter.place(x=500,y=340)
                                q6.place(x=500,y=220)
                                p.config(text="Progress: 5/7")                              
                            ans = tk.Label(gui_1,
                                           text = options,
                                           font=('Imago',13),
                                           anchor = 'w')
                            ans.place(x=500,y=170)
                            q5_2.place(x=500,y=150)
                            p.config(text="Progress: 5/7") 
                            store_drug_options()
                            
                        if user_choice[3][0] == 'Breast, Metastatic':
                            options = ['Avastin','Herceptin','Xeloda']
                            
                            def store_drug_options():
                                option1 = drug_1.get()
                                option2 = drug_2.get()
                                option3 = drug_3.get()
                                if option1 == 1:
                                    drug_user_input.append("Avastin")
                                if option2 == 1:
                                    drug_user_input.append("Herceptin")
                                if option3 == 1:
                                    drug_user_input.append('Xeloda')
                                user_choice.append(drug_user_input)
                                print(user_choice)
                                p.config(text="Progress: 5/7")   
                                drugoptions ='Kadcyla'
                                toptions = ['Metastatic, Prior Treatment','Recurrance Treatment','None']
                                def store_treament():
                                    option1 = treatment_user_1.get()
                                    option2 = treatment_user_2.get()
                                
                                    if option2 ==1 and option1==2:
                                        user_choice[3].append('Metastatic, Prior Treatment')   
                                        user_choice[3].append('Recurrance Treatment')
                                        user_choice[4].append(drugoptions)   
                                    elif option1 ==1:
                                        user_choice[3].append('Metastatic, Prior Treatment')
                                        user_choice[4].append(drugoptions)
                                    elif option2 ==1:
                                        user_choice[3].append('Recurrance Treatment')
                                        user_choice[4].append(drugoptions)  

                                    print(user_choice)
                                    def store_show_month():
                                        user_month = month_user.get()
                                        user_choice.append(user_month)
                                        print(user_choice)
                                        def close_window():
                                            gui_1.destroy()
                                        def change_label():
                                            p.destroy()
                                            pfinal = tk.Label(gui_1,text="""Complete!""",width =30,font=('Imago',17,'bold'),anchor = 'w',fg='#0066CC')
                                            pfinal.place(x=400,y=775)
                                        change_label()
                                        close_window()
    
                                    btn6_1,btn6_2,btn6_3,btn6_4,btn6_5,btn6_6,btn6_7,btn6_8,btn6_9,btn6_10,btn6_11,btn6_12 = '','','','','','','','','','','',''
                                    bttn6 = [btn6_1,btn6_2,btn6_3,btn6_4,btn6_5,btn6_6,btn6_7,btn6_8,btn6_9,btn6_10,btn6_11,btn6_12]
                                    optionm = [("January"),("February"),("March"),("April"),("May"),("June"),("July"),("August"),("September"),("October"),("November"),("December")]
                                    array = [1,2,3,4,5,6,7,8,9,10,11,12]
                                    for i in range(6):
                                        yval = 530 + 30*(i)
                                        bttn6[i] = tk.Radiobutton(gui_1,
                                                                text = optionm[i],
                                                                variable = month_user,
                                                                width = 15,
                                                                font=('Imago',13),
                                                                command = store_show_month,
                                                                value = array[i],
                                                                anchor = 'w')
                                        bttn6[i].place(x=500,y=yval)
                                    
                                    for i in range(6):
                                        yval = 530 + 30*(i)
                                        bttn6[i] = tk.Radiobutton(gui_1,
                                                                text = optionm[i+6],
                                                                variable = month_user,
                                                                width = 15,
                                                                font=('Imago',13),
                                                                command = store_show_month,
                                                                value = array[i+6],
                                                                anchor = 'w')
                                        bttn6[i].place(x=700,y=yval)
                                    q7.place(x=500,y=500)
                                    p.config(text = "Progress: 6/7")                                 
                                btn1 = tk.Checkbutton(gui_1, text=toptions[0], variable=treatment_user_1, width = 30,font=('Imago',13),anchor ='w')
                                btn1.place(x=500,y=355)
                                btn2 = tk.Checkbutton(gui_1, text=toptions[1], variable=treatment_user_2, width = 30,font=('Imago',13),anchor ='w')
                                btn2.place(x=500,y=385)  
                                btn3 = tk.Checkbutton(gui_1, text=toptions[2], width = 20,font=('Imago',13),anchor ='w')
                                btn3.place(x=500,y=415) 
                                enter = tk.Button(gui_1, text='Select Treatment', font=('Imago',13), command = store_treament)
                                enter.place(x=500,y=445)
                                q6.place(x=500,y=325)
                                p.config(text="Progress: 5/7")                              
                            
                            btn1 = tk.Checkbutton(gui_1, text=options[0], variable=drug_1, width = 20,font=('Imago',13),anchor ='w')
                            btn1.place(x=500,y=180)
                            btn2 = tk.Checkbutton(gui_1, text=options[1], variable=drug_2, width = 20,font=('Imago',13),anchor ='w')
                            btn2.place(x=500,y=210)
                            btn3 = tk.Checkbutton(gui_1, text=options[2], variable=drug_3, width = 20,font=('Imago',13),anchor ='w')
                            btn3.place(x=500,y=240)    
                            enter = tk.Button(gui_1, text='Select Drug', font=('Imago',13), command = store_drug_options)
                            enter.place(x=500,y=270)
                            q5_1.place(x=500,y=150)
                            p.config(text="Progress: 4/7")                    
                                        
                        
                    for i in range(2):
                        yval = 70 + (30*(i))
                        buttons4[i] = tk.Radiobutton(gui_1,
                                                     text = buttons4_options[i],
                                                     variable = cancer_type_user,
                                                     width = 35,
                                                     font=('Imago',13),
                                                     command = store_cancer_type,
                                                     value = buttons4_options[i],
                                                     anchor = 'w')
                        buttons4[i].place(x=500,y=yval)
                    q4_1.place(x=500,y=30)
                    p.config(text="Progress: 3/7")
                    
                if user_choice[2] == 'Colorectal':
                    btn4_1,btn4_2 = '',''
                    buttons4 = [btn4_1,btn4_2]
                    buttons4_options = ["Colon, Metastatic","Colon"]
                        
                    def store_cancer_type():
                        user_cancer_type = cancer_type_user.get()
                        cancer_type_user_input.append(user_cancer_type)
                        user_choice.append(cancer_type_user_input)
                        print(user_choice)
                        #Q5
                        if user_choice[3][0] == 'Colon, Metastatic':
                            options ='Avastin'
                            
                            def store_drug_options():
                                drug_user_input.append(options)
                                user_choice.append(drug_user_input)
                                print(user_choice)
                                drugoptions ='Kadcyla'
                                toptions = ['Metastatic, Prior Treatment','Recurrance Treatment','None']
                                def store_treament():
                                    option1 = treatment_user_1.get()
                                    option2 = treatment_user_2.get()
                                    if option2 ==1 and option1==2:
                                        user_choice[3].append('Metastatic, Prior Treatment')   
                                        user_choice[3].append('Recurrance Treatment')
                                        user_choice[4].append(drugoptions)   
                                    elif option1 ==1:
                                        user_choice[3].append('Metastatic, Prior Treatment')
                                        user_choice[4].append(drugoptions)
                                    elif option2 ==1:
                                        user_choice[3].append('Recurrance Treatment')
                                        user_choice[4].append(drugoptions)  

                                    print(user_choice)
                                    def store_show_month():
                                        user_month = month_user.get()
                                        user_choice.append(user_month)
                                        print(user_choice)
                                        def close_window():
                                            gui_1.destroy()
                                        def change_label():
                                            p.destroy()
                                            pfinal = tk.Label(gui_1,text="""Complete!""",width =30,font=('Imago',17,'bold'),anchor = 'w',fg='#0066CC')
                                            pfinal.place(x=400,y=775)
                                        change_label()
                                        close_window()
    
                                    btn6_1,btn6_2,btn6_3,btn6_4,btn6_5,btn6_6,btn6_7,btn6_8,btn6_9,btn6_10,btn6_11,btn6_12 = '','','','','','','','','','','',''
                                    bttn6 = [btn6_1,btn6_2,btn6_3,btn6_4,btn6_5,btn6_6,btn6_7,btn6_8,btn6_9,btn6_10,btn6_11,btn6_12]
                                    optionm = [("January"),("February"),("March"),("April"),("May"),("June"),("July"),("August"),("September"),("October"),("November"),("December")]
                                    array = [1,2,3,4,5,6,7,8,9,10,11,12]
                                    for i in range(6):
                                        yval = 440 + 30*(i)
                                        bttn6[i] = tk.Radiobutton(gui_1,
                                                                text = optionm[i],
                                                                variable = month_user,
                                                                width = 15,
                                                                font=('Imago',13),
                                                                command = store_show_month,
                                                                value = array[i],
                                                                anchor = 'w')
                                        bttn6[i].place(x=500,y=yval)
                                    
                                    for i in range(6):
                                        yval = 440 + 30*(i)
                                        bttn6[i] = tk.Radiobutton(gui_1,
                                                                text = optionm[i+6],
                                                                variable = month_user,
                                                                width = 15,
                                                                font=('Imago',13),
                                                                command = store_show_month,
                                                                value = array[i+6],
                                                                anchor = 'w')
                                        bttn6[i].place(x=700,y=yval)
                                    q6.place(x=500,y=410)
                                    p.config(text = "Progress: 6/7")                                 
                                btn1 = tk.Checkbutton(gui_1, text=toptions[0], variable=treatment_user_1, width = 30,font=('Imago',13),anchor ='w')
                                btn1.place(x=500,y=250)
                                btn2 = tk.Checkbutton(gui_1, text=toptions[1], variable=treatment_user_2, width = 30,font=('Imago',13),anchor ='w')
                                btn2.place(x=500,y=280)  
                                btn3 = tk.Checkbutton(gui_1, text=toptions[2], width = 20,font=('Imago',13),anchor ='w')
                                btn3.place(x=500,y=310) 
                                enter = tk.Button(gui_1, text='Select Treatment', font=('Imago',13), command = store_treament)
                                enter.place(x=500,y=340)
                                q7.place(x=500,y=220)
                                p.config(text="Progress: 5/7")                               
                            #Q6 INSERT HERE
                            ans = tk.Label(gui_1,
                                           text = options,
                                           font=('Imago',13),
                                           anchor = 'w')
                            ans.place(x=500,y=180)
                            q5_2.place(x=500,y=150)
                            p.config(text="Progress: 5/7") 
                            store_drug_options()
                        if user_choice[3][0] == 'Colon':
                            options ='Xeloda'
                            def store_drug_options():
                                drug_user_input.append(options)
                                user_choice.append(drug_user_input)
                                print(user_choice)
                                drugoptions ='Kadcyla'
                                toptions = ['Metastatic, Prior Treatment','Recurrance Treatment','None']
                                def store_treament():
                                    option1 = treatment_user_1.get()
                                    option2 = treatment_user_2.get()
                                
                                    if option2 ==1 and option1==2:
                                        user_choice[3].append('Metastatic, Prior Treatment')   
                                        user_choice[3].append('Recurrance Treatment')
                                        user_choice[4].append(drugoptions)   
                                    elif option1 ==1:
                                        user_choice[3].append('Metastatic, Prior Treatment')
                                        user_choice[4].append(drugoptions)
                                    elif option2 ==1:
                                        user_choice[3].append('Recurrance Treatment')
                                        user_choice[4].append(drugoptions)  

                                    print(user_choice)
                                    def store_show_month():
                                        user_month = month_user.get()
                                        user_choice.append(user_month)
                                        print(user_choice)
                                        def close_window():
                                            gui_1.destroy()
                                        def change_label():
                                            p.destroy()
                                            pfinal = tk.Label(gui_1,text="""Complete!""",width =30,font=('Imago',17,'bold'),anchor = 'w',fg='#0066CC')
                                            pfinal.place(x=400,y=775)
                                        change_label()
                                        close_window()
    
                                    btn6_1,btn6_2,btn6_3,btn6_4,btn6_5,btn6_6,btn6_7,btn6_8,btn6_9,btn6_10,btn6_11,btn6_12 = '','','','','','','','','','','',''
                                    bttn6 = [btn6_1,btn6_2,btn6_3,btn6_4,btn6_5,btn6_6,btn6_7,btn6_8,btn6_9,btn6_10,btn6_11,btn6_12]
                                    optionm = [("January"),("February"),("March"),("April"),("May"),("June"),("July"),("August"),("September"),("October"),("November"),("December")]
                                    array = [1,2,3,4,5,6,7,8,9,10,11,12]
                                    for i in range(6):
                                        yval = 440 + 30*(i)
                                        bttn6[i] = tk.Radiobutton(gui_1,
                                                                text = optionm[i],
                                                                variable = month_user,
                                                                width = 15,
                                                                font=('Imago',13),
                                                                command = store_show_month,
                                                                value = array[i],
                                                                anchor = 'w')
                                        bttn6[i].place(x=500,y=yval) 
                                    for i in range(6):
                                        yval = 440 + 30*(i)
                                        bttn6[i] = tk.Radiobutton(gui_1,
                                                                text = optionm[i+6],
                                                                variable = month_user,
                                                                width = 15,
                                                                font=('Imago',13),
                                                                command = store_show_month,
                                                                value = array[i+6],
                                                                anchor = 'w')
                                        bttn6[i].place(x=700,y=yval)
                                    q7.place(x=500,y=410)
                                    p.config(text = "Progress: 6/7")                                 
                                btn1 = tk.Checkbutton(gui_1, text=toptions[0], variable=treatment_user_1, width = 30,font=('Imago',13),anchor ='w')
                                btn1.place(x=500,y=250)
                                btn2 = tk.Checkbutton(gui_1, text=toptions[1], variable=treatment_user_2, width = 30,font=('Imago',13),anchor ='w')
                                btn2.place(x=500,y=280)  
                                btn3 = tk.Checkbutton(gui_1, text=toptions[2], width = 20,font=('Imago',13),anchor ='w')
                                btn3.place(x=500,y=310) 
                                enter = tk.Button(gui_1, text='Select Treatment', font=('Imago',13), command = store_treament)
                                enter.place(x=500,y=340)
                                q6.place(x=500,y=220)
                                p.config(text="Progress: 5/7")                                 
                            #Q6 INSERT HERE
                            ans = tk.Label(gui_1,
                                           text = options,
                                           font=('Imago',13),
                                           anchor = 'w')
                            ans.place(x=500,y=180)
                            q5_2.place(x=500,y=150)
                            p.config(text="Progress: 5/7") 
                            store_drug_options()              
                            
                    for i in range(2):
                        yval = 70 + (30*(i))
                        buttons4[i] = tk.Radiobutton(gui_1,
                                                     text = buttons4_options[i],
                                                     variable = cancer_type_user,
                                                     width = 35,
                                                     font=('Imago',13),
                                                     command = store_cancer_type,
                                                     value = buttons4_options[i],
                                                     anchor = 'w')
                        buttons4[i].place(x=500,y=yval)
                    q4_1.place(x=500,y=30)
                    p.config(text="Progress: 3/7")
                
                if user_choice[2] == 'Esophagus':
                    def store_cancer_type():
                        user_cancer_type = 'Esophagal'
                        cancer_type_user_input.append(user_cancer_type)
                        user_choice.append(cancer_type_user_input)
                        print(user_choice)
    
                        if user_choice[3][0] == 'Esophagal':
                            options ='Xeloda'
                            
                        def store_drug_options():
                            drug_user_input.append(options)
                            user_choice.append(drug_user_input)
                            print(user_choice)
                            drugoptions ='Kadcyla'
                            toptions = ['Metastatic, Prior Treatment','Recurrance Treatment','None']
                            def store_treament():
                                option1 = treatment_user_1.get()
                                option2 = treatment_user_2.get()
                                if option2 ==1 and option1==2:
                                    user_choice[3].append('Metastatic, Prior Treatment')   
                                    user_choice[3].append('Recurrance Treatment')
                                    user_choice[4].append(drugoptions)   
                                elif option1 ==1:
                                    user_choice[3].append('Metastatic, Prior Treatment')
                                    user_choice[4].append(drugoptions)
                                elif option2 ==1:
                                    user_choice[3].append('Recurrance Treatment')
                                    user_choice[4].append(drugoptions)    
  
                                print(user_choice)
                                def store_show_month():
                                    user_month = month_user.get()
                                    user_choice.append(user_month)
                                    print(user_choice)
                                    def close_window():
                                        gui_1.destroy()
                                    def change_label():
                                        p.destroy()
                                        pfinal = tk.Label(gui_1,text="""Complete!""",width =30,font=('Imago',17,'bold'),anchor = 'w',fg='#0066CC')
                                        pfinal.place(x=400,y=775)
                                    change_label()
                                    close_window()
    
                                btn6_1,btn6_2,btn6_3,btn6_4,btn6_5,btn6_6,btn6_7,btn6_8,btn6_9,btn6_10,btn6_11,btn6_12 = '','','','','','','','','','','',''
                                bttn6 = [btn6_1,btn6_2,btn6_3,btn6_4,btn6_5,btn6_6,btn6_7,btn6_8,btn6_9,btn6_10,btn6_11,btn6_12]
                                optionm = [("January"),("February"),("March"),("April"),("May"),("June"),("July"),("August"),("September"),("October"),("November"),("December")]
                                array = [1,2,3,4,5,6,7,8,9,10,11,12]
                                for i in range(6):
                                    yval = 410 + 30*(i)
                                    bttn6[i] = tk.Radiobutton(gui_1,
                                                            text = optionm[i],
                                                            variable = month_user,
                                                            width = 15,
                                                            font=('Imago',13),
                                                            command = store_show_month,
                                                            value = array[i],
                                                            anchor = 'w')
                                    bttn6[i].place(x=500,y=yval)
                                
                                for i in range(6):
                                    yval = 410 + 30*(i)
                                    bttn6[i] = tk.Radiobutton(gui_1,
                                                            text = optionm[i+6],
                                                            variable = month_user,
                                                            width = 15,
                                                            font=('Imago',13),
                                                            command = store_show_month,
                                                            value = array[i+6],
                                                            anchor = 'w')
                                    bttn6[i].place(x=700,y=yval)
                                q7.place(x=500,y=380)
                                p.config(text = "Progress: 6/7")                             
                            btn1 = tk.Checkbutton(gui_1, text=toptions[0], variable=treatment_user_1, width = 30,font=('Imago',13),anchor ='w')
                            btn1.place(x=500,y=215)
                            btn2 = tk.Checkbutton(gui_1, text=toptions[1], variable=treatment_user_2, width = 30,font=('Imago',13),anchor ='w')
                            btn2.place(x=500,y=245)  
                            btn3 = tk.Checkbutton(gui_1, text=toptions[2], width = 20,font=('Imago',13),anchor ='w')
                            btn3.place(x=500,y=275) 
                            enter = tk.Button(gui_1, text='Select Treatment', font=('Imago',13), command = store_treament)
                            enter.place(x=500,y=310)
                            q6.place(x=500,y=185)
                            p.config(text="Progress: 5/7")                         
                        #Q6 INSERT HERE
                        ans = tk.Label(gui_1,
                                       text = options,
                                       font=('Imago',13),
                                       anchor = 'w')
                        ans.place(x=500,y=135)
                        q5_2.place(x=500,y=115)
                        p.config(text="Progress: 5/7") 
                        store_drug_options()  
                                       
                    q4_2.place(x=500,y=30)
                    ans = tk.Label(gui_1,
                                   text = 'Esophagal',
                                   font=('Imago',13),
                                   anchor = 'w')
                    ans.place(x=500,y=55)
                    p.config(text="Progress: 3/7")
                    store_cancer_type()
                
                if user_choice[2] == 'Kidney':
                    def store_cancer_type():
                        user_cancer_type = 'Renal Cell Carcinoma, Metastatic'
                        cancer_type_user_input.append(user_cancer_type)
                        user_choice.append(cancer_type_user_input)
                        print(user_choice)
                    #Q5
                        if user_choice[3][0] == 'Renal Cell Carcinoma, Metastatic':
                            options ='Avastin'
                            
                            def store_drug_options():
                                drug_user_input.append(options)
                                user_choice.append(drug_user_input)
                                print(user_choice)
                                drugoptions ='Kadcyla'
                                toptions = ['Metastatic, Prior Treatment','Recurrance Treatment','None']
                                def store_treament():
                                    option1 = treatment_user_1.get()
                                    option2 = treatment_user_2.get()
                                
                                    if option2 ==1 and option1==2:
                                        user_choice[3].append('Metastatic, Prior Treatment')   
                                        user_choice[3].append('Recurrance Treatment')
                                        user_choice[4].append(drugoptions)   
                                    elif option1 ==1:
                                        user_choice[3].append('Metastatic, Prior Treatment')
                                        user_choice[4].append(drugoptions)
                                    elif option2 ==1:
                                        user_choice[3].append('Recurrance Treatment')
                                        user_choice[4].append(drugoptions)  

                                    print(user_choice)
                                    def store_show_month():
                                        user_month = month_user.get()
                                        user_choice.append(user_month)
                                        print(user_choice)
                                        def close_window():
                                            gui_1.destroy()
                                        def change_label():
                                            p.destroy()
                                            pfinal = tk.Label(gui_1,text="""Complete!""",width =30,font=('Imago',17,'bold'),anchor = 'w',fg='#0066CC')
                                            pfinal.place(x=400,y=775)
                                        change_label()
                                        close_window()
    
                                    btn6_1,btn6_2,btn6_3,btn6_4,btn6_5,btn6_6,btn6_7,btn6_8,btn6_9,btn6_10,btn6_11,btn6_12 = '','','','','','','','','','','',''
                                    bttn6 = [btn6_1,btn6_2,btn6_3,btn6_4,btn6_5,btn6_6,btn6_7,btn6_8,btn6_9,btn6_10,btn6_11,btn6_12]
                                    optionm = [("January"),("February"),("March"),("April"),("May"),("June"),("July"),("August"),("September"),("October"),("November"),("December")]
                                    array = [1,2,3,4,5,6,7,8,9,10,11,12]
                                    for i in range(6):
                                        yval = 405 + 30*(i)
                                        bttn6[i] = tk.Radiobutton(gui_1,
                                                                text = optionm[i],
                                                                variable = month_user,
                                                                width = 15,
                                                                font=('Imago',13),
                                                                command = store_show_month,
                                                                value = array[i],
                                                                anchor = 'w')
                                        bttn6[i].place(x=500,y=yval)
                                    
                                    for i in range(6):
                                        yval = 405 + 30*(i)
                                        bttn6[i] = tk.Radiobutton(gui_1,
                                                                text = optionm[i+6],
                                                                variable = month_user,
                                                                width = 15,
                                                                font=('Imago',13),
                                                                command = store_show_month,
                                                                value = array[i+6],
                                                                anchor = 'w')
                                        bttn6[i].place(x=700,y=yval)
                                    q7.place(x=500,y=375)
                                    p.config(text = "Progress: 6/7")                                 
                                btn1 = tk.Checkbutton(gui_1, text=toptions[0], variable=treatment_user_1, width = 30,font=('Imago',13),anchor ='w')
                                btn1.place(x=500,y=220)
                                btn2 = tk.Checkbutton(gui_1, text=toptions[1], variable=treatment_user_2, width = 30,font=('Imago',13),anchor ='w')
                                btn2.place(x=500,y=250)  
                                btn3 = tk.Checkbutton(gui_1, text=toptions[2], width = 20,font=('Imago',13),anchor ='w')
                                btn3.place(x=500,y=280) 
                                enter = tk.Button(gui_1, text='Select Treatment', font=('Imago',13), command = store_treament)
                                enter.place(x=500,y=310)
                                q6.place(x=500,y=190)
                                p.config(text="Progress: 5/7")                               
                            #Q6 INSERT HERE
                            ans = tk.Label(gui_1,
                                           text = options,
                                           font=('Imago',13),
                                           anchor = 'w')
                            ans.place(x=500,y=140)
                            q5_2.place(x=500,y=115)
                            p.config(text="Progress: 5/7") 
                            store_drug_options()   
                            
                    q4_2.place(x=500,y=30)
                    ans = tk.Label(gui_1,
                                   text = 'Renal Cell Carcinoma, Metastatic',
                                   font=('Imago',13),
                                   anchor = 'w')
                    ans.place(x=500,y=55)
                    p.config(text="Progress: 3/7")
                    store_cancer_type()
                
                if user_choice[2] == 'Liver':
                    def store_cancer_type():
                        user_cancer_type = 'Hepatobiliary'
                        cancer_type_user_input.append(user_cancer_type)
                        user_choice.append(cancer_type_user_input)
                        print(user_choice)
                    #Q5
                        if user_choice[3][0] == 'Hepatobiliary':
                            options ='Xeloda'
                            
                            def store_drug_options():
                                drug_user_input.append(options)
                                user_choice.append(drug_user_input)
                                print(user_choice)
                                drugoptions ='Kadcyla'
                                toptions = ['Metastatic, Prior Treatment','Recurrance Treatment','None']
                                def store_treament():
                                    option1 = treatment_user_1.get()
                                    option2 = treatment_user_2.get()
                                
                                    if option2 ==1 and option1==2:
                                        user_choice[3].append('Metastatic, Prior Treatment')   
                                        user_choice[3].append('Recurrance Treatment')
                                        user_choice[4].append(drugoptions)   
                                    elif option1 ==1:
                                        user_choice[3].append('Metastatic, Prior Treatment')
                                        user_choice[4].append(drugoptions)
                                    elif option2 ==1:
                                        user_choice[3].append('Recurrance Treatment')
                                        user_choice[4].append(drugoptions)  

                                    print(user_choice)
                                    def store_show_month():
                                        user_month = month_user.get()
                                        user_choice.append(user_month)
                                        print(user_choice)
                                        def close_window():
                                            gui_1.destroy()
                                        def change_label():
                                            p.destroy()
                                            pfinal = tk.Label(gui_1,text="""Complete!""",width =30,font=('Imago',17,'bold'),anchor = 'w',fg='#0066CC')
                                            pfinal.place(x=400,y=775)
                                        change_label()
                                        close_window()
    
                                    btn6_1,btn6_2,btn6_3,btn6_4,btn6_5,btn6_6,btn6_7,btn6_8,btn6_9,btn6_10,btn6_11,btn6_12 = '','','','','','','','','','','',''
                                    bttn6 = [btn6_1,btn6_2,btn6_3,btn6_4,btn6_5,btn6_6,btn6_7,btn6_8,btn6_9,btn6_10,btn6_11,btn6_12]
                                    optionm = [("January"),("February"),("March"),("April"),("May"),("June"),("July"),("August"),("September"),("October"),("November"),("December")]
                                    array = [1,2,3,4,5,6,7,8,9,10,11,12]
                                    for i in range(6):
                                        yval = 410 + 30*(i)
                                        bttn6[i] = tk.Radiobutton(gui_1,
                                                                text = optionm[i],
                                                                variable = month_user,
                                                                width = 15,
                                                                font=('Imago',13),
                                                                command = store_show_month,
                                                                value = array[i],
                                                                anchor = 'w')
                                        bttn6[i].place(x=500,y=yval)
                                    
                                    for i in range(6):
                                        yval = 410 + 30*(i)
                                        bttn6[i] = tk.Radiobutton(gui_1,
                                                                text = optionm[i+6],
                                                                variable = month_user,
                                                                width = 15,
                                                                font=('Imago',13),
                                                                command = store_show_month,
                                                                value = array[i+6],
                                                                anchor = 'w')
                                        bttn6[i].place(x=700,y=yval)
                                    q7.place(x=500,y=380)
                                    p.config(text = "Progress: 6/7")                                 
                                btn1 = tk.Checkbutton(gui_1, text=toptions[0], variable=treatment_user_1, width = 30,font=('Imago',13),anchor ='w')
                                btn1.place(x=500,y=220)
                                btn2 = tk.Checkbutton(gui_1, text=toptions[1], variable=treatment_user_2, width = 30,font=('Imago',13),anchor ='w')
                                btn2.place(x=500,y=250)  
                                btn3 = tk.Checkbutton(gui_1, text=toptions[2], width = 20,font=('Imago',13),anchor ='w')
                                btn3.place(x=500,y=280) 
                                enter = tk.Button(gui_1, text='Select Treatment', font=('Imago',13), command = store_treament)
                                enter.place(x=500,y=320)
                                q6.place(x=500,y=190)
                                p.config(text="Progress: 5/7")                              
                            #Q6 INSERT HERE
                            ans = tk.Label(gui_1,
                                           text = options,
                                           font=('Imago',13),
                                           anchor = 'w')
                            ans.place(x=500,y=135)
                            q5_2.place(x=500,y=115)
                            p.config(text="Progress: 5/7") 
                            store_drug_options()  
                            
                    q4_2.place(x=500,y=30)
                    ans = tk.Label(gui_1,
                                   text = 'Hepatobiliary',
                                   font=('Imago',13),
                                   anchor = 'w')
                    ans.place(x=500,y=55)
                    p.config(text="Progress: 3/7")
                    store_cancer_type()
                
                if user_choice[2] == 'Lungs':
                    btn4_1,btn4_2 = '',''
                    buttons4 = [btn4_1,btn4_2]
                    buttons4_options = ["Lung, Non-Small, Metastatic","Lung, Non-Small, Non-Squamous"]
                        
                    def store_cancer_type():
                        user_cancer_type = cancer_type_user.get()
                        cancer_type_user_input.append(user_cancer_type)
                        user_choice.append(cancer_type_user_input)
                        print(user_choice)
                    #Q5
                        if user_choice[3][0] == 'Lung, Non-Small, Metastatic':
                            options ='Tarceva'
                            
                            def store_drug_options():
                                drug_user_input.append(options)
                                user_choice.append(drug_user_input)
                                print(user_choice)
                                drugoptions ='Kadcyla'
                                toptions = ['Metastatic, Prior Treatment','Recurrance Treatment','None']
                                def store_treament():
                                    option1 = treatment_user_1.get()
                                    option2 = treatment_user_2.get()
                                
                                    if option2 ==1 and option1==2:
                                        user_choice[3].append('Metastatic, Prior Treatment')   
                                        user_choice[3].append('Recurrance Treatment')
                                        user_choice[4].append(drugoptions)   
                                    elif option1 ==1:
                                        user_choice[3].append('Metastatic, Prior Treatment')
                                        user_choice[4].append(drugoptions)
                                    elif option2 ==1:
                                        user_choice[3].append('Recurrance Treatment')
                                        user_choice[4].append(drugoptions)  

                                    print(user_choice)
                                    def store_show_month():
                                        user_month = month_user.get()
                                        user_choice.append(user_month)
                                        print(user_choice)
                                        def close_window():
                                            gui_1.destroy()
                                        def change_label():
                                            p.destroy()
                                            pfinal = tk.Label(gui_1,text="""Complete!""",width =30,font=('Imago',17,'bold'),anchor = 'w',fg='#0066CC')
                                            pfinal.place(x=400,y=775)
                                        change_label()
                                        close_window()
    
                                    btn6_1,btn6_2,btn6_3,btn6_4,btn6_5,btn6_6,btn6_7,btn6_8,btn6_9,btn6_10,btn6_11,btn6_12 = '','','','','','','','','','','',''
                                    bttn6 = [btn6_1,btn6_2,btn6_3,btn6_4,btn6_5,btn6_6,btn6_7,btn6_8,btn6_9,btn6_10,btn6_11,btn6_12]
                                    optionm = [("January"),("February"),("March"),("April"),("May"),("June"),("July"),("August"),("September"),("October"),("November"),("December")]
                                    array = [1,2,3,4,5,6,7,8,9,10,11,12]
                                    for i in range(6):
                                        yval = 475 + 30*(i)
                                        bttn6[i] = tk.Radiobutton(gui_1,
                                                                text = optionm[i],
                                                                variable = month_user,
                                                                width = 15,
                                                                font=('Imago',13),
                                                                command = store_show_month,
                                                                value = array[i],
                                                                anchor = 'w')
                                        bttn6[i].place(x=500,y=yval)
                                    
                                    for i in range(6):
                                        yval = 475 + 30*(i)
                                        bttn6[i] = tk.Radiobutton(gui_1,
                                                                text = optionm[i+6],
                                                                variable = month_user,
                                                                width = 15,
                                                                font=('Imago',13),
                                                                command = store_show_month,
                                                                value = array[i+6],
                                                                anchor = 'w')
                                        bttn6[i].place(x=700,y=yval)
                                    q7.place(x=475,y=445)
                                    p.config(text = "Progress: 6/7")                                 
                                btn1 = tk.Checkbutton(gui_1, text=toptions[0], variable=treatment_user_1, width = 30,font=('Imago',13),anchor ='w')
                                btn1.place(x=500,y=280)
                                btn2 = tk.Checkbutton(gui_1, text=toptions[1], variable=treatment_user_2, width = 30,font=('Imago',13),anchor ='w')
                                btn2.place(x=500,y=310)  
                                btn3 = tk.Checkbutton(gui_1, text=toptions[2], width = 20,font=('Imago',13),anchor ='w')
                                btn3.place(x=500,y=340) 
                                enter = tk.Button(gui_1, text='Select Treatment', font=('Imago',13), command = store_treament)
                                enter.place(x=500,y=380)
                                q6.place(x=500,y=250)
                                p.config(text="Progress: 5/7")                             
                            #Q6 INSERT HERE
                            ans = tk.Label(gui_1,
                                           text = options,
                                           font=('Imago',13),
                                           anchor = 'w')
                            ans.place(x=500,y=185)
                            q5_2.place(x=500,y=155)
                            p.config(text="Progress: 5/7") 
                            store_drug_options()  
                            
                        if user_choice[3][0] == 'Lung, Non-Small, Non-Squamous':
                            options ='Avastin'
                            
                            def store_drug_options():
                                drug_user_input.append(options)
                                user_choice.append(drug_user_input)
                                print(user_choice)
                                drugoptions ='Kadcyla'
                                toptions = ['Metastatic, Prior Treatment','Recurrance Treatment','None']
                                def store_treament():
                                    option1 = treatment_user_1.get()
                                    option2 = treatment_user_2.get()
                                
                                    if option2 ==1 and option1==2:
                                        user_choice[3].append('Metastatic, Prior Treatment')   
                                        user_choice[3].append('Recurrance Treatment')
                                        user_choice[4].append(drugoptions)   
                                    elif option1 ==1:
                                        user_choice[3].append('Metastatic, Prior Treatment')
                                        user_choice[4].append(drugoptions)
                                    elif option2 ==1:
                                        user_choice[3].append('Recurrance Treatment')
                                        user_choice[4].append(drugoptions)  
  
                                    print(user_choice)
                                    def store_show_month():
                                        user_month = month_user.get()
                                        user_choice.append(user_month)
                                        print(user_choice)
                                        def close_window():
                                            gui_1.destroy()
                                        def change_label():
                                            p.destroy()
                                            pfinal = tk.Label(gui_1,text="""Complete!""",width =30,font=('Imago',17,'bold'),anchor = 'w',fg='#0066CC')
                                            pfinal.place(x=400,y=775)
                                        change_label()
                                        close_window()
    
                                    btn6_1,btn6_2,btn6_3,btn6_4,btn6_5,btn6_6,btn6_7,btn6_8,btn6_9,btn6_10,btn6_11,btn6_12 = '','','','','','','','','','','',''
                                    bttn6 = [btn6_1,btn6_2,btn6_3,btn6_4,btn6_5,btn6_6,btn6_7,btn6_8,btn6_9,btn6_10,btn6_11,btn6_12]
                                    optionm = [("January"),("February"),("March"),("April"),("May"),("June"),("July"),("August"),("September"),("October"),("November"),("December")]
                                    array = [1,2,3,4,5,6,7,8,9,10,11,12]
                                    for i in range(6):
                                        yval = 455 + 30*(i)
                                        bttn6[i] = tk.Radiobutton(gui_1,
                                                                text = optionm[i],
                                                                variable = month_user,
                                                                width = 15,
                                                                font=('Imago',13),
                                                                command = store_show_month,
                                                                value = array[i],
                                                                anchor = 'w')
                                        bttn6[i].place(x=500,y=yval)
                                    
                                    for i in range(6):
                                        yval = 455 + 30*(i)
                                        bttn6[i] = tk.Radiobutton(gui_1,
                                                                text = optionm[i+6],
                                                                variable = month_user,
                                                                width = 15,
                                                                font=('Imago',13),
                                                                command = store_show_month,
                                                                value = array[i+6],
                                                                anchor = 'w')
                                        bttn6[i].place(x=700,y=yval)
                                    q7.place(x=500,y=435)
                                    p.config(text = "Progress: 6/7")                                 
                                btn1 = tk.Checkbutton(gui_1, text=toptions[0], variable=treatment_user_1, width = 30,font=('Imago',13),anchor ='w')
                                btn1.place(x=500,y=280)
                                btn2 = tk.Checkbutton(gui_1, text=toptions[1], variable=treatment_user_2, width = 30,font=('Imago',13),anchor ='w')
                                btn2.place(x=500,y=310)  
                                btn3 = tk.Checkbutton(gui_1, text=toptions[2], width = 20,font=('Imago',13),anchor ='w')
                                btn3.place(x=500,y=340) 
                                enter = tk.Button(gui_1, text='Select Treatment', font=('Imago',13), command = store_treament)
                                enter.place(x=500,y=370)
                                q6.place(x=500,y=250)
                                p.config(text="Progress: 5/7")                              
                            #Q6 INSERT HERE
                            ans = tk.Label(gui_1,
                                           text = options,
                                           font=('Imago',13),
                                           anchor = 'w')
                            ans.place(x=500,y=185)
                            q5_2.place(x=500,y=155)
                            p.config(text="Progress: 4/7") 
                            store_drug_options()                             
            
                    for i in range(2):
                        yval = 70 + (30*(i))
                        buttons4[i] = tk.Radiobutton(gui_1,
                                                     text = buttons4_options[i],
                                                     variable = cancer_type_user,
                                                     width = 35,
                                                     font=('Imago',13),
                                                     command = store_cancer_type,
                                                     value = buttons4_options[i],
                                                     anchor = 'w')
                        buttons4[i].place(x=500,y=yval)
                    q4_1.place(x=500,y=30)
                    p.config(text="Progress: 3/7")
                            
                if user_choice[2] == 'Ovary':
                    btn4_1,btn4_2 = '',''
                    buttons4 = [btn4_1,btn4_2]
                    buttons4_options = ["Fallopian Tube","Ovarian"]
                    def store_cancer_type():
                        user_cancer_type = cancer_type_user.get()
                        cancer_type_user_input.append(user_cancer_type)
                        user_choice.append(cancer_type_user_input)
                        print(user_choice)
                        if user_choice[2] == 'Ovary':
                            options ='Xeloda'
                            def store_drug_options():
                                drug_user_input.append(options)
                                user_choice.append(drug_user_input)
                                print(user_choice)
                                drugoptions ='Kadcyla'
                                toptions = ['Metastatic, Prior Treatment','Recurrance Treatment','None']
                                def store_treament():
                                    option1 = treatment_user_1.get()
                                    option2 = treatment_user_2.get()
                                    if option2 ==1 and option1==2:
                                        user_choice[3].append('Metastatic, Prior Treatment')   
                                        user_choice[3].append('Recurrance Treatment')
                                        user_choice[4].append(drugoptions)   
                                    elif option1 ==1:
                                        user_choice[3].append('Metastatic, Prior Treatment')
                                        user_choice[4].append(drugoptions)
                                    elif option2 ==1:
                                        user_choice[3].append('Recurrance Treatment')
                                        user_choice[4].append(drugoptions)   
 
                                    print(user_choice)
                                    def store_show_month():
                                        user_month = month_user.get()
                                        user_choice.append(user_month)
                                        print(user_choice)
                                        def close_window():
                                            gui_1.destroy()
                                        def change_label():
                                            p.destroy()
                                            pfinal = tk.Label(gui_1,text="""Complete!""",width =30,font=('Imago',17,'bold'),anchor = 'w',fg='#0066CC')
                                            pfinal.place(x=400,y=775)
                                        change_label()
                                        close_window()
    
                                    btn6_1,btn6_2,btn6_3,btn6_4,btn6_5,btn6_6,btn6_7,btn6_8,btn6_9,btn6_10,btn6_11,btn6_12 = '','','','','','','','','','','',''
                                    bttn6 = [btn6_1,btn6_2,btn6_3,btn6_4,btn6_5,btn6_6,btn6_7,btn6_8,btn6_9,btn6_10,btn6_11,btn6_12]
                                    optionm = [("January"),("February"),("March"),("April"),("May"),("June"),("July"),("August"),("September"),("October"),("November"),("December")]
                                    array = [1,2,3,4,5,6,7,8,9,10,11,12]
                                    for i in range(6):
                                        yval = 420 + 30*(i)
                                        bttn6[i] = tk.Radiobutton(gui_1,
                                                                text = optionm[i],
                                                                variable = month_user,
                                                                width = 15,
                                                                font=('Imago',13),
                                                                command = store_show_month,
                                                                value = array[i],
                                                                anchor = 'w')
                                        bttn6[i].place(x=500,y=yval)
                                    
                                    for i in range(6):
                                        yval = 420 + 30*(i)
                                        bttn6[i] = tk.Radiobutton(gui_1,
                                                                text = optionm[i+6],
                                                                variable = month_user,
                                                                width = 15,
                                                                font=('Imago',13),
                                                                command = store_show_month,
                                                                value = array[i+6],
                                                                anchor = 'w')
                                        bttn6[i].place(x=700,y=yval)
                                    q7.place(x=500,y=390)
                                    p.config(text = "Progress: 6/7")                                 
                                btn1 = tk.Checkbutton(gui_1, text=toptions[0], variable=treatment_user_1, width = 30,font=('Imago',13),anchor ='w')
                                btn1.place(x=500,y=230)
                                btn2 = tk.Checkbutton(gui_1, text=toptions[1], variable=treatment_user_2, width = 30,font=('Imago',13),anchor ='w')
                                btn2.place(x=500,y=260)  
                                btn3 = tk.Checkbutton(gui_1, text=toptions[2], width = 20,font=('Imago',13),anchor ='w')
                                btn3.place(x=500,y=290) 
                                enter = tk.Button(gui_1, text='Select Treatment', font=('Imago',13), command = store_treament)
                                enter.place(x=500,y=325)
                                q6.place(x=500,y=210)
                                p.config(text="Progress: 5/7") 
                            ans = tk.Label(gui_1,text = options,font=('Imago',13),anchor = 'w')
                            ans.place(x=500,y=165)
                            q5_2.place(x=500,y=140)
                            p.config(text="Progress: 4/7") 
                            store_drug_options()          
                           
                    for i in range(2):
                        yval = 70 + (30*(i))
                        buttons4[i] = tk.Radiobutton(gui_1,text = buttons4_options[i],variable = cancer_type_user,indicatoron = 1,width = 35,font=('Imago',13),command = store_cancer_type,value = buttons4_options[i],anchor = 'w')
                        buttons4[i].place(x=500,y=yval)
                        q4_1.place(x=500,y=30)
                        p.config(text="Progress: 3/7")
                
                if user_choice[2] == 'Pancreas':
                    btn4_1,btn4_2 = '',''
                    buttons4 = [btn4_1,btn4_2]
                    buttons4_options = ["Pancreatic","Pancreatic, Metastatic"]
                        
                    def store_cancer_type():
                        user_cancer_type = cancer_type_user.get()
                        cancer_type_user_input.append(user_cancer_type)
                        user_choice.append(cancer_type_user_input)
                        print(user_choice)
                        #Q5
                        if user_choice[3][0] == 'Pancreatic':
                            options ='Xeloda'
                            def store_drug_options():
                                drug_user_input.append(options)
                                user_choice.append(drug_user_input)
                                print(user_choice)
                                drugoptions ='Kadcyla'
                                toptions = ['Metastatic, Prior Treatment','Recurrance Treatment','None']
                                def store_treament():
                                    option1 = treatment_user_1.get()
                                    option2 = treatment_user_2.get()
                                    if option2 ==1 and option1==2:
                                        user_choice[3].append('Metastatic, Prior Treatment')   
                                        user_choice[3].append('Recurrance Treatment')
                                        user_choice[4].append(drugoptions)   
                                    elif option1 ==1:
                                        user_choice[3].append('Metastatic, Prior Treatment')
                                        user_choice[4].append(drugoptions)
                                    elif option2 ==1:
                                        user_choice[3].append('Recurrance Treatment')
                                        user_choice[4].append(drugoptions)  
                                    print(user_choice)
                                    def store_show_month():
                                        user_month = month_user.get()
                                        user_choice.append(user_month)
                                        print(user_choice)
                                        def close_window():
                                            gui_1.destroy()
                                        def change_label():
                                            p.destroy()
                                            pfinal = tk.Label(gui_1,text="""Complete!""",width =30,font=('Imago',17,'bold'),anchor = 'w',fg='#0066CC')
                                            pfinal.place(x=400,y=775)
                                        change_label()
                                        close_window()
    
                                    btn6_1,btn6_2,btn6_3,btn6_4,btn6_5,btn6_6,btn6_7,btn6_8,btn6_9,btn6_10,btn6_11,btn6_12 = '','','','','','','','','','','',''
                                    bttn6 = [btn6_1,btn6_2,btn6_3,btn6_4,btn6_5,btn6_6,btn6_7,btn6_8,btn6_9,btn6_10,btn6_11,btn6_12]
                                    optionm = [("January"),("February"),("March"),("April"),("May"),("June"),("July"),("August"),("September"),("October"),("November"),("December")]
                                    array = [1,2,3,4,5,6,7,8,9,10,11,12]
                                    for i in range(6):
                                        yval = 405 + 30*(i)
                                        bttn6[i] = tk.Radiobutton(gui_1,
                                                                text = optionm[i],
                                                                variable = month_user,
                                                                width = 15,
                                                                font=('Imago',13),
                                                                command = store_show_month,
                                                                value = array[i],
                                                                anchor = 'w')
                                        bttn6[i].place(x=500,y=yval)
                                    
                                    for i in range(6):
                                        yval = 405 + 30*(i)
                                        bttn6[i] = tk.Radiobutton(gui_1,
                                                                text = optionm[i+6],
                                                                variable = month_user,
                                                                width = 15,
                                                                font=('Imago',13),
                                                                command = store_show_month,
                                                                value = array[i+6],
                                                                anchor = 'w')
                                        bttn6[i].place(x=700,y=yval)
                                    q7.place(x=500,y=375)
                                    p.config(text = "Progress: 6/7")                                 
                                btn1 = tk.Checkbutton(gui_1, text=toptions[0], variable=treatment_user_1, width = 30,font=('Imago',13),anchor ='w')
                                btn1.place(x=500,y=230)
                                btn2 = tk.Checkbutton(gui_1, text=toptions[1], variable=treatment_user_2, width = 30,font=('Imago',13),anchor ='w')
                                btn2.place(x=500,y=260)  
                                btn3 = tk.Checkbutton(gui_1, text=toptions[2], width = 20,font=('Imago',13),anchor ='w')
                                btn3.place(x=500,y=290) 
                                enter = tk.Button(gui_1, text='Select Treatment', font=('Imago',13), command = store_treament)
                                enter.place(x=500,y=320)
                                q6.place(x=500,y=210)
                                p.config(text="Progress: 5/7")                             
                            #Q6 INSERT HERE
                            ans = tk.Label(gui_1,
                                           text = options,
                                           font=('Imago',13),
                                           anchor = 'w')
                            ans.place(x=500,y=165)
                            q5_2.place(x=500,y=140)
                            p.config(text="Progress: 5/7") 
                            store_drug_options()         
                            
                        if user_choice[3][0] == 'Pancreatic, Metastatic':
                            options ='Tarceva'
                            def store_drug_options():
                                drug_user_input.append(options)
                                user_choice.append(drug_user_input)
                                print(user_choice)
                                drugoptions ='Kadcyla'
                                toptions = ['Metastatic, Prior Treatment','Recurrance Treatment','None']
                                def store_treament():
                                    option1 = treatment_user_1.get()
                                    option2 = treatment_user_2.get()
                                
                                    if option2 ==1 and option1==2:
                                        user_choice[3].append('Metastatic, Prior Treatment')   
                                        user_choice[3].append('Recurrance Treatment')
                                        user_choice[4].append(drugoptions)   
                                    elif option1 ==1:
                                        user_choice[3].append('Metastatic, Prior Treatment')
                                        user_choice[4].append(drugoptions)
                                    elif option2 ==1:
                                        user_choice[3].append('Recurrance Treatment')
                                        user_choice[4].append(drugoptions)  

                                    print(user_choice)
                                    def store_show_month():
                                        user_month = month_user.get()
                                        user_choice.append(user_month)
                                        print(user_choice)
                                        def close_window():
                                            gui_1.destroy()
                                        def change_label():
                                            p.destroy()
                                            pfinal = tk.Label(gui_1,text="""Complete!""",width =30,font=('Imago',17,'bold'),anchor = 'w',fg='#0066CC')
                                            pfinal.place(x=400,y=775)
                                        change_label()
                                        close_window()
    
                                    btn6_1,btn6_2,btn6_3,btn6_4,btn6_5,btn6_6,btn6_7,btn6_8,btn6_9,btn6_10,btn6_11,btn6_12 = '','','','','','','','','','','',''
                                    bttn6 = [btn6_1,btn6_2,btn6_3,btn6_4,btn6_5,btn6_6,btn6_7,btn6_8,btn6_9,btn6_10,btn6_11,btn6_12]
                                    optionm = [("January"),("February"),("March"),("April"),("May"),("June"),("July"),("August"),("September"),("October"),("November"),("December")]
                                    array = [1,2,3,4,5,6,7,8,9,10,11,12]
                                    for i in range(6):
                                        yval = 405 + 30*(i)
                                        bttn6[i] = tk.Radiobutton(gui_1,
                                                                text = optionm[i],
                                                                variable = month_user,
                                                                width = 15,
                                                                font=('Imago',13),
                                                                command = store_show_month,
                                                                value = array[i],
                                                                anchor = 'w')
                                        bttn6[i].place(x=500,y=yval)
                                    
                                    for i in range(6):
                                        yval = 405 + 30*(i)
                                        bttn6[i] = tk.Radiobutton(gui_1,
                                                                text = optionm[i+6],
                                                                variable = month_user,
                                                                width = 15,
                                                                font=('Imago',13),
                                                                command = store_show_month,
                                                                value = array[i+6],
                                                                anchor = 'w')
                                        bttn6[i].place(x=700,y=yval)
                                    q6.place(x=500,y=375)
                                    p.config(text = "Progress: 6/7")                                 
                                btn1 = tk.Checkbutton(gui_1, text=toptions[0], variable=treatment_user_1, width = 30,font=('Imago',13),anchor ='w')
                                btn1.place(x=500,y=230)
                                btn2 = tk.Checkbutton(gui_1, text=toptions[1], variable=treatment_user_2, width = 30,font=('Imago',13),anchor ='w')
                                btn2.place(x=500,y=260)  
                                btn3 = tk.Checkbutton(gui_1, text=toptions[2], width = 20,font=('Imago',13),anchor ='w')
                                btn3.place(x=500,y=290) 
                                enter = tk.Button(gui_1, text='Select Treatment', font=('Imago',13), command = store_treament)
                                enter.place(x=500,y=320)
                                q6.place(x=500,y=210)
                                p.config(text="Progress: 5/7")                          
                            #Q6 INSERT HERE
                            ans = tk.Label(gui_1,
                                           text = options,
                                           font=('Imago',13),
                                           anchor = 'w')
                            ans.place(x=500,y=165)
                            q5_2.place(x=500,y=140)
                            p.config(text="Progress: 5/7") 
                            store_drug_options()                    
                    for i in range(2):
                        yval = 70 + (30*(i))
                        buttons4[i] = tk.Radiobutton(gui_1,
                                                     text = buttons4_options[i],
                                                     variable = cancer_type_user,
                                                     width = 35,
                                                     font=('Imago',13),
                                                     command = store_cancer_type,
                                                     value = buttons4_options[i],
                                                     anchor = 'w')
                        buttons4[i].place(x=500,y=yval)
                    q4_1.place(x=500,y=30)
                    p.config(text="Progress: 3/7")
                    
                if user_choice[2] == 'Peritoneum':
                    def store_cancer_type():
                        user_cancer_type = 'Peritoneal'
                        cancer_type_user_input.append(user_cancer_type)
                        user_choice.append(cancer_type_user_input)
                        print(user_choice[3])
                        #Q5
                        if user_choice[3][0] == 'Peritoneal':
                            def store_drug_options():
                                drug_user_input.append('Xeloda')
                                user_choice.append(drug_user_input)
                                print(user_choice)
                                drugoptions ='Kadcyla'
                                toptions = ['Metastatic, Prior Treatment','Recurrance Treatment','None']
                                def store_treament():
                                    option1 = treatment_user_1.get()
                                    option2 = treatment_user_2.get()
                                
                                    if option2 ==1 and option1==2:
                                        user_choice[3].append('Metastatic, Prior Treatment')   
                                        user_choice[3].append('Recurrance Treatment')
                                        user_choice[4].append(drugoptions)   
                                    elif option1 ==1:
                                        user_choice[3].append('Metastatic, Prior Treatment')
                                        user_choice[4].append(drugoptions)
                                    elif option2 ==1:
                                        user_choice[3].append('Recurrance Treatment')
                                        user_choice[4].append(drugoptions)  

                                    print(user_choice)
                                    def store_show_month():
                                        user_month = month_user.get()
                                        user_choice.append(user_month)
                                        print(user_choice)
                                        def close_window():
                                            gui_1.destroy()
                                        def change_label():
                                            p.destroy()
                                            pfinal = tk.Label(gui_1,text="""Complete!""",width =30,font=('Imago',17,'bold'),anchor = 'w',fg='#0066CC')
                                            pfinal.place(x=400,y=775)
                                        change_label()
                                        close_window()
    
                                    btn6_1,btn6_2,btn6_3,btn6_4,btn6_5,btn6_6,btn6_7,btn6_8,btn6_9,btn6_10,btn6_11,btn6_12 = '','','','','','','','','','','',''
                                    bttn6 = [btn6_1,btn6_2,btn6_3,btn6_4,btn6_5,btn6_6,btn6_7,btn6_8,btn6_9,btn6_10,btn6_11,btn6_12]
                                    optionm = [("January"),("February"),("March"),("April"),("May"),("June"),("July"),("August"),("September"),("October"),("November"),("December")]
                                    array = [1,2,3,4,5,6,7,8,9,10,11,12]
                                    for i in range(6):
                                        yval = 395 + 30*(i)
                                        bttn6[i] = tk.Radiobutton(gui_1,
                                                                text = optionm[i],
                                                                variable = month_user,
                                                                width = 15,
                                                                font=('Imago',13),
                                                                command = store_show_month,
                                                                value = array[i],
                                                                anchor = 'w')
                                        bttn6[i].place(x=500,y=yval)
                                    
                                    for i in range(6):
                                        yval = 395 + 30*(i)
                                        bttn6[i] = tk.Radiobutton(gui_1,
                                                                text = optionm[i+6],
                                                                variable = month_user,
                                                                width = 15,
                                                                font=('Imago',13),
                                                                command = store_show_month,
                                                                value = array[i+6],
                                                                anchor = 'w')
                                        bttn6[i].place(x=700,y=yval)
                                    q7.place(x=500,y=365)
                                    p.config(text = "Progress: 6/7")                                
                                btn1 = tk.Checkbutton(gui_1, text=toptions[0], variable=treatment_user_1, width = 30,font=('Imago',13),anchor ='w')
                                btn1.place(x=500,y=210)
                                btn2 = tk.Checkbutton(gui_1, text=toptions[1], variable=treatment_user_2, width = 30,font=('Imago',13),anchor ='w')
                                btn2.place(x=500,y=240)  
                                btn3 = tk.Checkbutton(gui_1, text=toptions[2], width = 20,font=('Imago',13),anchor ='w')
                                btn3.place(x=500,y=270) 
                                enter = tk.Button(gui_1, text='Select Treatment', font=('Imago',13), command = store_treament)
                                enter.place(x=500,y=300)
                                q6.place(x=500,y=180)
                                p.config(text="Progress: 5/7")                                
                            #Q6 INSERT HERE
                        options ='Xeloda'
                        ans = tk.Label(gui_1,
                                       text = options,
                                       font=('Imago',13),
                                       anchor = 'w')
                        ans.place(x=500,y=135)
                        q5_2.place(x=500,y=115)
                        p.config(text="Progress: 5/7") 
                        store_drug_options()        
                        
                    q4_2.place(x=500,y=30)
                    ans = tk.Label(gui_1,
                                   text = 'Peritoneal',
                                   font=('Imago',13),
                                   anchor = 'w')
                    ans.place(x=500,y=55)
                    p.config(text="Progress: 3/7")
                    store_cancer_type()    
                
                if user_choice[2] == 'Skin':
                    btn4_1,btn4_2 = '',''
                    buttons4 = [btn4_1,btn4_2]
                    buttons4_options = ["Basal Cell Carcinoma, Metastatic","Melanoma, Metastatic"]
                        
                    def store_cancer_type():
                        user_cancer_type = cancer_type_user.get()
                        cancer_type_user_input.append(user_cancer_type)
                        user_choice.append(cancer_type_user_input)
                        print(user_choice[3])
                     
                        #Q5
                        if user_choice[3][0] == 'Basal Cell Carcinoma, Metastatic':                        
                            def store_drug_options():
                                drug_user_input.append('Erivedge')
                                user_choice.append(drug_user_input)
                                print(user_choice)
                                drugoptions ='Kadcyla'
                                toptions = ['Metastatic, Prior Treatment','Recurrance Treatment','None']
                                def store_treament():
                                    option1 = treatment_user_1.get()
                                    option2 = treatment_user_2.get()
                                
                                    if option2 ==1 and option1==2:
                                        user_choice[3].append('Metastatic, Prior Treatment')   
                                        user_choice[3].append('Recurrance Treatment')
                                        user_choice[4].append(drugoptions)   
                                    elif option1 ==1:
                                        user_choice[3].append('Metastatic, Prior Treatment')
                                        user_choice[4].append(drugoptions)
                                    elif option2 ==1:
                                        user_choice[3].append('Recurrance Treatment')
                                        user_choice[4].append(drugoptions)  

                                    print(user_choice)
                                    def store_show_month():
                                        user_month = month_user.get()
                                        user_choice.append(user_month)
                                        print(user_choice)
                                        def close_window():
                                            gui_1.destroy()
                                        def change_label():
                                            p.destroy()
                                            pfinal = tk.Label(gui_1,text="""Complete!""",width =30,font=('Imago',17,'bold'),anchor = 'w',fg='#0066CC')
                                            pfinal.place(x=400,y=775)
                                        change_label()
                                        close_window()
    
                                    btn6_1,btn6_2,btn6_3,btn6_4,btn6_5,btn6_6,btn6_7,btn6_8,btn6_9,btn6_10,btn6_11,btn6_12 = '','','','','','','','','','','',''
                                    bttn6 = [btn6_1,btn6_2,btn6_3,btn6_4,btn6_5,btn6_6,btn6_7,btn6_8,btn6_9,btn6_10,btn6_11,btn6_12]
                                    optionm = [("January"),("February"),("March"),("April"),("May"),("June"),("July"),("August"),("September"),("October"),("November"),("December")]
                                    array = [1,2,3,4,5,6,7,8,9,10,11,12]
                                    for i in range(6):
                                        yval = 470 + 30*(i)
                                        bttn6[i] = tk.Radiobutton(gui_1,
                                                                text = optionm[i],
                                                                variable = month_user,
                                                                width = 15,
                                                                font=('Imago',13),
                                                                command = store_show_month,
                                                                value = array[i],
                                                                anchor = 'w')
                                        bttn6[i].place(x=500,y=yval)
                                    
                                    for i in range(6):
                                        yval = 470 + 30*(i)
                                        bttn6[i] = tk.Radiobutton(gui_1,
                                                                text = optionm[i+6],
                                                                variable = month_user,
                                                                width = 15,
                                                                font=('Imago',13),
                                                                command = store_show_month,
                                                                value = array[i+6],
                                                                anchor = 'w')
                                        bttn6[i].place(x=700,y=yval)
                                    q7.place(x=500,y=430)
                                    p.config(text = "Progress: 6/7")                                 
                                btn1 = tk.Checkbutton(gui_1, text=toptions[0], variable=treatment_user_1, width = 30,font=('Imago',13),anchor ='w')
                                btn1.place(x=500,y=260)
                                btn2 = tk.Checkbutton(gui_1, text=toptions[1], variable=treatment_user_2, width = 30,font=('Imago',13),anchor ='w')
                                btn2.place(x=500,y=290)  
                                btn3 = tk.Checkbutton(gui_1, text=toptions[2], width = 20,font=('Imago',13),anchor ='w')
                                btn3.place(x=500,y=320) 
                                enter = tk.Button(gui_1, text='Select Treatment', font=('Imago',13), command = store_treament)
                                enter.place(x=500,y=360)
                                q6.place(x=500,y=230)
                                p.config(text="Progress: 5/7")                             
                            #Q6 INSERT HERE
                            options ='Erivedge'
                            ans = tk.Label(gui_1,
                                           text = options,
                                           font=('Imago',13),
                                           anchor = 'w')
                            ans.place(x=500,y=175)
                            q5_2.place(x=500,y=150)
                            p.config(text="Progress: 5/7")
                            store_drug_options()   
                        if user_choice[3][0] == 'Melanoma, Metastatic':
                            options ='Zelboraf'
                            def store_drug_options():
                                drug_user_input.append(options)
                                user_choice.append(drug_user_input)
                                print(user_choice)
                                drugoptions ='Kadcyla'
                                toptions = ['Metastatic, Prior Treatment','Recurrance Treatment','None']
                                def store_treament():
                                    option1 = treatment_user_1.get()
                                    option2 = treatment_user_2.get()
                                
                                    if option2 ==1 and option1==2:
                                        user_choice[3].append('Metastatic, Prior Treatment')   
                                        user_choice[3].append('Recurrance Treatment')
                                        user_choice[4].append(drugoptions)   
                                    elif option1 ==1:
                                        user_choice[3].append('Metastatic, Prior Treatment')
                                        user_choice[4].append(drugoptions)
                                    elif option2 ==1:
                                        user_choice[3].append('Recurrance Treatment')
                                        user_choice[4].append(drugoptions)  
 
                                    print(user_choice)
                                    def store_show_month():
                                        user_month = month_user.get()
                                        user_choice.append(user_month)
                                        print(user_choice)
                                        def close_window():
                                            gui_1.destroy()
                                        def change_label():
                                            p.destroy()
                                            pfinal = tk.Label(gui_1,text="""Complete!""",width =30,font=('Imago',17,'bold'),anchor = 'w',fg='#0066CC')
                                            pfinal.place(x=400,y=775)
                                        change_label()
                                        close_window()
    
                                    btn6_1,btn6_2,btn6_3,btn6_4,btn6_5,btn6_6,btn6_7,btn6_8,btn6_9,btn6_10,btn6_11,btn6_12 = '','','','','','','','','','','',''
                                    bttn6 = [btn6_1,btn6_2,btn6_3,btn6_4,btn6_5,btn6_6,btn6_7,btn6_8,btn6_9,btn6_10,btn6_11,btn6_12]
                                    optionm = [("January"),("February"),("March"),("April"),("May"),("June"),("July"),("August"),("September"),("October"),("November"),("December")]
                                    array = [1,2,3,4,5,6,7,8,9,10,11,12]
                                    for i in range(6):
                                        yval = 440 + 30*(i)
                                        bttn6[i] = tk.Radiobutton(gui_1,
                                                                text = optionm[i],
                                                                variable = month_user,
                                                                width = 15,
                                                                font=('Imago',13),
                                                                command = store_show_month,
                                                                value = array[i],
                                                                anchor = 'w')
                                        bttn6[i].place(x=500,y=yval)
                                    
                                    for i in range(6):
                                        yval = 440 + 30*(i)
                                        bttn6[i] = tk.Radiobutton(gui_1,
                                                                text = optionm[i+6],
                                                                variable = month_user,
                                                                width = 15,
                                                                font=('Imago',13),
                                                                command = store_show_month,
                                                                value = array[i+6],
                                                                anchor = 'w')
                                        bttn6[i].place(x=700,y=yval)
                                    q7.place(x=500,y=410)
                                    p.config(text = "Progress: 6/7")                                 
                                btn1 = tk.Checkbutton(gui_1, text=toptions[0], variable=treatment_user_1, width = 30,font=('Imago',13),anchor ='w')
                                btn1.place(x=500,y=260)
                                btn2 = tk.Checkbutton(gui_1, text=toptions[1], variable=treatment_user_2, width = 30,font=('Imago',13),anchor ='w')
                                btn2.place(x=500,y=290)  
                                btn3 = tk.Checkbutton(gui_1, text=toptions[2], width = 20,font=('Imago',13),anchor ='w')
                                btn3.place(x=500,y=320) 
                                enter = tk.Button(gui_1, text='Select Treatment', font=('Imago',13), command = store_treament)
                                enter.place(x=500,y=355)
                                q6.place(x=500,y=230)
                                p.config(text="Progress: 5/7")                                      
                            #Q6 INSERT HERE
                            ans = tk.Label(gui_1,
                                           text = options,
                                           font=('Imago',13),
                                           anchor = 'w')
                            ans.place(x=500,y=175)
                            q5_2.place(x=500,y=150)
                            p.config(text="Progress: 5/7") 
                            store_drug_options()     
                            
                    for i in range(2):
                        yval = 70 + (30*(i))
                        buttons4[i] = tk.Radiobutton(gui_1,
                                                     text = buttons4_options[i],
                                                     variable = cancer_type_user,
                                                     width = 35,
                                                     font=('Imago',13),
                                                     command = store_cancer_type,
                                                     value = buttons4_options[i],
                                                     anchor = 'w')
                        buttons4[i].place(x=500,y=yval)
                        q4_1.place(x=500,y=30)
                        p.config(text="Progress: 3/7")
                    
                
                if user_choice[2] == 'Stomach':
                    def store_cancer_type():
                        user_cancer_type = 'Stomach'
                        cancer_type_user_input.append(user_cancer_type)
                        user_choice.append(cancer_type_user_input)
                        print(user_choice)   
                        if user_choice[3][0] == 'Stomach':
                            options = ['Xeloda','Herceptin']
                            
                            def store_drug_options():
                                option1 = drug_1.get()
                                option2 = drug_2.get()
                                if option1 == 1:
                                    drug_user_input.append("Xeloda")
                                if option2 == 1:
                                    drug_user_input.append("Herceptin")
                                user_choice.append(drug_user_input)
                                print(user_choice)
                                drugoptions ='Kadcyla'
                                toptions = ['Metastatic, Prior Treatment','Recurrance Treatment','None']
                                def store_treament():
                                    option1 = treatment_user_1.get()
                                    option2 = treatment_user_2.get()
                                    if option2 ==1 and option1==2:
                                        user_choice[3].append('Metastatic, Prior Treatment')   
                                        user_choice[3].append('Recurrance Treatment')
                                        user_choice[4].append(drugoptions)   
                                    elif option1 ==1:
                                        user_choice[3].append('Metastatic, Prior Treatment')
                                        user_choice[4].append(drugoptions)
                                    elif option2 ==1:
                                        user_choice[3].append('Recurrance Treatment')
                                        user_choice[4].append(drugoptions)  
                                    print(user_choice)
                                    def store_show_month():
                                        user_month = month_user.get()
                                        user_choice.append(user_month)
                                        print(user_choice)
                                        def close_window():
                                            gui_1.destroy()
                                        def change_label():
                                            p.destroy()
                                            pfinal = tk.Label(gui_1,text="""Complete!""",width =30,font=('Imago',17,'bold'),anchor = 'w',fg='#0066CC')
                                            pfinal.place(x=400,y=775)
                                        change_label()
                                        close_window()
        
                                    btn6_1,btn6_2,btn6_3,btn6_4,btn6_5,btn6_6,btn6_7,btn6_8,btn6_9,btn6_10,btn6_11,btn6_12 = '','','','','','','','','','','',''
                                    bttn6 = [btn6_1,btn6_2,btn6_3,btn6_4,btn6_5,btn6_6,btn6_7,btn6_8,btn6_9,btn6_10,btn6_11,btn6_12]
                                    optionm = [("January"),("February"),("March"),("April"),("May"),("June"),("July"),("August"),("September"),("October"),("November"),("December")]
                                    array = [1,2,3,4,5,6,7,8,9,10,11,12]
                                    for i in range(6):
                                        yval = 490 + 30*(i)
                                        bttn6[i] = tk.Radiobutton(gui_1,
                                                                text = optionm[i],
                                                                variable = month_user,
                                                                width = 15,
                                                                font=('Imago',13),
                                                                command = store_show_month,
                                                                value = array[i],
                                                                anchor = 'w')
                                        bttn6[i].place(x=500,y=yval)
                                    
                                    for i in range(6):
                                        yval = 490 + 30*(i)
                                        bttn6[i] = tk.Radiobutton(gui_1,
                                                                text = optionm[i+6],
                                                                variable = month_user,
                                                                width = 15,
                                                                font=('Imago',13),
                                                                command = store_show_month,
                                                                value = array[i+6],
                                                                anchor = 'w')
                                        bttn6[i].place(x=700,y=yval)
                                    q7.place(x=500,y=460)
                                    p.config(text = "Progress: 6/7")                             
                                btn1 = tk.Checkbutton(gui_1, text=toptions[0], variable=treatment_user_1, width = 30,font=('Imago',13),anchor ='w')
                                btn1.place(x=500,y=305)
                                btn2 = tk.Checkbutton(gui_1, text=toptions[1], variable=treatment_user_2, width = 30,font=('Imago',13),anchor ='w')
                                btn2.place(x=500,y=335)  
                                btn3 = tk.Checkbutton(gui_1, text=toptions[2], width = 20,font=('Imago',13),anchor ='w')
                                btn3.place(x=500,y=365) 
                                enter = tk.Button(gui_1, text='Select Treatment', font=('Imago',13), command = store_treament)
                                enter.place(x=500,y=395)
                                q6.place(x=500,y=275)
                                p.config(text="Progress: 5/7")                                   
                            btn1 = tk.Checkbutton(gui_1, text=options[0], variable=drug_1, width = 20,font=('Imago',13),anchor ='w')
                            btn1.place(x=500,y=150)
                            btn2 = tk.Checkbutton(gui_1, text=options[1], variable=drug_2, width = 20,font=('Imago',13),anchor ='w')
                            btn2.place(x=500,y=180)  
                            enter = tk.Button(gui_1, text='Select Drug', font=('Imago',13), command = store_drug_options)
                            enter.place(x=500,y=210)
                            q5_1.place(x=500,y=120)
                            p.config(text="Progress: 4/7")                 
                    q4_2.place(x=500,y=30)
                    p.config(text="Progress: 4/7")
                    ans = tk.Label(gui_1,
                                   text = 'Stomach',
                                   font=('Imago',13),
                                   anchor = 'w')
                    ans.place(x=500,y=55)
                    store_cancer_type()    
    
                
                if user_choice[2] == 'Neuroendocrine':
                    def store_cancer_type():
                        user_cancer_type = 'Neuroendocrine'
                        cancer_type_user_input.append(user_cancer_type)
                        user_choice.append(cancer_type_user_input)
                        print(user_choice)
                    #Q5
                        if user_choice[3][0] == 'Neuroendocrine':
                            options ='Xeloda'
                            
                            def store_drug_options():
                                drug_user_input.append(options)
                                user_choice.append(drug_user_input)
                                print(user_choice)
                                drugoptions ='Kadcyla'
                                toptions = ['Metastatic, Prior Treatment','Recurrance Treatment','None']
                                def store_treament():
                                    option1 = treatment_user_1.get()
                                    option2 = treatment_user_2.get()
                                    if option2 ==1 and option1==2:
                                        user_choice[3].append('Metastatic, Prior Treatment')   
                                        user_choice[3].append('Recurrance Treatment')
                                        user_choice[4].append(drugoptions)   
                                    elif option1 ==1:
                                        user_choice[3].append('Metastatic, Prior Treatment')
                                        user_choice[4].append(drugoptions)
                                    elif option2 ==1:
                                        user_choice[3].append('Recurrance Treatment')
                                        user_choice[4].append(drugoptions)   
   
                                    print(user_choice)
                                    def store_show_month():
                                        user_month = month_user.get()
                                        user_choice.append(user_month)
                                        print(user_choice)
                                        def close_window():
                                            gui_1.destroy()
                                        def change_label():
                                            p.destroy()
                                            pfinal = tk.Label(gui_1,text="""Complete!""",width =30,font=('Imago',17,'bold'),anchor = 'w',fg='#0066CC')
                                            pfinal.place(x=400,y=775)
                                        change_label()
                                        close_window()
    
                                    btn6_1,btn6_2,btn6_3,btn6_4,btn6_5,btn6_6,btn6_7,btn6_8,btn6_9,btn6_10,btn6_11,btn6_12 = '','','','','','','','','','','',''
                                    bttn6 = [btn6_1,btn6_2,btn6_3,btn6_4,btn6_5,btn6_6,btn6_7,btn6_8,btn6_9,btn6_10,btn6_11,btn6_12]
                                    optionm = [("January"),("February"),("March"),("April"),("May"),("June"),("July"),("August"),("September"),("October"),("November"),("December")]
                                    array = [1,2,3,4,5,6,7,8,9,10,11,12]
                                    for i in range(6):
                                        yval = 425 + 30*(i)
                                        bttn6[i] = tk.Radiobutton(gui_1,
                                                                text = optionm[i],
                                                                variable = month_user,
                                                                width = 15,
                                                                font=('Imago',13),
                                                                command = store_show_month,
                                                                value = array[i],
                                                                anchor = 'w')
                                        bttn6[i].place(x=500,y=yval)
                                    
                                    for i in range(6):
                                        yval = 425 + 30*(i)
                                        bttn6[i] = tk.Radiobutton(gui_1,
                                                                text = optionm[i+6],
                                                                variable = month_user,
                                                                width = 15,
                                                                font=('Imago',13),
                                                                command = store_show_month,
                                                                value = array[i+6],
                                                                anchor = 'w')
                                        bttn6[i].place(x=700,y=yval)
                                    q7.place(x=500,y=395)
                                    p.config(text = "Progress: 6/7")                                 
                                btn1 = tk.Checkbutton(gui_1, text=toptions[0], variable=treatment_user_1, width = 30,font=('Imago',13),anchor ='w')
                                btn1.place(x=500,y=235)
                                btn2 = tk.Checkbutton(gui_1, text=toptions[1], variable=treatment_user_2, width = 30,font=('Imago',13),anchor ='w')
                                btn2.place(x=500,y=265)  
                                btn3 = tk.Checkbutton(gui_1, text=toptions[2], width = 20,font=('Imago',13),anchor ='w')
                                btn3.place(x=500,y=295) 
                                enter = tk.Button(gui_1, text='Select Treatment', font=('Imago',13), command = store_treament)
                                enter.place(x=500,y=325)
                                q6.place(x=500,y=205)
                                p.config(text="Progress: 5/7")                              
                            #Q6 INSERT HERE
                            ans = tk.Label(gui_1,
                                           text = options,
                                           font=('Imago',13),
                                           anchor = 'w')
                            ans.place(x=500,y=140)
                            q5_2.place(x=500,y=115)
                            p.config(text="Progress: 5/7") 
                            store_drug_options()  
                            
                    q4_2.place(x=500,y=30)
                    ans = tk.Label(gui_1,
                                   text = 'Neuroendocrine',
                                   font=('Imago',13),
                                   anchor = 'w')
                    ans.place(x=500,y=55)
                    p.config(text="Progress: 3/7")
                    store_cancer_type()   
                    
            #INSERT AFTER DEF
            btn1_1,btnq1_2,btn1_3,btn1_4,btn1_5,btn1_6,btn1_7,btn1_8,btn1_9,btn1_10,btn1_11,btn1_12,btn1_13,btn1_14 = '','','','','','','','','','','','','',''
            buttons1 = [btn1_1,btnq1_2,btn1_3,btn1_4,btn1_5,btn1_6,btn1_7,btn1_8,btn1_9,btn1_10,btn1_11,btn1_12,btn1_13,btn1_14]            
            if user_choice[1]=='Female':
                buttons1_options = [("Blood"),("Brain"),("Breast"),("Colorectal"),("Esophagus"),("Kidney"),("Liver"),("Lungs"),("Neuroendocrine"),("Ovary"),("Pancreas"),("Peritoneum"),("Skin"),("Stomach")]
                for i in range(14):
                    yval = 300 + 30*(i)
                    buttons1[i] = tk.Radiobutton(gui_1,
                                            text = buttons1_options[i],
                                            variable = cancer_location_user,
                                            width = 15,
                                            font=('Imago',13),
                                            command = store_cancer_location,
                                            value = buttons1_options[i],
                                            anchor = 'w')
                    buttons1[i].place(x=40,y=yval)
            if user_choice[1]=='Male':
                buttons1_options = [("Blood"),("Brain"),("Breast"),("Colorectal"),("Esophagus"),("Kidney"),("Liver"),("Lungs"),("Neuroendocrine"),("Pancreas"),("Peritoneum"),("Skin"),("Stomach")]
                for i in range(13):
                    yval = 300 + 30*(i)
                    buttons1[i] = tk.Radiobutton(gui_1,
                                            text = buttons1_options[i],
                                            variable = cancer_location_user,
                                            width = 15,
                                            font=('Imago',13),
                                            command = store_cancer_location,
                                            value = buttons1_options[i],
                                            anchor = 'w')
                    buttons1[i].place(x=40,y=yval)    
            q3.place(x=40,y=250)    
            p.config(text="Progress: 2/7")
        
        btn2_1,btn2_2 = '',''
        buttons2 = [btn2_1,btn2_2]
        buttons2_options = [("Male"),("Female")]
        
        for i in range(2):
            xval = (100*i)+ 40
            buttons2[i] = tk.Radiobutton(gui_1,
                                        text = buttons2_options[i],
                                        variable = gender_user,
                                        width = 8,
                                        font=('Imago',13),
                                        command = store_gender,
                                        value = buttons2_options[i],
                                        anchor ='w')
            buttons2[i].place(x=xval,y=185)
        q2.place(x=40,y=150)
        p.config(text="Progress: 1/7")
            
    btn1 = tk.Button(gui_1,
                    text = 'Enter Age',
                    textvariable = age_user.get(),
                    font=('Imaho',13),
                    command = store_age,
                    width = 9)
    btn1.place(x=40,y=90)
    q1.place(x=40,y=30)
    p.place(x=400,y=775)

#----------------------------------------------------------------------------------------------------------------------------------------
    gui_1.mainloop()
get_user_info()
print(user_choice)


#SECTION: IMPORT HACKATHON DATA - RESEARCH DATA
#----------------------------------------------------------------------------------------------------------------------------------
symptomsheet = '/Users/piaoruilin/Desktop/python/Hackathon Data - Sympyom Chart.csv'
cancersheet = '/Users/piaoruilin/Desktop/python/Hackathon Data - Cancer Symptom-2.csv'
drugsheet = '/Users/piaoruilin/Desktop/python/Hackathon Data - Drug Symptom-2.csv'
othersheet = '/Users/piaoruilin/Desktop/python/Hackathon Data - Other Symptom.csv'

#HACAKTHON DATA - LIST
symptom_list, description_list = ([] for i in range(2)) #SYMPTOM
cancer_area_list, cancer_symptom_list,cancer_description_list,cancer_fatal_freq = ([] for i in range(4)) #CANCER
cancer_area_drug_list,cancer_type_list,drug_name_list,drug_symptom_list,drug_description_list = ([] for i in range(5)) #CANCERFREQ
drug_normal_freq_list,drug_fatal_freqeuncy_list,drug_emergency_freq_list = ([] for i in range(3)) #DRUG
other_symptom_list,other_description_list,other_fatal_freq_list = ([] for i in range(3)) #OTHER

#This function sorts all Hackathon Data in to list in columns
def open_sort_csv(b,c,d,e):
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
    return(symptom_list,description_list,cancer_area_list,cancer_symptom_list,cancer_description_list,cancer_fatal_freq,cancer_area_drug_list,cancer_type_list,drug_name_list,drug_symptom_list,drug_description_list,drug_normal_freq_list,drug_fatal_freqeuncy_list,drug_emergency_freq_list)

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
octpath = '/Users/piaoruilin/Desktop/python/months/Test1 - October.csv'
novpath = '/Users/piaoruilin/Desktop/python/months/Test1 - November.csv'
decpath = '/Users/piaoruilin/Desktop/python/months/Test1 - December.csv'
yearpath = [janpath,febpath,marpath,aprpath,maypath,junpath,julpath,augpath,seppath,octpath,novpath,decpath]

#This function sorts test data into lists so it can be plot
def sort_test_into_list():
    
    def test_get_january(jan):
        with open(str(jan), newline='') as file:
            reader = csv.reader(file)
            jancsv = [row for row in reader]
        return january
    
    def test_get_february(feb):
        with open(str(feb), newline='') as file:
            reader = csv.reader(file)
            febcsv = [row for row in reader]
        
        for i in range(29):
            for j in range(534):
                february.append(febcsv[j][i])
        return february
    
    def test_get_march(mar):
        with open(str(mar), newline='') as file:
            reader = csv.reader(file)
            marcsv = [row for row in reader]
        
        for i in range(31):
            for j in range(534):
                march.append(marcsv[j][i])
        return march
                          
    def test_get_april(apr):
        with open(str(apr), newline='') as file:
            reader = csv.reader(file)
            aprcsv = [row for row in reader]
        
        for i in range(30):
            for j in range(534):
                april.append(aprcsv[j][i])
        return april
                
    def test_get_may(mayy):
        with open(str(mayy), newline='') as file:
            reader = csv.reader(file)
            maycsv = [row for row in reader]
        
        for i in range(31):
            for j in range(534):
                may.append(maycsv[j][i])
        return may       
    def test_get_june(jun):
        with open(str(jun), newline='') as file:
            reader = csv.reader(file)
            juncsv = [row for row in reader]
        
        for i in range(30):
            for j in range(534):
                june.append(juncsv[j][i])
        return june        
    def test_get_july(jul):
        with open(str(jul), newline='') as file:
            reader = csv.reader(file)
            julcsv = [row for row in reader]
        
        for i in range(31):
            for j in range(534):
                july.append(julcsv[j][i])
        return july        
    def test_get_august(aug):
        with open(str(aug), newline='') as file:
            reader = csv.reader(file)
            augcsv = [row for row in reader]
        
        for i in range(31):
            for j in range(534):
                august.append(augcsv[j][i])
        return august        
    
    def test_get_september(sep): 
        with open(str(sep), newline='') as file:
            reader = csv.reader(file)
            aprcsv = [row for row in reader]
        for i in range(30):
            for j in range(534):
                september.append(aprcsv[j][i])
        return september
                    
    def test_get_october(octo):
        with open(str(octo), newline='') as file:
            reader = csv.reader(file)
            octcsv = [row for row in reader]
        for i in range(31):
            for j in range(534):
                october.append(octcsv[j][i])
        return october
        
    def test_get_november(nov):
        with open(str(nov), newline='') as file:
            reader = csv.reader(file)
            novcsv = [row for row in reader]
        for i in range(30):
            for j in range(534):
                november.append(novcsv[j][i])            
        return november
        
    def test_get_december(dec):
        with open(str(dec), newline='') as file:
            reader = csv.reader(file)
            deccsv = [row for row in reader]
        for i in range(31):
            for j in range(534):
                december.append(deccsv[j][i])            
        return december   
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
    return

sort_test_into_list()
'''

#SECTION: SORTING (RUILIN)
#--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#sort and compare user choice with symptoms
import operator 

user_choice = [0, 'Female', 'Breast', ['Breast, Metastatic'], ['Xeloda'], 1]

#Getting rid of 1st and 2nd element in user_choice array
index = [0,1]
new_user_choice = [i for i in user_choice if user_choice.index(i) not in index]

#Sorting out drug symptoms and putting them into an array
drugs_list = []
drugs = open("/Users/piaoruilin/Desktop/python/Hackathon Data - Drug Symptom-2.csv", 'r')
csv1 = csv.reader(drugs, delimiter=',')
sort = sorted(csv1, key=operator.itemgetter(0))
for eachline in sort :
    drug_array = eachline
    drugs_list.append(drug_array)
    
#Sorting out cancer symptoms and putting them into an array
cancer_list = []
cancer = open("/Users/piaoruilin/Desktop/python/Hackathon Data - Cancer Symptom-2.csv", 'r')
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
    other_array = eachline_2
    others_list.append(other_array)

#Sorting out symptom chart and putting them into an array
symptom_list = []
chart = open("/Users/piaoruilin/Desktop/python/Hackathon Data - Sympyom Chart.csv", 'r')
csv4 = csv.reader(chart, delimiter=',')
sort4 = sorted(csv4, key=operator.itemgetter(0))
for eachline_3 in sort4 :
    chart_array = eachline_3
    symptom_list.append(chart_array)

#Comparing user choice with cancer symptoms and sorting by the area of cancer
new_drugs_list = []
for i in range(len(drugs_list)):
    if new_user_choice[0]==drugs_list[i][0] and new_user_choice[1][0]==drugs_list[i][1]:
        new_drugs_list.append(drugs_list[i])

new_cancer_list = []
for i in range(len(cancer_list)):
    if new_user_choice[0]==cancer_list[i][0]:
        new_cancer_list.append(cancer_list[i])

#Finding most frequent symptom of the month-------------------------------------------------------------------------------------------
#declare month arrays
#january[[day1],[day2],[day3],...]
#day1[symptom1, symptom2, symptom3,...]

with open('/Users/piaoruilin/Desktop/python/months/Test - January.csv', newline='') as jan:
    reader = csv.reader(jan)
    january = [row for row in reader]
with open('/Users/piaoruilin/Desktop/python/months/Test - February.csv', newline='') as feb:
    reader = csv.reader(feb)
    february = [tuple(row) for row in reader]
with open('/Users/piaoruilin/Desktop/python/months/Test - March.csv', newline='') as mar:
    reader = csv.reader(mar)
    march = [tuple(row) for row in reader]
with open('/Users/piaoruilin/Desktop/python/months/Test - April.csv', newline='') as apr:
    reader = csv.reader(apr)
    april = [tuple(row) for row in reader]
with open('/Users/piaoruilin/Desktop/python/months/Test - May.csv', newline='') as may:
    reader = csv.reader(may)
    may = [tuple(row) for row in reader]
with open('/Users/piaoruilin/Desktop/python/months/Test - June.csv', newline='') as jun:
    reader = csv.reader(jun)
    june = [tuple(row) for row in reader]
with open('/Users/piaoruilin/Desktop/python/months/Test - July.csv', newline='') as jul:
    reader = csv.reader(jul)
    july = [tuple(row) for row in reader]
with open('/Users/piaoruilin/Desktop/python/months/Test - August.csv', newline='') as aug:
    reader = csv.reader(aug)
    august = [tuple(row) for row in reader]
with open('/Users/piaoruilin/Desktop/python/months/Test - September.csv', newline='') as sep:
    reader = csv.reader(sep)
    september = [tuple(row) for row in reader]
with open('/Users/piaoruilin/Desktop/python/months/Test1 - October.csv', newline='') as octo:
    reader = csv.reader(octo)
    october = [tuple(row) for row in reader]
with open('/Users/piaoruilin/Desktop/python/months/Test1 - November.csv', newline='') as nov:
    reader = csv.reader(nov)
    november = [tuple(row) for row in reader]
with open('/Users/piaoruilin/Desktop/python/months/Test1 - December.csv', newline='') as dec:
    reader = csv.reader(dec)
    december = [tuple(row) for row in reader]

#!!!!!!TRY NOT TO DO MANUAL
for i in range(len(january)):
    january[0]
   
'''
frequent_jan = 24 #Ringing, Ears
frequent_feb = 23 #Difficulty, Leg Control | Problems with Urine, Blood | Sweling Eyelids
frequent_mar = 24 #Aches and Pain, Chest Tightness |  Aches and Pain, Upper Abdomen Mild | Difficulty, Swallowing
frequent_apr = 22 #Abnormalities, Enlarged Veins in Right Testicle
frequent_may = 24 #Redness, Breast
frequent_jun = 24 #Red Moles, Scalp
frequent_jul = 24 #Problems with Urine, Frothy
frequent_aug = 23 #Problems with Urine, Pain | Problems with Skin, Peeling,Palms | Heart Problems, Palpitation
frequent_sep = 26 #Bleeding, Stools
frequent_octo = 24 #Vision Problems, Watery Eyes
frequent_nov = 24 #Aches and Pain, Nipple
frequent_dec = 24 #Breathing Problems, Onset | Abnormalities, Wounds would not heal | Aches and Pain, Lower Back Mild

#SECTION: GETTING RESULTS
#--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
janf = [2,1,3,4] #10
febf = [4,3,1,5] #8
marf = [5,1,2,12] #10
aprf = [5,0,2,3] #9
mayf = [1,2,3,1] #10
junf = [1,1,0,0] #9
julf = [1,1,2,1] #10
augf = [1,4,1,1] #10
sepf = [1,3,1,0] #9
octf = [1,3,1,0] #10
novf = [1,4,3,1] #9
decf = [1,0,1,0] #10
most_freq = [1,3,2,5,6,7,8,4,1,4,2,6]
most_symptom = ''
yearf = [janf,febf,marf,aprf,mayf,junf,julf,augf,sepf,octf,novf,decf]
year = ["January","February","March","April","May","June","July","August","September","October","November","December"]


mean,summ,specificmean = 0,0,0
globalmean = 8
globalspecificmean = 4
month_chosen = user_choice[5]
x_ticks, lastweek, resultbar, resultpred, resultspecific  = [],[],[],[],[]

def get_mean():
    global mean
    if month_chosen == 1:
        for i in range(1):
            for x in range(3):
                mean = mean + int(yearf[i][x])
        mean = mean/3
    if month_chosen == 2:
        for i in range(2):
            for x in range(4):
                mean = mean + int(yearf[i][x])
        mean = mean - yearf[1][3]
        mean = mean/7
    if month_chosen == 3:
        for i in range(3):
            for x in range(4):
                mean = mean + int(yearf[i][x])
        mean = mean - yearf[2][3]
        mean = mean/11
    if month_chosen == 4:
        for i in range(4):
            for x in range(4):
                mean = mean + int(yearf[i][x])
        mean = mean - yearf[3][3]
        mean = mean/15
    if month_chosen == 5:
        for i in range(5):
            for x in range(4):
                mean = mean + int(yearf[i][x])
        mean = mean - yearf[4][3]
        mean = mean/19
    if month_chosen == 6:
        for i in range(6):
            for x in range(4):
                mean = mean + int(yearf[i][x])
        mean = mean - yearf[5][3]
        mean = mean/23
    if month_chosen == 7:
        for i in range(7):
            for x in range(4):
                mean = mean + int(yearf[i][x])
        mean = mean - yearf[6][3]
        mean = mean/27
    if month_chosen == 8:
        for i in range(8):
            for x in range(4):
                mean = mean + int(yearf[i][x])
        mean = mean - yearf[7][3]
        mean = mean/31
    if month_chosen == 9:
        for i in range(9):
            for x in range(4):
                mean = mean + int(yearf[i][x])
        mean = mean - yearf[8][3]
        mean = mean/35
    if month_chosen == 10:
        for i in range(10):
            for x in range(4):
                mean = mean + int(yearf[i][x])
        mean = mean - yearf[9][3]
        mean = mean/39
    if month_chosen == 11:
        for i in range(11):
            for x in range(4):
                mean = mean + int(yearf[i][x])
        mean = mean - yearf[10][3]
        mean = mean/43
    if month_chosen == 12:
        for i in range(12):
            for x in range(4):
                mean = mean + int(yearf[i][x])
        mean = mean - yearf[11][3]
        mean = mean/47
    return mean 
    
def get_last_week():
        for i in range(month_chosen):
            lastweek.append(int(yearf[i][3]))
                
get_mean()
get_last_week()

def get_x_ticks():
    for x in range(month_chosen):
        x_ticks.append(year[x])
    return x_ticks

get_x_ticks()


def plot_bar_graph():
    fig = plt.figure()
    ax = fig.add_axes([0.1, 0.135, 0.65, 0.75])
    fig = plt.gcf()
    fig.set_size_inches(9, 7)
    x_plot = [(i+1) for i in range(month_chosen)]
    plt.bar(x_plot,lastweek,alpha=0.5,color='orange')
    plt.xticks(x_plot,x_ticks,rotation=45)
    plt.axhline(y=mean, color='r', linestyle=':',label="Patient's Average")
    plt.axhline(y=globalmean, color='g', linestyle=':',label="World Average")
    plt.title("TOTAL NUMBER OF FATAL SYMPTOMS OF CANCER FOR EACH MONTH")
    plt.ylabel("Frequency of symptoms",style='oblique')
    plt.xlabel("Months",style='oblique')
    plt.legend(bbox_to_anchor=(1.05, 1), loc='upper left', borderaxespad=0.)
    plt.savefig("bar.png")
    return plt.show()
plot_bar_graph()

def get_result_for_bargraph():
    for i in range(len(lastweek)):
        if lastweek[i]>mean and lastweek[i]>globalmean:
            resultbar.append(("Patient's cancer condition is worsening with an extra of %d significant symptoms compared to their average number and an extra %f symptoms compared to global mean a month in %s.")% (round(lastweek[i]-mean),round(lastweek[i]-globalmean),year[i]))
        if lastweek[i]<mean and lastweek[i]>globalmean:
            resultbar.append(("Patient's cancer condition is worsening with an extra of %d significant symptoms compared to the global average number but is improving when compared to their average in %s.")% (round(lastweek[i]-globalmean),year[i]))
        if lastweek[i]>mean and lastweek[i]<globalmean:
            resultbar.append(("Patient's cancer condition is worsening with an extra of %d significant symptoms compared to the thier average number but is improving when compared to global mean in %s.")% (round(lastweek[i]-mean),year[i]))
        if lastweek[i]<mean and lastweek[i]<globalmean:
            resultbar.append(("Patient's cancer condition is improving when compared to their average and global average number of significant symptoms global mean in %s.")% (year[i]))

get_result_for_bargraph()
summ,specificmean = 0,0
def get_specific_mean():
    global summ
    global specificmean
    summ,specificmean=0,0
    for i in range(month_chosen):
        summ=summ+most_freq[i]
    specificmean = (summ)/month_chosen
    return specificmean
get_specific_mean()

y_plot = []
def plot_specific_graph():
    fig = plt.figure()
    ax = fig.add_axes([0.1, 0.135, 0.65, 0.75])
    fig = plt.gcf()
    fig.set_size_inches(9, 7)
    for i in range(month_chosen):
        y_plot.append(most_freq[i])
    x_plot = [(i+1) for i in range(month_chosen)]
    plt.bar(x_plot,y_plot,alpha=0.5,color='blue')
    plt.xticks(x_plot,x_ticks,rotation=45)
    plt.axhline(y=specificmean, color='r', linestyle=':',label="Patient's Average")
    plt.axhline(y=globalspecificmean, color='g', linestyle=':',label="World Average")
    plt.title("FREQUENCY OF PATIENT'S MOST PRONE FATAL SYMPTOM")
    plt.ylabel("Frequency of symptoms",style='oblique')
    plt.xlabel("Months",style='oblique')
    plt.legend(bbox_to_anchor=(1.05, 1), loc='upper left', borderaxespad=0.)
    plt.savefig("specific.png")
    return plt.show()    
plot_specific_graph()
def get_result_for_specificgraph():
    resultspecific.append("Patient's most susceptible and frequently displayed symptom is %s and can be used to gauge how effective treatment is for patient."%(most_symptom))
    for i in range(month_chosen):
        if most_freq[i]>specificmean and most_freq[i]>globalspecificmean:
            resultspecific.append(("Patient's cancer condition is worsening with an extra of %d symptom compared to their average number and an extra %d symptoms compared to global mean a month in %s.")% (round(most_freq[i]-specificmean,2),round(most_freq[i]-globalspecificmean,2),year[i]))
        if most_freq[i]<specificmean and most_freq[i]>globalspecificmean:
            resultspecific.append(("Patient's cancer condition is worsening with an extra of %d symptoms compared to the global average number but is improving when compared to their average in %s.")% (round(most_freq[i]-globalspecificmean,2),year[i]))
        if most_freq[i]>specificmean and most_freq[i]<globalspecificmean:
            resultspecific.append(("Patient's cancer condition is worsening with an extra of %d symptoms compared to the their average number but is improving when compared to global mean in %s.")% (round(most_freq[i]-specificmean,2),year[i]))
        if most_freq[i]<specificmean and most_freq[i]<globalspecificmean:
            resultspecific.append(("Patient's cancer condition is improving when compared to thier average and global average number of significant symptoms global mean in %s.")% (year[i]))
get_result_for_specificgraph()
y_plot_user=[]
y_plot_global = []

def get_yplots():
    length = len(lastweek)
    for i in range(length):
        yu = (mean)/(lastweek[i]+mean)
        y_plot_user.append(yu)
        yg = (globalmean)/(lastweek[i]+mean)
        y_plot_global.append(yg)
    return y_plot_user,y_plot_global
get_yplots()
x_plot = [(i+1) for i in range(month_chosen)]
def plot_pred_graph():
    fig = plt.figure()
    ax = fig.add_axes([0.1, 0.135, 0.65, 0.75])
    fig.set_size_inches(11, 7)
    plt.plot(x_plot,y_plot_user,c='blue',marker='o',label="Based on Patient's average")
    plt.plot(x_plot,y_plot_global,c='black',marker='o',label="Based on World's average")    
    plt.axhline(y=1, color='r', linestyle=':',label = "Stable Marker")
    plt.title("PREDICTION OF PATIENT'S CONDITION IMPROVEMENT")
    plt.xticks(x_plot,x_ticks,rotation=45)
    plt.legend(bbox_to_anchor=(1.05, 1), loc='upper left', borderaxespad=0.)
    plt.xlabel("Month")
    plt.ylabel("Scale of Improvement for Patient's cancer")
    plt.savefig('pred.png')
    return plt.show()
plot_pred_graph()       

def get_result_for_predgraph():
    countuser = 0
    countglobal = 0
    for i in range(month_chosen):
        if y_plot_user[i]>1:
            countuser = countuser+1
    for i in range(month_chosen):
        if y_plot_global[i]>1:
            countglobal =countglobal+1
    resultpred.append("Points above Stable Marker indicates patient's condition has improved due to a decrease in fatal symptoms experienced.")
    resultpred.append("Steepness of line between each point indicates the intensity of improvement change.")
    resultpred.append("Similarly points on the Stable marker indicates patient's condition is stable.") 
    overalmarkermonths = int(round(0.5*month_chosen))
    if countuser > overalmarkermonths:
        resultpred.append(("Patient condition is worsening overall based on patient's average over the progressing %s months")%(str(month_chosen)))
    if countuser < overalmarkermonths:
        resultpred.append(("Patient condition is improving overall based on patient's average over the progressing %s months")%(str(month_chosen)))
    if countuser == overalmarkermonths:
        resultpred.append(("Patient condition is stable overall based on patient's average over the progressing %s months")%(str(month_chosen)))
    if countglobal > overalmarkermonths:
        resultpred.append(("Patient condition is worsening overall based on world's average over the progressing %s months")%(str(month_chosen)))
    if countglobal < overalmarkermonths:
        resultpred.append(("Patient condition is improving overall based on world's average over the progressing %s months")%(str(month_chosen)))
    if countglobal == overalmarkermonths:
        resultpred.append(("Patient condition is stable overall based on world's average over the progressing %s months")%(str(month_chosen)))
get_result_for_predgraph()                          

for i in range(len(resultspecific)):
    print(resultspecific[i])
    print(" ")

for i in range(len(resultbar)):
    print(resultbar[i])
    print(" ")
#------------------------------------------------------------------------------------------------------------------------------------
def get_results():
    import tkinter as tk
    gui_2 = tk.Tk()
    gui_2.geometry("1400x950")
    
#ALL VARIABLES------------------------------------------------------------------------------------------------------------------------------------
    age = str(user_choice[0])
    gender =  str(user_choice[1])
    cancerlocation = str(user_choice[2])
    cancertype = str(user_choice[3][0])
    if len(user_choice[3])==1:
        treatment = 'None'
    else:
        templist=[]
        a=len(user_choice[3])
        for i in range(a-1):
            templist.append(user_choice[3][i+1])
        treatment = ', '.join(i for i in templist)
    stringg = ', '.join(i for i in user_choice[4])
    drugsused = stringg
    monthc =  year[month_chosen-1]
    print(treatment,stringg)
#SCROLLBAR FOR FRAME-------------------------------------------------------------------------------------------------------------------------------------
    def on_configure(event):
        canvas.configure(scrollregion=canvas.bbox('all')) 
    canvas = tk.Canvas(gui_2,width=1380,height=935,bg='red') #width adjusts scroll bar place
    canvas.pack(side=tk.LEFT)
    scrollbar = tk.Scrollbar(gui_2, command=canvas.yview)
    scrollbar.pack(side=tk.LEFT, fill='y')
    canvas.configure(yscrollcommand = scrollbar.set)
    canvas.bind('<Configure>', on_configure)    
    frame = tk.Frame(canvas,width=1380,height=8000) #
    canvas.create_window((0,0),window=frame, anchor='nw')
    cancer_fatal_symptom_sum =['a','b','c','d','e','f','g','h','i','j','ksdfafaefedrwsrwserwre','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
    cancernumber = [12,32,54]
#USER LABELS------------------------------------------------------------------------------------------------------
    userage = tk.Label(frame,text=age,font=('Imago',15),anchor='w')
    usergender = tk.Label(frame, text=gender,font=('Imago',15),anchor='w')
    usercancerlocation = tk.Label(frame, text=cancerlocation,font=('Imago',15),anchor='w')
    usercancertype = tk.Label(frame, text=cancertype,font=('Imago',15),anchor='w')
    usertreatment = tk.Label(frame, text=treatment,font=('Imago',15),anchor='w')
    userdrug = tk.Label(frame, text=drugsused,font=('Imago',15),anchor='w')
    usermonth = tk.Label(frame, text=monthc,font=('Imago',15),anchor='w')
#GENERAL LABELS------------------------------------------------------------------------------------------------------
    lbl = tk.Label(frame, text="Patient's details",font=('Imago',19,'bold'),fg='#0066CC',anchor='w')
    agelbl = tk.Label(frame, text="Age:",font=('Imago',15,'bold'),anchor='w')
    genderlbl = tk.Label(frame, text="Gender:",font=('Imago',15,'bold'),anchor='w')
    cancerlocationlbl = tk.Label(frame, text="Location of cancer:",font=('Imago',15,'bold'),anchor='w')
    cancertypelbl = tk.Label(frame, text="Type of cancer:",font=('Imago',15,'bold'),anchor='w')
    treatmentlbl = tk.Label(frame, text="Type of treament:",font=('Imago',15,'bold'),anchor='w')
    druglbl = tk.Label(frame, text="Roche drug used:",font=('Imago',15,'bold'),anchor='w')
    monthlbl = tk.Label(frame,text="Month of visit:",font=('Imago',15,'bold'),anchor='w')
    text1="SUMMARY OF FATAL CANCER SYMPTOMS EXPERIENCED BY PATIENT IN %s"%(monthc.upper())
    cancerflbl = tk.Label(frame,text=text1,font=('Imago',19,'bold'),anchor='w')
    text2="SUMMARY OF EMERGENCY CANCER SYMPTOMS EXPERIENCED BY PATIENT IN %s"%(monthc.upper())
    cancerelbl = tk.Label(frame,text=text2,font=('Imago',19,'bold'),fg='red',anchor='w')
    canceredesclbl = tk.Label(frame,text="Month of visit:",font=('Imago',15,'bold'),anchor='w')
    text3="SUMMARY OF FATAL DRUG CANCER SYMPTOMS EXPERIENCED BY PATIENT IN %s"%(monthc.upper())
    drugflbl = tk.Label(frame,text=text3,font=('Imago',19,'bold'),anchor='w')
    text4="SUMMARY OF EMERGENCY DRUG SYMPTOMS EXPERIENCED BY PATIENT IN %s"%(monthc.upper())
    drugelbl = tk.Label(frame,text=text4,font=('Imago',19,'bold'),fg='red',anchor='w')
    drugfdesclbl = tk.Label(frame,text="Month of visit:",font=('Imago',15,'bold'),anchor='w')
    drugedesclbl = tk.Label(frame,text="Month of visit:",font=('Imago',15,'bold'),anchor='w')
    resymplbl = tk.Label(frame,text="Month of visit:",font=('Imago',15,'bold'),anchor='w')
    resympdesclbl = tk.Label(frame,text="Month of visit:",font=('Imago',15,'bold'),anchor='w')
    condlbl = tk.Label(frame,text="PATIENT CONDITION REPORT",font=('Imago',19,'bold'),fg='#0066CC',anchor='w')
    speclbl = tk.Label(frame,text="PATIENT'S MOST PRONE SYMPTOM CHART ANALYSIS",font=('Imago',15,'bold'),anchor='w')
    predlbl = tk.Label(frame,text="PATIENT'S CANCER CONDITION PREDICTION ANALYSIS",font=('Imago',15,'bold'),anchor='w')
    barlbl = tk.Label(frame,text="PATIENT'S FATAL SYMPTOM EXPERIENCED ANALYSIS",font=('Imago',15,'bold'),anchor='w')
    sympdclbl = tk.Label(frame,text="SUMMARY OF PATIENT'S RECURRING SYMPTOMS NOT CAUSED BY CANCER OR DRUG",font=('Imago',19,'bold'),anchor='w')
    
#LABELS AND PUTTING IN INFO-----------------------------------------------------------------------------------------------------------------------------------
    originalcolor='#40E0D0'
     
    cancerflbl.place(x=50,y=500)
    cancerflist = tk.Listbox(frame,font=('Imago',16),width=50,height=15)
    cancerflist.place(x=50,y=560)
    for i in range(len(cancer_fatal_symptom_sum)): 
        cancerflist.insert(END, cancer_fatal_symptom_sum[i]) 
    cancerfdesc = "Fatal cancer symptoms displayed by patient should be investigated as soon as possible as this could indicate the worsening of patient's cancer condition"
    cancerfmsg = tk.Message(frame,text=cancerfdesc,font=('Imago',17),width=500)
    cancerfmsg.place(x=740,y=590)
    
    cancerelbl.place(x=50,y=1050)
    cancerelist = tk.Listbox(frame,font=('Imago',16),width=50,height=15)
    cancerelist.place(x=50,y=1110)
    for i in range(len(cancer_fatal_symptom_sum)): 
        cancerelist.insert(END, cancer_fatal_symptom_sum[i]) 
    canceremsg = "Reccuring symptoms not caused by cancer or drug displayed by patient should be tended to immediately as first priority, as this could indicate the worsening of patient's cancer condition"
    canceremsg = tk.Message(frame,text=canceremsg,font=('Imago',17),width=500)
    canceremsg.place(x=740,y=1140)
        
    drugflbl.place(x=50,y=1600)
    drugflist = tk.Listbox(frame,font=('Imago',16),width=50,height=15)
    drugflist.place(x=50,y=1660)
    for i in range(len(cancer_fatal_symptom_sum)): 
        drugflist.insert(END, cancer_fatal_symptom_sum[i]) 
    drugfmsg = "Fatal drug symptoms displayed by patient should be tended to immediately as first priority, as this could indicate the worsening of patient's cancer condition"
    drugfmsg = tk.Message(frame,text=drugfmsg,font=('Imago',17),width=500)
    drugfmsg.place(x=740,y=1690)
                
    drugelbl.place(x=50,y=2150)
    drugelist = tk.Listbox(frame,font=('Imago',16),width=50,height=15)
    drugelist.place(x=50,y=2210)
    for i in range(len(cancer_fatal_symptom_sum)): 
        drugelist.insert(END, cancer_fatal_symptom_sum[i]) 
    drugemsg = "Fatal emergency drug symptoms displayed by patient should be tended to immediately as first priority, as this could indicate the worsening of patient's cancer condition"
    drugemsg = tk.Message(frame,text=drugemsg,font=('Imago',17),width=500)
    drugemsg.place(x=740,y=2240)

    sympdclbl.place(x=50,y=2700)
    sympdclist = tk.Listbox(frame,font=('Imago',16),width=50,height=15)
    sympdclist.place(x=50,y=2760)
    for i in range(len(cancer_fatal_symptom_sum)): 
        sympdclist.insert(END, cancer_fatal_symptom_sum[i]) 
    sympdct = "Fatal emergency drug symptoms displayed by patient should be tended to immediately as first priority, as this could indicate the worsening of patient's cancer condition"
    sympdcmsg = tk.Message(frame,text=sympdct,font=('Imago',17),width=500)
    sympdcmsg.place(x=740,y=2790)
        
    
    gbar = tk.PhotoImage(file='bar.png')
    labelbar = tk.Label(frame, image = gbar)    
    barlbl.place(x=50,y=2850)
    labelbar.place(x=50, y=2900)

    gspecific = tk.PhotoImage(file ='specific.png')
    labelspecific = tk.Label(frame, image = gspecific)
    speclbl.place(x=50,y=3850)
    labelspecific.place(x=50,y=3900)
    
    gpred = tk.PhotoImage(file='pred.png')
    labelpred = tk.Label(frame, image = gpred)
    predlbl.place(x=50,y=4850)
    labelpred.place(x=50,y=4900)
    
    lbl.place(x=50,y=30) #x+300,y+40
    agelbl.place(x=50,y=90)
    userage.place(x=300,y=90)
    genderlbl.place(x=50,y=140)
    usergender.place(x=300,y=140)
    cancerlocationlbl.place(x=50, y=190)
    usercancerlocation.place(x=300,y=190)
    cancertypelbl.place(x=50,y=240) #x+250,y+50
    usercancertype.place(x=300,y=240)
    treatmentlbl.place(x=50,y=290)
    usertreatment.place(x=300,y=290)
    druglbl.place(x=50,y=340)
    userdrug.place(x=300,y=340)
    monthlbl.place(x=50,y=390)
    usermonth.place(x=300,y=390)
    
    


    
    # --- start program ---
    gui_2.mainloop()

get_results()
'''