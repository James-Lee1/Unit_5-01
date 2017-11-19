# Created by : James Lee
# Created on : Nov 2017
# Created for : ICS3UR
# This program generates 10 random numbers and calculates the average

import ui
import random

my_numbers = []
    
def find_average_touch_up_inside(sender):   
    # This calculates the average of the ten numbers and runs once the button is clicked

    calculate_average(my_numbers)

    print_average = str(calculate_average(my_numbers))
    view['average_label'].text = "The average is: " + print_average

def calculate_average(my_numbers): 
    # Function that finds the average of the numbers
    total = 0

    for number, value in enumerate(my_numbers, 0):      
        total = total + value
        number = number + 1
                  
    average = float(total / 10)     
    return average    
	
view = ui.load_view()
view.present('full_screen') 

def create_10_random_numbers():
    # Creates ten random numbers

    for random_number in range(10):
        random_number = random.randint(1,100)
        my_numbers.append(random_number)    
        view['average_textview'].text = str(my_numbers)

create_10_random_numbers()
