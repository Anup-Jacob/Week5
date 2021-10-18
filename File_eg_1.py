# ---------------------------------

# File          : File_eg_1.py
# Author        : Anup Jacob
# Version       : v1.0
# Created Date  : 18/10/2021
# Modified Date : 
# Description   : File handling example 1
# Licensing     : Anup Jacob, LYIT
# ----------------------------------

def file_processing(file_name):
 """
 Open a file with a list of students and print their details.
 Parameters:
 file_name name of file with students name, lnumber and course details
 Returns:
 none
 """
 lines = open(file_name).readlines()
    # lines.sort() #this method can be used to sort a file
 for line in lines:
    student, l_num, course = line.split(",")
    print("Student Name:{0} \nLNumber: \t{1} \nCourse\t\t{2}\n".format(student, l_num, course))
    # Practice: Could you format the string in another way?

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
 file_processing("sample.txt")
