# ---------------------------------

# File          : File_eg_4.py
# Author        : Anup Jacob
# Version       : v1.0
# Created Date  : 18/10/2021
# Modified Date : 
# Description   : File handling example for zip files
# Licensing     : Anup Jacob, LYIT
# ----------------------------------

import zipfile, os


def zip_file_processing():
    """
    Zip File Demo

    :return:
    """
    # before running this example create a folder called c://zipDemo
    # add two files, one called sample2.txt the other called rubbish.txt
    os.chdir(os.path.normpath("C://zipDemo"))
    newZip = zipfile.ZipFile('myNew.zip', 'a')  # create a zip file. can be r,w,a read / write / append
    newZip.write('sample2.txt')  # add a file to the same zip file
    print("{}".format(newZip.printdir()))  # show contents of the file
    print("")
    newZip.write("RubbishFile.txt")  # add a second file
    print("{}".format(newZip.printdir()))  # show contents of the file
    # assuming that the zipDemo folder has been created...
    print("\nFiles in the zip are: {}\n".format("c://zipDemo//extracthere"))
    newZip.extractall("c://zipDemo//extracthere")
    newZip.close()

if __name__ == '__main__':
    zip_file_processing()

