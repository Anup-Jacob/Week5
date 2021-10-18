# ---------------------------------

# File          : practice2.py
# Author        : Anup Jacob
# Version       : v1.0
# Created Date  : 18/10/2021
# Modified Date :
# Description   : Sample Q2 for practice purpose
# Licensing     : Anup Jacob, LYIT
# ----------------------------------
import os


def practice_q():

    total_size = 0
    sub_size = 0

    filepath = input("Enter the location of your directory : ")

    if not os.path.exists(filepath):
        print("The Directory/ Path you have specified does not exist!!. Please check your input.")
    else:

        for file_list in os.walk(filepath):
            #print("\nIn directory {}".format(root))
            print(file_list)
            for file_name in file_list:
                if file_name != filepath and file_name :
                    print("\nFilepath is :" + format(filepath))
                    print("Filename is :"+format(file_name))
                    path = filepath+"/"+''.join(map(str,file_name))
                    print("The path is "+path)
                    subsize = os.path.getsize("C://zipdemo/extracthere")
                    print("The size of the subfolder = "+format(subsize))

                #sub_size = sub_size + size
                #print("Subfolder size is "+format(size))
                #total_size = total_size + size


            #print("The contents of this directory is: {}".format(total_size))

if __name__=='__main__':
    practice_q()