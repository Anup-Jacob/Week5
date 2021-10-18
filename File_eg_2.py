# ---------------------------------

# File          : File_eg_2
# Author        : Anup Jacob
# Version       : v1.0
# Created Date  : 18/10/2021
# Modified Date : 
# Description   : File Handling example 2
# Licensing     : Anup Jacob, LYIT
# ----------------------------------

def file_processing2(file_name):
    #open a file with the list of students and print their details...

    file_obj = open(file_name,"r+")
    #Lines.sort()  # this method can be used to sort a file

    for line in file_obj:
        print(line.rstrip())  #remove or strip whitespace at the end of the line while printing

    file_obj.write("\nThe Stopper, L0012356, Electrical Engineering")
    file_obj.seek(0)

    print("\nAfter the student has been added: ")
    all_file_contents = file_obj.read() #another way to read a file
    print(all_file_contents)  #prints now the contents that new line is added
    file_obj.close()

if __name__ == '__main__':
    file_processing2("sample.txt")

