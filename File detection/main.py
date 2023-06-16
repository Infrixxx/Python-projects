# File detection = checking if a file exists on the computer
#we need to import the os module

import os

# first we need to create a file to detect
#create text file on desktop

#create a variable called path that will
# detect the path of the file

#we need double back-slashes,
# which is escape sequence for a backslash within a string
path="C:\\Users\\BC RACHOSHI\\Desktop\\File detection.txt"

#if os.path.exists(path):
    #print("That location exists")

#else:
    #print("That location doesn't exist!")

#check if location exists
#if that is file
#if os.path.exists(path):
    #print("That location exists")
    #if os.path.isfile(path):
        #print("That is a file")

#else:
    #print("That location doesn't exist!")

#Say it was a folder but not a file
#we can make use of elif statement

path="C:\\Users\\BC RACHOSHI\\Desktop\\Is a directory"

if os.path.exists(path):
    print("That location exists")
    if os.path.isfile(path):
        print("That is a file")
    elif os.path.isdir(path):
        print("That is a directory")
else:
    print("That location doesn't exist!")