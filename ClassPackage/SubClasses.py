# ---------------------------------

# File          : SubClasses.py
# Author        : Anup Jacob
# Version       : v1.0
# Created Date  : 22/10/2021
# Modified Date : 
# Description   : Sample program created to check the functionality of class and inheritance
# Licensing     : Anup Jacob, LYIT
# ----------------------------------


class Person:

    def attendCollege(self):
        print("I am attending college")

    def sitExams(self):
        print("I am writing Exams")

    def lecture(self):
        print("I am inside Lecturer function")

    def marCA(self):
        print("I am inside markCA")


class Students(Person):

    Person.attendCollege(self=1)
    Person.sitExams(self=1)


class Lecturer(Person):

    Person.marCA(self=1)
    Person.lecture(self=1)

