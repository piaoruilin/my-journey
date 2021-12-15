#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Nov  2 14:17:08 2020

@author: piaoruilin
"""

import tkinter as tk 
import time

#SECTION: GETTING USER INFO FROM GUI
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
                  text="""Please selent patient's gender""",
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
                                    if option1 ==1:
                                        user_choice[3].append('Metastatic, Prior Treatment')
                                        user_choice[4].append(drugoptions)
                                    elif option2 ==1:
                                        user_choice[3].append('Recurrance Treatment')
                                        user_choice[4].append(drugoptions)   
                                    elif option1 ==1 and option2 ==1:
                                        user_choice[3].append('Metastatic, Prior Treatment','Recurrance Treatment')
                                        user_choice[4].append(drugoptions)   
                                    print(user_choice)
                                    def store_show_month():
                                        user_month = month_user.get()
                                        user_choice.append(user_month)
                                        print(user_choice)
                                        def close_window():
                                            time.sleep(3)
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
                                    q6.place(x=500,y=525)
                                    p.config(text = "Progress: 6/7")                                
                                btn1 = tk.Checkbutton(gui_1, text=toptions[0], variable=treatment_user_1, width = 20,font=('Imago',13),anchor ='w')
                                btn1.place(x=500,y=375)
                                btn2 = tk.Checkbutton(gui_1, text=toptions[1], variable=treatment_user_2, width = 20,font=('Imago',13),anchor ='w')
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
                                
                                    if option1 ==1:
                                        user_choice[3].append('Metastatic, Prior Treatment')
                                        user_choice[4].append(drugoptions)
                                    elif option2 ==1:
                                        user_choice[3].append('Recurrance Treatment')
                                        user_choice[4].append(drugoptions)   
                                    elif option1 ==1 and option2 ==1:
                                        user_choice[3].append('Metastatic, Prior Treatment','Recurrance Treatment')
                                        user_choice[4].append(drugoptions)   
                                    print(user_choice)
                                    def store_show_month():
                                        user_month = month_user.get()
                                        user_choice.append(user_month)
                                        print(user_choice)
                                        def close_window():
                                            time.sleep(3)
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
                                btn1 = tk.Checkbutton(gui_1, text=toptions[0], variable=treatment_user_1, width = 25,font=('Imago',13),anchor ='w')
                                btn1.place(x=500,y=290)
                                btn2 = tk.Checkbutton(gui_1, text=toptions[1], variable=treatment_user_2, width = 25,font=('Imago',13),anchor ='w')
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
                                
                                    if option1 ==1:
                                        user_choice[3].append('Metastatic, Prior Treatment')
                                        user_choice[4].append(drugoptions)
                                    elif option2 ==1:
                                        user_choice[3].append('Recurrance Treatment')
                                        user_choice[4].append(drugoptions)   
                                    elif option1 ==1 and option2 ==1:
                                        user_choice[3].append('Metastatic, Prior Treatment','Recurrance Treatment')
                                        user_choice[4].append(drugoptions)   
                                    print(user_choice)
                                    def store_show_month():
                                        user_month = month_user.get()
                                        user_choice.append(user_month)
                                        print(user_choice)
                                        def close_window():
                                            time.sleep(3)
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
                                btn1 = tk.Checkbutton(gui_1, text=toptions[0], variable=treatment_user_1, width = 20,font=('Imago',13),anchor ='w')
                                btn1.place(x=500,y=295)
                                btn2 = tk.Checkbutton(gui_1, text=toptions[1], variable=treatment_user_2, width = 20,font=('Imago',13),anchor ='w')
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
                                
                                    if option1 ==1:
                                        user_choice[3].append('Metastatic, Prior Treatment')
                                        user_choice[4].append(drugoptions)
                                    elif option2 ==1:
                                        user_choice[3].append('Recurrance Treatment')
                                        user_choice[4].append(drugoptions)   
                                    elif option1 ==1 and option2 ==1:
                                        user_choice[3].append('Metastatic, Prior Treatment','Recurrance Treatment')
                                        user_choice[4].append(drugoptions)   
                                    print(user_choice)
                                    def store_show_month():
                                        user_month = month_user.get()
                                        user_choice.append(user_month)
                                        print(user_choice)
                                        def close_window():
                                            time.sleep(3)
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
                                btn1 = tk.Checkbutton(gui_1, text=toptions[0], variable=treatment_user_1, width = 20,font=('Imago',13),anchor ='w')
                                btn1.place(x=500,y=230)
                                btn2 = tk.Checkbutton(gui_1, text=toptions[1], variable=treatment_user_2, width = 20,font=('Imago',13),anchor ='w')
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
                        
                    #Q5 START HERE
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
                                
                                    if option1 ==1:
                                        user_choice[3].append('Metastatic, Prior Treatment')
                                        user_choice[4].append(drugoptions)
                                    elif option2 ==1:
                                        user_choice[3].append('Recurrance Treatment')
                                        user_choice[4].append(drugoptions)   
                                    elif option1 ==1 and option2 ==1:
                                        user_choice[3].append('Metastatic, Prior Treatment','Recurrance Treatment')
                                        user_choice[4].append(drugoptions)   
                                    print(user_choice)
                                    def store_show_month():
                                        user_month = month_user.get()
                                        user_choice.append(user_month)
                                        print(user_choice)
                                        def close_window():
                                            time.sleep(3)
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
                                btn1 = tk.Checkbutton(gui_1, text=toptions[0], variable=treatment_user_1, width = 20,font=('Imago',13),anchor ='w')
                                btn1.place(x=500,y=250)
                                btn2 = tk.Checkbutton(gui_1, text=toptions[1], variable=treatment_user_2, width = 20,font=('Imago',13),anchor ='w')
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
                                
                                    if option1 ==1:
                                        user_choice[3].append('Metastatic, Prior Treatment')
                                        user_choice[4].append(drugoptions)
                                    elif option2 ==1:
                                        user_choice[3].append('Recurrance Treatment')
                                        user_choice[4].append(drugoptions)   
                                    elif option1 ==1 and option2 ==1:
                                        user_choice[3].append('Metastatic, Prior Treatment','Recurrance Treatment')
                                        user_choice[4].append(drugoptions)   
                                    print(user_choice)
                                    def store_show_month():
                                        user_month = month_user.get()
                                        user_choice.append(user_month)
                                        print(user_choice)
                                        def close_window():
                                            time.sleep(3)
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
                                        yval = + 30*(i)
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
                                btn1 = tk.Checkbutton(gui_1, text=toptions[0], variable=treatment_user_1, width = 20,font=('Imago',13),anchor ='w')
                                btn1.place(x=500,y=355)
                                btn2 = tk.Checkbutton(gui_1, text=toptions[1], variable=treatment_user_2, width = 20,font=('Imago',13),anchor ='w')
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
                                
                                    if option1 ==1:
                                        user_choice[3].append('Metastatic, Prior Treatment')
                                        user_choice[4].append(drugoptions)
                                    elif option2 ==1:
                                        user_choice[3].append('Recurrance Treatment')
                                        user_choice[4].append(drugoptions)   
                                    elif option1 ==1 and option2 ==1:
                                        user_choice[3].append('Metastatic, Prior Treatment','Recurrance Treatment')
                                        user_choice[4].append(drugoptions)   
                                    print(user_choice)
                                    def store_show_month():
                                        user_month = month_user.get()
                                        user_choice.append(user_month)
                                        print(user_choice)
                                        def close_window():
                                            time.sleep(3)
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
                                btn1 = tk.Checkbutton(gui_1, text=toptions[0], variable=treatment_user_1, width = 20,font=('Imago',13),anchor ='w')
                                btn1.place(x=500,y=250)
                                btn2 = tk.Checkbutton(gui_1, text=toptions[1], variable=treatment_user_2, width = 20,font=('Imago',13),anchor ='w')
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
                                
                                    if option1 ==1:
                                        user_choice[3].append('Metastatic, Prior Treatment')
                                        user_choice[4].append(drugoptions)
                                    elif option2 ==1:
                                        user_choice[3].append('Recurrance Treatment')
                                        user_choice[4].append(drugoptions)   
                                    elif option1 ==1 and option2 ==1:
                                        user_choice[3].append('Metastatic, Prior Treatment','Recurrance Treatment')
                                        user_choice[4].append(drugoptions)   
                                    print(user_choice)
                                    def store_show_month():
                                        user_month = month_user.get()
                                        user_choice.append(user_month)
                                        print(user_choice)
                                        def close_window():
                                            time.sleep(3)
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
                                btn1 = tk.Checkbutton(gui_1, text=toptions[0], variable=treatment_user_1, width = 20,font=('Imago',13),anchor ='w')
                                btn1.place(x=500,y=250)
                                btn2 = tk.Checkbutton(gui_1, text=toptions[1], variable=treatment_user_2, width = 20,font=('Imago',13),anchor ='w')
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
                                if option1 ==1:
                                    user_choice[3].append('Metastatic, Prior Treatment')
                                    user_choice[4].append(drugoptions)
                                elif option2 ==1:
                                    user_choice[3].append('Recurrance Treatment')
                                    user_choice[4].append(drugoptions)   
                                elif option1 ==1 and option2 ==1:
                                    user_choice[3].append('Metastatic, Prior Treatment','Recurrance Treatment')
                                    user_choice[4].append(drugoptions)   
                                print(user_choice)
                                def store_show_month():
                                    user_month = month_user.get()
                                    user_choice.append(user_month)
                                    print(user_choice)
                                    def close_window():
                                        time.sleep(3)
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
                            btn1 = tk.Checkbutton(gui_1, text=toptions[0], variable=treatment_user_1, width = 20,font=('Imago',13),anchor ='w')
                            btn1.place(x=500,y=215)
                            btn2 = tk.Checkbutton(gui_1, text=toptions[1], variable=treatment_user_2, width = 20,font=('Imago',13),anchor ='w')
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
                                
                                    if option1 ==1:
                                        user_choice[3].append('Metastatic, Prior Treatment')
                                        user_choice[4].append(drugoptions)
                                    elif option2 ==1:
                                        user_choice[3].append('Recurrance Treatment')
                                        user_choice[4].append(drugoptions)   
                                    elif option1 ==1 and option2 ==1:
                                        user_choice[3].append('Metastatic, Prior Treatment','Recurrance Treatment')
                                        user_choice[4].append(drugoptions)   
                                    print(user_choice)
                                    def store_show_month():
                                        user_month = month_user.get()
                                        user_choice.append(user_month)
                                        print(user_choice)
                                        def close_window():
                                            time.sleep(3)
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
                                btn1 = tk.Checkbutton(gui_1, text=toptions[0], variable=treatment_user_1, width = 20,font=('Imago',13),anchor ='w')
                                btn1.place(x=500,y=220)
                                btn2 = tk.Checkbutton(gui_1, text=toptions[1], variable=treatment_user_2, width = 20,font=('Imago',13),anchor ='w')
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
                                
                                    if option1 ==1:
                                        user_choice[3].append('Metastatic, Prior Treatment')
                                        user_choice[4].append(drugoptions)
                                    elif option2 ==1:
                                        user_choice[3].append('Recurrance Treatment')
                                        user_choice[4].append(drugoptions)   
                                    elif option1 ==1 and option2 ==1:
                                        user_choice[3].append('Metastatic, Prior Treatment','Recurrance Treatment')
                                        user_choice[4].append(drugoptions)   
                                    print(user_choice)
                                    def store_show_month():
                                        user_month = month_user.get()
                                        user_choice.append(user_month)
                                        print(user_choice)
                                        def close_window():
                                            time.sleep(3)
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
                                btn1 = tk.Checkbutton(gui_1, text=toptions[0], variable=treatment_user_1, width = 20,font=('Imago',13),anchor ='w')
                                btn1.place(x=500,y=220)
                                btn2 = tk.Checkbutton(gui_1, text=toptions[1], variable=treatment_user_2, width = 20,font=('Imago',13),anchor ='w')
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
                                
                                    if option1 ==1:
                                        user_choice[3].append('Metastatic, Prior Treatment')
                                        user_choice[4].append(drugoptions)
                                    elif option2 ==1:
                                        user_choice[3].append('Recurrance Treatment')
                                        user_choice[4].append(drugoptions)   
                                    elif option1 ==1 and option2 ==1:
                                        user_choice[3].append('Metastatic, Prior Treatment','Recurrance Treatment')
                                        user_choice[4].append(drugoptions)   
                                    print(user_choice)
                                    def store_show_month():
                                        user_month = month_user.get()
                                        user_choice.append(user_month)
                                        print(user_choice)
                                        def close_window():
                                            time.sleep(3)
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
                                btn1 = tk.Checkbutton(gui_1, text=toptions[0], variable=treatment_user_1, width = 40,font=('Imago',13),anchor ='w')
                                btn1.place(x=500,y=280)
                                btn2 = tk.Checkbutton(gui_1, text=toptions[1], variable=treatment_user_2, width = 20,font=('Imago',13),anchor ='w')
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
                                
                                    if option1 ==1:
                                        user_choice[3].append('Metastatic, Prior Treatment')
                                        user_choice[4].append(drugoptions)
                                    elif option2 ==1:
                                        user_choice[3].append('Recurrance Treatment')
                                        user_choice[4].append(drugoptions)   
                                    elif option1 ==1 and option2 ==1:
                                        user_choice[3].append('Metastatic, Prior Treatment','Recurrance Treatment')
                                        user_choice[4].append(drugoptions)   
                                    print(user_choice)
                                    def store_show_month():
                                        user_month = month_user.get()
                                        user_choice.append(user_month)
                                        print(user_choice)
                                        def close_window():
                                            time.sleep(3)
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
                                btn1 = tk.Checkbutton(gui_1, text=toptions[0], variable=treatment_user_1, width = 20,font=('Imago',13),anchor ='w')
                                btn1.place(x=500,y=280)
                                btn2 = tk.Checkbutton(gui_1, text=toptions[1], variable=treatment_user_2, width = 20,font=('Imago',13),anchor ='w')
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
                                    if option1 ==1:
                                        user_choice[3].append('Metastatic, Prior Treatment')
                                        user_choice[4].append(drugoptions)
                                    elif option2 ==1:
                                        user_choice[3].append('Recurrance Treatment')
                                        user_choice[4].append(drugoptions)   
                                    elif option1 ==1 and option2 ==1:
                                        user_choice[3].append('Metastatic, Prior Treatment','Recurrance Treatment')
                                        user_choice[4].append(drugoptions)   
                                    print(user_choice)
                                    def store_show_month():
                                        user_month = month_user.get()
                                        user_choice.append(user_month)
                                        print(user_choice)
                                        def close_window():
                                            time.sleep(3)
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
                                btn1 = tk.Checkbutton(gui_1, text=toptions[0], variable=treatment_user_1, width = 20,font=('Imago',13),anchor ='w')
                                btn1.place(x=500,y=230)
                                btn2 = tk.Checkbutton(gui_1, text=toptions[1], variable=treatment_user_2, width = 20,font=('Imago',13),anchor ='w')
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
                                    if option1 ==1:
                                        user_choice[3].append('Metastatic, Prior Treatment')
                                        user_choice[4].append(drugoptions)
                                    elif option2 ==1:
                                        user_choice[3].append('Recurrance Treatment')
                                        user_choice[4].append(drugoptions)   
                                    elif option1 ==1 and option2 ==1:
                                        user_choice[3].append('Metastatic, Prior Treatment','Recurrance Treatment')
                                        user_choice[4].append(drugoptions)   
                                    print(user_choice)
                                    def store_show_month():
                                        user_month = month_user.get()
                                        user_choice.append(user_month)
                                        print(user_choice)
                                        def close_window():
                                            time.sleep(3)
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
                                btn1 = tk.Checkbutton(gui_1, text=toptions[0], variable=treatment_user_1, width = 20,font=('Imago',13),anchor ='w')
                                btn1.place(x=500,y=230)
                                btn2 = tk.Checkbutton(gui_1, text=toptions[1], variable=treatment_user_2, width = 20,font=('Imago',13),anchor ='w')
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
                                
                                    if option1 ==1:
                                        user_choice[3].append('Metastatic, Prior Treatment')
                                        user_choice[4].append(drugoptions)
                                    elif option2 ==1:
                                        user_choice[3].append('Recurrance Treatment')
                                        user_choice[4].append(drugoptions)   
                                    elif option1 ==1 and option2 ==1:
                                        user_choice[3].append('Metastatic, Prior Treatment','Recurrance Treatment')
                                        user_choice[4].append(drugoptions)   
                                    print(user_choice)
                                    def store_show_month():
                                        user_month = month_user.get()
                                        user_choice.append(user_month)
                                        print(user_choice)
                                        def close_window():
                                            time.sleep(3)
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
                                btn1 = tk.Checkbutton(gui_1, text=toptions[0], variable=treatment_user_1, width = 20,font=('Imago',13),anchor ='w')
                                btn1.place(x=500,y=230)
                                btn2 = tk.Checkbutton(gui_1, text=toptions[1], variable=treatment_user_2, width = 20,font=('Imago',13),anchor ='w')
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
                                
                                    if option1 ==1:
                                        user_choice[3].append('Metastatic, Prior Treatment')
                                        user_choice[4].append(drugoptions)
                                    elif option2 ==1:
                                        user_choice[3].append('Recurrance Treatment')
                                        user_choice[4].append(drugoptions)   
                                    elif option1 ==1 and option2 ==1:
                                        user_choice[3].append('Metastatic, Prior Treatment','Recurrance Treatment')
                                        user_choice[4].append(drugoptions)   
                                    print(user_choice)
                                    def store_show_month():
                                        user_month = month_user.get()
                                        user_choice.append(user_month)
                                        print(user_choice)
                                        def close_window():
                                            time.sleep(3)
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
                                btn1 = tk.Checkbutton(gui_1, text=toptions[0], variable=treatment_user_1, width = 20,font=('Imago',13),anchor ='w')
                                btn1.place(x=500,y=210)
                                btn2 = tk.Checkbutton(gui_1, text=toptions[1], variable=treatment_user_2, width = 20,font=('Imago',13),anchor ='w')
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
                                
                                    if option1 ==1:
                                        user_choice[3].append('Metastatic, Prior Treatment')
                                        user_choice[4].append(drugoptions)
                                    elif option2 ==1:
                                        user_choice[3].append('Recurrance Treatment')
                                        user_choice[4].append(drugoptions)   
                                    elif option1 ==1 and option2 ==1:
                                        user_choice[3].append('Metastatic, Prior Treatment','Recurrance Treatment')
                                        user_choice[4].append(drugoptions)   
                                    print(user_choice)
                                    def store_show_month():
                                        user_month = month_user.get()
                                        user_choice.append(user_month)
                                        print(user_choice)
                                        def close_window():
                                            time.sleep(3)
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
                                btn1 = tk.Checkbutton(gui_1, text=toptions[0], variable=treatment_user_1, width = 20,font=('Imago',13),anchor ='w')
                                btn1.place(x=500,y=260)
                                btn2 = tk.Checkbutton(gui_1, text=toptions[1], variable=treatment_user_2, width = 20,font=('Imago',13),anchor ='w')
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
                                
                                    if option1 ==1:
                                        user_choice[3].append('Metastatic, Prior Treatment')
                                        user_choice[4].append(drugoptions)
                                    elif option2 ==1:
                                        user_choice[3].append('Recurrance Treatment')
                                        user_choice[4].append(drugoptions)   
                                    elif option1 ==1 and option2 ==1:
                                        user_choice[3].append('Metastatic, Prior Treatment','Recurrance Treatment')
                                        user_choice[4].append(drugoptions)   
                                    print(user_choice)
                                    def store_show_month():
                                        user_month = month_user.get()
                                        user_choice.append(user_month)
                                        print(user_choice)
                                        def close_window():
                                            time.sleep(3)
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
                                btn1 = tk.Checkbutton(gui_1, text=toptions[0], variable=treatment_user_1, width = 20,font=('Imago',13),anchor ='w')
                                btn1.place(x=500,y=260)
                                btn2 = tk.Checkbutton(gui_1, text=toptions[1], variable=treatment_user_2, width = 20,font=('Imago',13),anchor ='w')
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
                                
                                    if option1 ==1:
                                        user_choice[3].append('Metastatic, Prior Treatment')
                                        user_choice[4].append(drugoptions)
                                    elif option2 ==1:
                                        user_choice[3].append('Recurrance Treatment')
                                        user_choice[4].append(drugoptions)   
                                    elif option1 ==1 and option2 ==1:
                                        user_choice[3].append('Metastatic, Prior Treatment','Recurrance Treatment')
                                        user_choice[4].append(drugoptions)   
                                    print(user_choice)
                                    def store_show_month():
                                        user_month = month_user.get()
                                        user_choice.append(user_month)
                                        print(user_choice)
                                        def close_window():
                                            time.sleep(3)
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
                                btn1 = tk.Checkbutton(gui_1, text=toptions[0], variable=treatment_user_1, width = 20,font=('Imago',13),anchor ='w')
                                btn1.place(x=500,y=305)
                                btn2 = tk.Checkbutton(gui_1, text=toptions[1], variable=treatment_user_2, width = 20,font=('Imago',13),anchor ='w')
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
                                
                                    if option1 ==1:
                                        user_choice[3].append('Metastatic, Prior Treatment')
                                        user_choice[4].append(drugoptions)
                                    elif option2 ==1:
                                        user_choice[3].append('Recurrance Treatment')
                                        user_choice[4].append(drugoptions)   
                                    elif option1 ==1 and option2 ==1:
                                        user_choice[3].append('Metastatic, Prior Treatment','Recurrance Treatment')
                                        user_choice[4].append(drugoptions)   
                                    print(user_choice)
                                    def store_show_month():
                                        user_month = month_user.get()
                                        user_choice.append(user_month)
                                        print(user_choice)
                                        def close_window():
                                            time.sleep(3)
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
                                btn1 = tk.Checkbutton(gui_1, text=toptions[0], variable=treatment_user_1, width = 20,font=('Imago',13),anchor ='w')
                                btn1.place(x=500,y=235)
                                btn2 = tk.Checkbutton(gui_1, text=toptions[1], variable=treatment_user_2, width = 20,font=('Imago',13),anchor ='w')
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


#sorting and comparing the data
#==========================================================================================================================
#Sorting out drugs symptoms and putting them into an array

import csv
import operator 

user_choice = [0, 'Female', 'Breast', ['Breast, Metastatic'], ['Avastin', 'Herceptin', 'Xeloda'], 1]
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

#Trying to get rid of 1st and 2nd element in each array
index = [0,1,5]
new_user_choice = [i for i in user_choice if user_choice.index(i) not in index]

#COmparing user choice with cancer and drugs symptoms and sorting by the area of cancer
new_cancer_list=[]
new_drugs_list = []
final_array = []
for i in range(len(drugs_list)) :
    if new_user_choice[0]==drugs_list[i][0]:
        new_drugs_list.append(drugs_list[i])
    elif new_user_choice[1][0]==drugs_list[i][1]:
        new_drugs_list.append(drugs_list[i])
    
print(drugs_list)

'''
new_drugs_list = []
for n in range(len(drugs_list)) :
    if new_user_choice[0]==drugs_list[n][0] :
        new_drugs_list.append(drugs_list[n])'''


#sort by year











