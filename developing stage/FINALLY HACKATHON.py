#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Nov  6 02:21:02 2020

@author: piaoruilin
"""

import csv
import numpy as np
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
                  text="""Which drugs are currenly used to treat patient?""",
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


#SECTION: SORTING (RUILIN)
#--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#sort and compare user choice with symptoms

import operator 

user_choice = [12, 'Male', 'Brain', ['Glioblastoma', 'Recurrance Treatment'], ['Avastin', 'Kadcyla'], 4]

#Getting rid of 1st and 2nd element in user_choice array
index = [0,1]
new_user_choice = [i for i in user_choice if user_choice.index(i) not in index]

#Sorting out drug symptoms and putting them into an array
drugs_list = []
drugs = open(str(drugsheet), 'r')
csv1 = csv.reader(drugs, delimiter=',')
sort = sorted(csv1, key=operator.itemgetter(0))
for eachline in sort :
    drug_array = eachline
    drugs_list.append(drug_array)
    
#Sorting out other symptoms and putting them into an array
others_list = []
others = open(str(othersheet),'r')
csv3 = csv.reader(others, delimiter=',')
sort3 = sorted(csv3, key=operator.itemgetter(0))
for eachline_2 in sort3 :
    other_array = eachline_2
    others_list.append(other_array)

#Sorting out symptom chart and putting them into an array
symptom_list = []
chart = open(str(symptomsheet), 'r')
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

#FAKING DATA--------------------------------------------------------------------------------------------------------------------------------------------------
#Sorting out cancer symptoms and putting them into an array
import operator
import random

#Sorting CSV files------------------------------------------------------------------------------------------------------------------------
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
cancer = open('/Users/piaoruilin/Desktop/Hackathon Data - Cancer Symptom-2.csv', 'r')
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
    
#Sorting out recurring symptom chart and putting them into an array
recurring_list = []
recurring = open("/Users/piaoruilin/Desktop/python/Hackathon Data - Recurring Symptoms.csv", 'r')
csv5 = csv.reader(recurring, delimiter=',')
sort5 = sorted(csv5, key=operator.itemgetter(0))
for eachline_4 in sort5 :
    recurring_array = eachline_4
    recurring_list.append(recurring_array)

#Faking the symptoms---------------------------------------------------------------------------------------------------------------------

user_choice = [12, 'Male', 'Brain', ['Glioblastoma', 'Recurrance Treatment'], ['Avastin', 'Kadcyla'], 4]

#Getting rid of 1st and 2nd element in user_choice array
index = [0,1]
new_user_choice = [i for i in user_choice if user_choice.index(i) not in index]
print(new_user_choice)

#CANCER FATAL FAKE

new_cancer_list = []
for i in range(len(cancer_list)):
    if new_user_choice[0]==cancer_list[i][0]:
        new_cancer_list.append(cancer_list[i])

for i in range(len(new_cancer_list)):
    new_cancer_list[i].pop(0)
    
cancer_fatal=[],[],[],[],[],[],[],[],[],[],[],[] #jan,feb,mar,apr,may,jun,jul,aug,sep,oct,nov,dec
for n in range(random.randint(4,10)):
    a = random.randint(1,15)
    jan_cancer_fatal=new_cancer_list[a]
    cancer_fatal[0].append(jan_cancer_fatal)
for n in range(random.randint(4,10)):
    a = random.randint(1,15)
    feb_cancer_fatal=new_cancer_list[a]
    cancer_fatal[1].append(feb_cancer_fatal)
for n in range(random.randint(4,10)):
    a = random.randint(1,15)
    mar_cancer_fatal=new_cancer_list[a]
    cancer_fatal[2].append(mar_cancer_fatal)
for n in range(random.randint(4,10)):
    a = random.randint(1,15)
    apr_cancer_fatal=new_cancer_list[a]
    cancer_fatal[3].append(apr_cancer_fatal)
for n in range(random.randint(4,10)):
    a = random.randint(1,15)
    may_cancer_fatal=new_cancer_list[a]
    cancer_fatal[4].append(may_cancer_fatal)
for n in range(random.randint(4,10)):
    a = random.randint(1,15)
    jun_cancer_fatal=new_cancer_list[a]
    cancer_fatal[5].append(jun_cancer_fatal)
for n in range(random.randint(4,10)):
    a = random.randint(1,15)
    jul_cancer_fatal=new_cancer_list[a]
    cancer_fatal[6].append(jul_cancer_fatal)
for n in range(random.randint(4,10)):
    a = random.randint(1,15)
    aug_cancer_fatal=new_cancer_list[a]
    cancer_fatal[7].append(aug_cancer_fatal)
for n in range(random.randint(4,10)):
    a = random.randint(1,15)
    sep_cancer_fatal=new_cancer_list[a]
    cancer_fatal[8].append(sep_cancer_fatal)
for n in range(random.randint(4,10)):
    a = random.randint(1,15)
    octo_cancer_fatal=new_cancer_list[a]
    cancer_fatal[9].append(octo_cancer_fatal)
for n in range(random.randint(4,10)):
    a = random.randint(1,15)
    nov_cancer_fatal=new_cancer_list[a]
    cancer_fatal[10].append(nov_cancer_fatal)
for n in range(random.randint(4,10)):
    a = random.randint(1,15)
    dec_cancer_fatal=new_cancer_list[a]
    cancer_fatal[11].append(dec_cancer_fatal)
    
#DRUGS FATAL FAKE
new_drugs_list = []
for i in range(len(drugs_list)):
    if new_user_choice[0]==drugs_list[i][0] and new_user_choice[1][0]==drugs_list[i][1]:
        new_drugs_list.append(drugs_list[i])

fatal_drugs_list = []
for m in range(len(new_drugs_list)):
    if new_drugs_list[m][6]=='1':
        fatal_drugs_list.append(new_drugs_list[m])    #find fatal

fatal_drugs = []
for i in range(len(fatal_drugs_list)): #get rid of unnessacry index
    v=[fatal_drugs_list[i][3],fatal_drugs_list[i][4]]
    fatal_drugs.append(v)

drugs_fatal=[],[],[],[],[],[],[],[],[],[],[],[]   #jan,feb,mar,apr,may,jun,jul,aug,sep,oct,nov,dec
for n in range(random.randint(3,8)):
    b = random.randint(1,10)
    jan_drugs_fatal=fatal_drugs[b]
    drugs_fatal[0].append(jan_drugs_fatal)
for n in range(random.randint(3,8)):
    b = random.randint(1,10)
    feb_drugs_fatal=fatal_drugs[b]
    drugs_fatal[1].append(feb_drugs_fatal)
for n in range(random.randint(3,8)):
    b = random.randint(1,10)
    mar_drugs_fatal=fatal_drugs[b]
    drugs_fatal[2].append(mar_drugs_fatal)
for n in range(random.randint(3,8)):
    b = random.randint(1,10)
    apr_drugs_fatal=fatal_drugs[b]
    drugs_fatal[3].append(apr_drugs_fatal)
for n in range(random.randint(3,8)):
    b = random.randint(1,10)
    may_drugs_fatal=fatal_drugs[b]
    drugs_fatal[4].append(may_drugs_fatal)
for n in range(random.randint(3,8)):
    b = random.randint(1,10)
    jun_drugs_fatal=fatal_drugs[b]
    drugs_fatal[5].append(jun_drugs_fatal)
for n in range(random.randint(3,8)):
    b = random.randint(1,10)
    jul_drugs_fatal=fatal_drugs[b]
    drugs_fatal[6].append(jul_drugs_fatal)
for n in range(random.randint(3,8)):
    b = random.randint(1,10)
    aug_drugs_fatal=fatal_drugs[b]
    drugs_fatal[7].append(aug_drugs_fatal)
for n in range(random.randint(3,8)):
    b = random.randint(1,10)
    sep_drugs_fatal=fatal_drugs[b]
    drugs_fatal[8].append(sep_drugs_fatal)
for n in range(random.randint(3,8)):
    b = random.randint(1,10)
    octo_drugs_fatal=fatal_drugs[b]
    drugs_fatal[9].append(octo_drugs_fatal)
for n in range(random.randint(3,8)):
    b = random.randint(1,10)
    nov_drugs_fatal=fatal_drugs[b]
    drugs_fatal[10].append(nov_drugs_fatal)
for n in range(random.randint(3,8)):
    b = random.randint(1,10)
    dec_drugs_fatal=fatal_drugs[b]
    drugs_fatal[11].append(dec_drugs_fatal)
print(drugs_fatal)

#DRUGS EMERGENCY
emergency_drugs_list = []
for m in range(len(new_drugs_list)):
    if new_drugs_list[m][7]=='1':
        emergency_drugs_list.append(new_drugs_list[m])    #find emergency

emergency_drugs = []
for i in range(len(emergency_drugs_list)): #get rid of unnessacry index
    w=[emergency_drugs_list[i][3],emergency_drugs_list[i][4]]
    emergency_drugs.append(w)

drugs_emergency=[[],[],[],[],[],[],[],[],[],[],[],[]]#jan,feb,mar,apr,may,jun,jul,aug,sep,oct,nov,dec
for n in range(random.randint(3,8)):
    b = random.randint(1,10)
    jan_drugs_emergency=emergency_drugs[b]
    drugs_emergency[0].append(jan_drugs_emergency)
for n in range(random.randint(3,8)):
    b = random.randint(1,10)
    feb_drugs_emergency=emergency_drugs[b]
    drugs_emergency[1].append(feb_drugs_emergency)
for n in range(random.randint(3,8)):
    b = random.randint(1,10)
    mar_drugs_emergency=emergency_drugs[b]
    drugs_emergency[2].append(mar_drugs_emergency)
for n in range(random.randint(3,8)):
    b = random.randint(1,10)
    apr_drugs_emergency=emergency_drugs[b]
    drugs_emergency[3].append(apr_drugs_emergency)
for n in range(random.randint(3,8)):
    b = random.randint(1,10)
    may_drugs_emergency=emergency_drugs[b]
    drugs_emergency[4].append(may_drugs_emergency)
for n in range(random.randint(3,8)):
    b = random.randint(1,10)
    jun_drugs_emergency=emergency_drugs[b]
    drugs_emergency[5].append(jun_drugs_emergency)
for n in range(random.randint(3,8)):
    b = random.randint(1,10)
    jul_drugs_emergency=emergency_drugs[b]
    drugs_emergency[6].append(jul_drugs_emergency)
for n in range(random.randint(3,8)):
    b = random.randint(1,10)
    aug_drugs_emergency=emergency_drugs[b]
    drugs_emergency[7].append(aug_drugs_emergency)
for n in range(random.randint(3,8)):
    b = random.randint(1,10)
    sep_drugs_emergency=emergency_drugs[b]
    drugs_emergency[8].append(sep_drugs_emergency)
for n in range(random.randint(3,8)):
    b = random.randint(1,10)
    octo_drugs_emergency=emergency_drugs[b]
    drugs_emergency[9].append(octo_drugs_emergency)
for n in range(random.randint(3,8)):
    b = random.randint(1,10)
    nov_drugs_emergency=emergency_drugs[b]
    drugs_emergency[10].append(nov_drugs_emergency)
for n in range(random.randint(3,8)):
    b = random.randint(1,10)
    dec_drugs_emergency=emergency_drugs[b]
    drugs_emergency[11].append(dec_drugs_emergency)

#OTHER FATAL FAKE
other_fatal = []
for s in range(len(others_list)):
    if others_list[s][2]=='1':
        other_fatal.append(others_list[s]) 
for x in range(len(other_fatal)):
    other_fatal[x].pop(2)
    
others_fatal=[[],[],[],[],[],[],[],[],[],[],[],[]] #jan,feb,mar,apr,may,jun,jul,aug,sep,oct,nov,dec
for n in range(random.randint(2,5)):
    a = random.randint(1,10)
    jan_others_fatal=other_fatal[a]
    others_fatal[0].append(jan_others_fatal)
for n in range(random.randint(2,5)):
    a = random.randint(1,10)
    feb_others_fatal=other_fatal[a]
    others_fatal[1].append(feb_others_fatal)
for n in range(random.randint(2,5)):
    a = random.randint(1,10)
    mar_others_fatal=other_fatal[a]
    others_fatal[2].append(mar_others_fatal)
for n in range(random.randint(2,5)):
    a = random.randint(1,10)
    apr_others_fatal=other_fatal[a]
    others_fatal[3].append(apr_others_fatal)
for n in range(random.randint(2,5)):
    a = random.randint(1,10)
    may_others_fatal=other_fatal[a]
    others_fatal[4].append(may_others_fatal)
for n in range(random.randint(2,5)):
    a = random.randint(1,10)
    jun_others_fatal=other_fatal[a]
    others_fatal[5].append(jun_others_fatal)
for n in range(random.randint(2,5)):
    a = random.randint(1,10)
    jul_others_fatal=other_fatal[a]
    others_fatal[6].append(jul_others_fatal)
for n in range(random.randint(2,5)):
    a = random.randint(1,10)
    aug_others_fatal=other_fatal[a]
    others_fatal[7].append(aug_others_fatal)
for n in range(random.randint(2,5)):
    a = random.randint(1,10)
    sep_others_fatal=other_fatal[a]
    others_fatal[8].append(sep_others_fatal)
for n in range(random.randint(2,5)):
    a = random.randint(1,10)
    octo_others_fatal=other_fatal[a]
    others_fatal[9].append(octo_others_fatal)
for n in range(random.randint(2,5)):
    a = random.randint(1,10)
    nov_others_fatal=other_fatal[a]
    others_fatal[10].append(nov_others_fatal)
for n in range(random.randint(2,5)):
    a = random.randint(1,10)
    dec_others_fatal=other_fatal[a]
    others_fatal[11].append(dec_others_fatal)
    
#RECURRING SYMPTOMS FAKE
new_recurring_list = []
for i in range(len(recurring_list)):
    if new_user_choice[0]==recurring_list[i][0]:
        new_recurring_list.append(recurring_list[i])
for x in range(len(new_recurring_list)):
    new_recurring_list[x].pop(0)

recur=[[],[],[],[],[],[],[],[],[],[],[],[]] #jan,feb,mar,apr,may,jun,jul,aug,sep,oct,nov,dec
for n in range(random.randint(2,5)):
    a = random.randint(1,3)
    jan_recur=new_recurring_list[a]
    recur[0].append(jan_recur)
for n in range(random.randint(2,5)):
    a = random.randint(1,3)
    feb_recur=new_recurring_list[a]
    recur[1].append(feb_recur)
for n in range(random.randint(2,5)):
    a = random.randint(1,3)
    mar_recur=new_recurring_list[a]
    recur[2].append(mar_recur)
for n in range(random.randint(2,5)):
    a = random.randint(1,3)
    apr_recur=new_recurring_list[a]
    recur[3].append(apr_recur)
for n in range(random.randint(2,5)):
    a = random.randint(1,3)
    may_recur=new_recurring_list[a]
    recur[4].append(may_recur)
for n in range(random.randint(2,5)):
    a = random.randint(1,3)
    jun_recur=new_recurring_list[a]
    recur[5].append(jun_recur)
for n in range(random.randint(2,5)):
    a = random.randint(1,3)
    jul_recur=new_recurring_list[a]
    recur[6].append(jul_recur)
for n in range(random.randint(2,5)):
    a = random.randint(1,3)
    aug_recur=new_recurring_list[a]
    recur[7].append(aug_recur)
for n in range(random.randint(2,5)):
    a = random.randint(1,3)
    sep_recur=new_recurring_list[a]
    recur[8].append(sep_recur)
for n in range(random.randint(2,5)):
    a = random.randint(1,3)
    octo_recur=new_recurring_list[a]
    recur[9].append(octo_recur)
for n in range(random.randint(2,5)):
    a = random.randint(1,3)
    nov_recur=new_recurring_list[a]
    recur[10].append(nov_recur)
for n in range(random.randint(2,5)):
    a = random.randint(1,3)
    dec_recur=new_recurring_list[a]
    recur[11].append(dec_recur)
    
#SORT BY MONTH
a = new_user_choice[-1]
fatalfatal_cancer = cancer_fatal[a]
fatalfatal_drug = drugs_fatal[a]
fatalfatal_others = others_fatal[a]
emergencyemergency_drug = drugs_emergency[a]
recurring_recur = recur[a]

#RANDOM WHETHER CANCER OR DRUG------------------------------------------------------------------------------------------------------------
choice = ['Cancer', 'Drug']
one = random.choice(choice)
for i in range(len(recurring_recur)):
    diff = recurring_recur[i]
    randomi = random.choice(diff)
    final = str(randomi)[2:-2]
    
difference = final, '-', one

#----------------------------------------------------------------------------------------------------------------------------


#Comparing user choice with cancer symptoms and sorting by the area of cancer
new_cancer_list=[]
for i in range(len(cancer_list)):
    if new_user_choice[0]==cancer_list[i][0]:
        string = "%s, %s"%(cancer_list[i][1],cancer_list[i][2])
        new_cancer_list.append(string)

#Finding most frequent symptom of the month-------------------------------------------------------------------------------------------
#declare month arrays
#january[[day1],[day2],[day3],...]
#day1[symptom1, symptom2, symptom3,...]

#SECTION: GETTING RESULTS
#--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
janf = [2,6,3,6] #10
febf = [9,3,1,5] #8
marf = [5,1,2,2] #10
aprf = [5,0,2,3] #9
mayf = [1,2,3,1] #10
junf = [1,1,0,0] #9
julf = [1,1,2,1] #10
augf = [1,4,1,1] #10
sepf = [1,3,1,0] #9
octf = [1,3,1,0] #10
novf = [1,4,3,1] #9
decf = [1,0,1,0] #10
most_freq = [23,13,6,3,2,6,8,5,12,1,13,25]
most_symptom = ""
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
            resultbar.append(("Patient's cancer condition is worsening with an extra of %d significant symptoms compared to their average number and an extra %d symptoms compared to global mean a month in %s.")% (round(lastweek[i]-mean),round(lastweek[i]-globalmean),year[i]))
        if lastweek[i]<mean and lastweek[i]>globalmean:
            resultbar.append(("Patient's cancer condition is worsening with an extra of %d significant symptoms compared to the global average number but is improving when compared to their average in %s.")% (round(lastweek[i]-globalmean),year[i]))
        if lastweek[i]>mean and lastweek[i]<globalmean:
            resultbar.append(("Patient's cancer condition is worsening with an extra of %d significant symptoms compared to the their average number but is improving when compared to global mean in %s.")% (round(lastweek[i]-mean),year[i]))
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
            resultspecific.append(("Patient's cancer condition is improving when compared to their average and global average number of significant symptoms global mean in %s.")% (year[i]))
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
    print(resultbar)
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
    text2="SUMMARY OF POSSIBLE CAUSE OF SYMPTOMS %s"%(monthc.upper())
    cdlbl = tk.Label(frame,text=text2,font=('Imago',19,'bold'),anchor='w')
    text3="SUMMARY OF FATAL DRUG CANCER SYMPTOMS EXPERIENCED BY PATIENT IN %s"%(monthc.upper())
    drugflbl = tk.Label(frame,text=text3,font=('Imago',19,'bold'),anchor='w')
    text4="SUMMARY OF EMERGENCY DRUG SYMPTOMS EXPERIENCED BY PATIENT IN %s"%(monthc.upper())
    drugelbl = tk.Label(frame,text=text4,font=('Imago',19,'bold'),fg='red',anchor='w')
    drugfdesclbl = tk.Label(frame,text="Month of visit:",font=('Imago',15,'bold'),anchor='w')
    drugedesclbl = tk.Label(frame,text="Month of visit:",font=('Imago',15,'bold'),anchor='w')
    resymplbl = tk.Label(frame,text="Month of visit:",font=('Imago',15,'bold'),anchor='w')
    resympdesclbl = tk.Label(frame,text="Month of visit:",font=('Imago',15,'bold'),anchor='w')
    condlbl = tk.Label(frame,text="PATIENT CONDITION REPORT",font=('Imago',19,'bold'),fg='#0066CC',anchor='w')
    speclbl = tk.Label(frame,text="PATIENT'S MOST PRONE SYMPTOM CHART ANALYSIS",font=('Imago',19,'bold'),anchor='w')
    predlbl = tk.Label(frame,text="PATIENT'S CANCER CONDITION PREDICTION ANALYSIS",font=('Imago',19,'bold'),anchor='w')
    barlbl = tk.Label(frame,text="PATIENT'S FATAL SYMPTOM EXPERIENCED ANALYSIS",font=('Imago',19,'bold'),anchor='w')
    sympdclbl = tk.Label(frame,text="SUMMARY OF PATIENT'S RECURRING SYMPTOMS NOT CAUSED BY CANCER AND DRUG",font=('Imago',19,'bold'),anchor='w')
    
#LABELS AND PUTTING IN INFO-----------------------------------------------------------------------------------------------------------------------------------
    originalcolor='#40E0D0'
     
    cancerflbl.place(x=50,y=500)
    cancerflist = tk.Listbox(frame,font=('Imago',16),width=50,height=15)
    cancerflist.place(x=50,y=560)
    for i in range(len(fatalfatal_cancer)): 
        cancerflist.insert(END, fatalfatal_cancer[i]) #change this 
    cancerfdesc = "Fatal cancer symptoms displayed by patient should be investigated as soon as possible as this could indicate the worsening of patient's cancer condition"
    cancerfmsg = tk.Message(frame,text=cancerfdesc,font=('Imago',17),width=500)
    cancerfmsg.place(x=740,y=590)

    drugflbl.place(x=50,y=1050)
    drugflist = tk.Listbox(frame,font=('Imago',16),width=50,height=15)
    drugflist.place(x=50,y=1110)
    for i in range(len(fatalfatal_drugs)): 
        drugflist.insert(END, fatalfatal_drugs[i]) #change this #change this 
    drugfmsg = "Fatal drug symptoms displayed by patient should be tended to immediately as first priority, as this could indicate the worsening of patient's cancer condition"
    drugfmsg = tk.Message(frame,text=drugfmsg,font=('Imago',17),width=500)
    drugfmsg.place(x=740,y=1140)
                 
    
    drugelbl.place(x=50,y=1600)
    drugelist = tk.Listbox(frame,font=('Imago',16),width=50,height=15)
    drugelist.place(x=50,y=1660)
    for i in range(len(emergencyemergency_drugs)): 
        drugelist.insert(END, emergencyemergencydrugs[i]) #change this 
    drugemsg = "Fatal emergency drug symptoms displayed by patient should be tended to immediately as first priority, as this could indicate the worsening of patient's cancer condition"
    drugemsg = tk.Message(frame,text=drugemsg,font=('Imago',17),width=500)
    drugemsg.place(x=740,y=1690)
 
    cdlbl.place(x=50,y=2150) #CHANGE THIS/check
    cdlist = tk.Listbox(frame,font=('Imago',16),width=50,height=15)
    cdlist.place(x=50,y=2210)
    for i in range(len(difference)): 
        cdlist.insert(END, difference[i]) #change this 
    cdmsg = "The source of symptom is sorted by its cause for symptoms that overlap in drug and cancer."
    cdmsg = tk.Message(frame,text=cdmsg,font=('Imago',17),width=500)
    cdmsg.place(x=740,y=2240)       
    
    sympdclbl.place(x=50,y=2700) #CHANGE THIS
    sympdclist = tk.Listbox(frame,font=('Imago',16),width=50,height=15)
    sympdclist.place(x=50,y=2760)
    for i in range(len(fatalfatal_others)): 
        sympdclist.insert(END, fatalfatal_others[i]) 
    sympdct = "Reccuring symptoms not caused by cancer or drug displayed by patient as it could potentially be a new symptom of cancer/drug"
    sympdcmsg = tk.Message(frame,text=sympdct,font=('Imago',17),width=500)
    sympdcmsg.place(x=740,y=2790)
    
    
#function to print
    def print_results_in_gui(array,yval):
        for i in range(len(array)):
            yax=yval+(110*i)
            tk.Message(frame, text=array[i],font=('Imago',16),width=600).place(x=740,y=yax)
    def print_results_in_gui_2(array,yval):
       for i in range(len(array)):
           yax=yval+(110*i)
           tk.Message(frame, text=array[i],font=('Imago',16),width=400).place(x=850,y=yax)           
# GRAPHS
    gbar = tk.PhotoImage(file='bar.png')
    labelbar = tk.Label(frame, image = gbar)    
    barlbl.place(x=50,y=3400)
    labelbar.place(x=50, y=3450)
    print_results_in_gui(resultbar,3450)
    
    gspecific = tk.PhotoImage(file ='specific.png')
    labelspecific = tk.Label(frame, image = gspecific)
    speclbl.place(x=50,y=5000)
    labelspecific.place(x=50,y=5050)
    print_results_in_gui(resultspecific,5050)
    
    gpred = tk.PhotoImage(file='pred.png')
    labelpred = tk.Label(frame, image = gpred)
    predlbl.place(x=50,y=6300)
    labelpred.place(x=50,y=6350)
    print_results_in_gui_2(resultpred,6350)
    
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