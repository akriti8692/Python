# -*- coding: utf-8 -*-
"""
Created on Fri Sep  4 20:43:10 2020

@author: 16509
"""
dict1={}
list1=[]
list2=[]

assignment=['Homework','Midterm','FinalExam']
def enter_grade(assignment,amount,max_grade):
    for i in assignment:
        if i=='Homework':
            while z in range(1,4):
                a=input("Enter your Homework marks {}".format(z))
                list1.append(a)
        if i=='Midterm': 
            while z in range(1,3):
                a=input("Enter your Midterm marks {}".format(z))
                list2.append(a)
        if i=='FinalExam': 
                val1=input("Enter your final Grade")

    
def setup_grade(dict1):
    enter_grade()
    
def display_grade():
    
#this need not be called from main
def average_grade(list1,list2):
    averagehw=(list1[0]+list1[1]+list1[2])/3
    averagemt=(list2[0]+list2[1])/2
        return averagehw
        return averagemt
    
        
def course_grade(list1,list2,val1):
    hwa=average_grade()
    mida=average_grade()
    CourseGrade= .25*hwa+.50*mida+.25*val1
    

#For Printing Course GRade    
def letter_grade(CourseGrade):
    if CourseGrade>=90 and CourseGrade<=100:
        print("A")
    elif CourseGrade>=80 and CourseGrade<=89:
        print("B")
    elif CourseGrade>=70 and CourseGrade<=79:
        print("C")
    elif CourseGrade>=60 and CourseGrade <=69:
        print("D")
    elif CourseGrade>=0 and CourseGrade<=59:
        print("F")

def main()
        
