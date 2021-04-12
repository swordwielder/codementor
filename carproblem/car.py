'''In this part of the assignment we will practice using a class that has been given to us.

You are provided with a file car.py (see attached file later). This file contains code that implements a very basic car object. 
It has a constructor, getter and setter methods. Take a look at the Car class and familiarize yourself with those methods.

Your task is to write the main routine that creates a Car object, 
prints the initial state of the object, speeds the car up until you reach a speed of 50 miles per hour, then slows it down until the speed is zero.

Here are some additional specifications:

The user of the program must provide the car's make and year model.
The year is an integer value and cannot be less than 1945 or greater than 2020.
You must use loops and try/except for the year validation.
You must properly use loops and conditional statements when needed.
You are not allowed to modify the car.py file or the Car class.
Make sure you include a header comment at the top of your file.
Below there’s a sample run:

Enter the car's make: Audi
Enter the car's year model: 1900
Invalid year. Try again. Enter the car's year model: abc
Invalid input: a numeric value was expected. Try again. Enter the car's year model: 2022
Invalid year. Try again. Enter the car's year model: 2020

My car's make: Audi
My car's year: 2020
My car's current speed: 0 mph.

Accelerating
My car's current speed: 5 mph.
My car's current speed: 10 mph.
My car's current speed: 15 mph.
My car's current speed: 20 mph.
My car's current speed: 25 mph.
My car's current speed: 30 mph.
My car's current speed: 35 mph.
My car's current speed: 40 mph.
My car's current speed: 45 mph.
My car's current speed: 50 mph.

Slowing down
My car's current speed: 45 mph.
My car's current speed: 40 mph.
My car's current speed: 35 mph.
My car's current speed: 30 mph.
My car's current speed: 25 mph.
My car's current speed: 20 mph.
My car's current speed: 15 mph.
My car's current speed: 10 mph.
My car's current speed: 5 mph.
My car's current speed: 0 mph.
Notes:

You may find the following site useful to compare your output against the expected program output: Diffchecker
The purpose of this problem is to practice using classes and modules.
Please make sure to submit a well-written program. Good identifier names, useful comments, and spacing will be some of the criteria that will be used when grading this assignment.
This assignment can be and must be solved using only the materials that have been discussed in class. Do not look for alternative methods that have not been covered as part of this course.
'''


'''
car.py file Below
'''


class Car:
    # constructor
    def __init__ (self, make, year):  
        self.__make = make
        self.__year = year
        self.__speed = 0
    
    # getters
    def getMake(self):
        return self.__make
    
    def getYear(self):
        return self.__year
    
    def getSpeed(self):
        return self.__speed
    
    # setters
    def accelerate(self):
        self.__speed = self.__speed + 5
    
    def brake(self):
        self.__speed = self.__speed - 5

