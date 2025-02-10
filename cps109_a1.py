#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Nov 14 09:01:50 2024

@author: salma
"""

#Determining an effective approach to weight management can be challenging due to the complexity of 
#factors like age, gender, activity level, and more. Many resources online can overwhelm users with
#excessive information or unclear guidance. This program simplifies the process by providing a 
#user-friendly interface that collects essential inputs such as weight, height, age, gender, activity 
#level, and validates these inputs. It calculates calorie requirements, tailored to each person using
#scientifically established formulas like BMI and BMR, and according to the user's goals (weight loss, 
#gain, or maintenance). This program also generates a weekly progress tracker, allowing user's to monitor
#and document their weight changes in a table, allowing them to stay motivated throughout this journey.
#This program eliminates unnecessary complexity and focuses on actionable, clear, and precise guidance 
#for effective weight management.

def valid_input(prompt,condition,error):
    try:
        if 'weight' in prompt or 'height' in prompt:
            x=float(input(prompt))
            #if the prompt asks for the user's weight or height, then the input has to be a number (whole, or real), if not it returns a message stating that it is invalid
        elif 'gender' in prompt:
            x=input(prompt).lower()
            #if the prompt asks for the user's gender, then the input has to be a string
        else:
            x=int(input(prompt))
            #if the prompt asks for something that isnt weight, height or gender, the input has to be an integer
        if condition(x):
            return x
            #if the input meets the condition, then the input is returned
        else:
            print(error)
            return valid_input(prompt, condition, error)
            #if the input does not meet the condition then the function is run again, until it does meet the condition
        #ensures that all the inputs are reasonable/appropriate
    except:
        print('Invalid input. Please try again.')
        return valid_input(prompt, condition, error)
    #ensures that all the inputs are valid

start_weight=valid_input('Enter your starting weight in kilograms : ',lambda x:0<x<600,'Error, please enter an appropriate weight.')
goal_weight=valid_input('Enter your goal weight in kilograms : ',lambda x:0<x<600,'Error, please enter an appropriate weight.')
#ensures that the weight the user inputs is a positive number but less than 600kg (heaviest person alive)
height=valid_input('Enter your height in centimetres : ',lambda x:0<x<300,'Error, please enter an appropriate height.')
#ensures that the height the user inputs is positive and is less than 300 (tallest person alive)
gender=valid_input('Enter your gender (m/f) : ',lambda x:x=='m' or x=='f', "Error, please enter either 'm' or 'f'.")
#ensures the the user inputs either m for male or f for female for the gender
age=valid_input('Enter your age : ',lambda x:0<x<200,'Error, please enter an appropriate age.')
#ensures that the height the user inputs is positive and is less than 200 (oldest person  alive)
#allows the user to enter all their information
    
print('\nActivity Levels\n \n1: Sedentary: little or no exercise \n2: Exercise 1-3 times/week \n3: Exercise 4-5 times/week \n4: Daily exercise or intense exercise 3-4 times/week \n5: Intense exercise 6-7 times/week \n6: Very intense exercise daily, or physical job \n\nExercise: 15-30 minutes of elevated heart rate activity.\nIntense exercise: 45-120 minutes of elevated heart rate activity.\nVery intense exercise: 2+ hours of elevated heart rate activity.\n ')
#shows the user the different activity levels then asks which category they think they fit in
activity_level=valid_input('Enter your activity level (1-6) : ',lambda x:0<x<7,'Error, please enter a number between 1 and 6.')
#ensures that the user inputs an activity level between 1 and 6

def bmi_calculator(weight,height):
    height_m=height/100
    #converts the user's height from centimetres to metres
    height_m=height_m**2
    #squares the height
    bmi=weight/height_m
    #divides the weight by the height in metres squared
    bmi=round(bmi,1)
    #rounds the BMI to one decimal place
    if bmi<18.5: 
        category='(underweight)'
        #categorises any BMI less than 18.5 as underweight
    elif bmi<25.0:
        category='(healthy)'
        #categorises any BMI between 18.5 and 24.9 as normal weight
    elif bmi<30.0:
        category='(overweight)'
        #categorises any BMI between 25 and 29.9 as overweight
    else:
        category='(obese)'
        #categorises any BMI thats 30 and above as obese
    return (bmi,category)
#uses the BMI formula to calculate the user's BMI and categorize them into classes

result1=bmi_calculator(start_weight,height)
result2=bmi_calculator(goal_weight,height)
#allows the BMI to be printed as a tring without brackets and quotation marks

print('\nYour current BMI is : ' + str(result1[0]) + ' ' + result1[1])
print('Your BMI when you acheive your goal will be : ', str(result2[0]) + ' ' + result2[1])
print('Healthy BMI is between 18.5 and 24.9.')
#lets the user know what healthy BMI is, but since BMI does not consider muscle mass it is not accurate
print('\n*BMI (Body Mass Index) does not factor your body fat versus muscle content, so it is not accurate*\n')
#coutput the users current BMI and their BMI after they acheive their goal, gives a sidclaimer that BMI does not factor in everything so it is not accurate

if gender=='f':
    bmr=(10*start_weight)+(6.25*height)-(5*age)-161
else:
    bmr=(10*start_weight)+(6.25*height)-(5*age)+5
#calculates the user's BMR using the Mifflin-St Jeor equation, factoring in gender, height, age and activity level

bmr=round(bmr)
#rounds the BMR to the nearest whole number

print('Your BMR (Basal Metabolic Rate) is : ',bmr)
#shows the user their BMR

if goal_weight>start_weight:
    i=1
    j='gain'
    k='gained'
elif start_weight>goal_weight:
    i=-1 
    j='lose'
    k='lost'
else:
    i=0
    j='maintain'
#works out if the user wants to lose weight, gain weight or maintain their current weight

def daily_calories(bmr,activity_level):
    multipliers=[1.2,1.375,1.465,1.55,1.725,1.9]
    return round(bmr*multipliers[activity_level-1])
#multipliers are based on activity levels, then is multiplied by the BMR to show the amount of calories they would need to maintain their current weight

cal=daily_calories(bmr,activity_level)+(i*500)
#uses the i valute to add 500 calories if they want to gain weight, subract 500 calories if they want to lose weight, and just keeps the calories the same if they want to maintain their weight

if i!=0:
    print('To ',j,' 1lb (0.45kg) per week, you would need to consume', cal,'per day.')
#shows the user how many calories they would need to consume per day to lose 1lb a week
else:
    print('To maintain your weight you would need to consume', cal,'per day')
#shows the user how many calories they would need to consume to maintain their current weight

if i!=0:
    print('You would need approximately',abs((goal_weight-start_weight)*2) ,'weeks to reach your goal weight.')
weeks=valid_input('\nEnter how many weeks you would like to diet for : ',lambda x:0<x<=52,'Error, please enter an appropriate number of weeks (up to a year).')
#allows the user to input 

print('\nHere is a tracker to track your progress for the next', weeks, 'weeks :\n')
#creates a printable, user-freindly table for the user to be able to use to track their current weight and how many kgs they have left to reach their goal weight

with open('tracker.txt','w') as file:
    file.write(f'Your starting weight : {start_weight}\nYour goal weight : {goal_weight}\nYour height : {height}\nYour gender : {gender}\nYour age : {age}\nYour activity level : {activity_level}\n')
    file.write('-----------------------------------------------------\n')
    #creates the top line of the table
    for n in range(weeks):
            file.write(f'| week : {n + 1} | current weight :    | goal weight : {int(goal_weight)} |\n')
            #the first column has the week number, the second and third columns represent the user's current weight and their goal weight and gives the user space to document their progress as well as adding lines in between the columns for aesthetic purposes and to make it as user-friendly as possible
    file.write('------------------------------------------------------')
    #creates the bottom line of the table
with open('tracker.txt','r') as file:
    content=file.read()
    print(content)
