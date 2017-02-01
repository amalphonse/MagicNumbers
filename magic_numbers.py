# -*- coding: utf-8 -*-
"""
Created on Mon Jan 30 14:35:35 2017

@author: Anju Mercian
"""

#magic number program in python
import random


magic_numbers = [random.randint(0,9),random.randint(0,9)]

def ask_user_and_check_number():
    user_number =int(input("Enter a number between 0 and 9: "))
    if user_number in magic_numbers:
        return "You have got the number right!"
        
    if user_number not in magic_numbers:
        return "You din't get it quite right."


def run_program_x_times(chances):
    for i in range(chances):
        print("This is attempt {}".format(i+1))
        message =  ask_user_and_check_number()
        print(message)
        
        
user_input = int(input('Enter the number of attempts: '))        
run_program_x_times(user_input)