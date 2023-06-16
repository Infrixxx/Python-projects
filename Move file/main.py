# moving file

import os

source='File detection.txt'

#We need path of desktop
destination='C:\\Users\\BC RACHOSHI\\desktop\\File moved.txt'

#write in try and except block to handle any exception

try:
    if os.path.exists(destination):
        print("There is already a file there")
    else:
        #code to move file from source to destination, thus passing the two arguments
        #This should result in the file being moved to desktop and named file moved
        os.replace(source,destination)
        print(source+" was moved")

except FileNotFoundError:
    print(source+" was not found")


#You can also use this to move a directory
source='Folder to move'
destination='C:\\Users\\BC RACHOSHI\\desktop\\Folder moved'

try:
    if os.path.exists(destination):
        print("There is already a file there")
    else:

        os.replace(source,destination)
        print(source+" folder moved")

except FileNotFoundError:
    print(source+" was not found")