# ---------------------------------

# File          : practice1.py
# Author        : Anup Jacob
# Version       : v1.0
# Created Date  : 18/10/2021
# Modified Date : 
# Description   : Sample Q1 for practice purpose
# Licensing     : Anup Jacob, LYIT
# ----------------------------------
import os


def practice_q():

    total_size = 0

    filepath = input("Enter the location of your directory : ")

    if not os.path.exists(filepath):
        print("The Directory/ Path you have specified does not exist!!. Please check your input.")
    else:
        for file_name in os.listdir(filepath):
            print(f"{file_name}")
            size = os.path.getsize(os.path.join(filepath, file_name))
            total_size = total_size + size

        print("The contents of this directory is: {}".format(total_size))

if __name__=='__main__':
    practice_q()