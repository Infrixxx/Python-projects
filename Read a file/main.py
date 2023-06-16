# Reading a file

#since our file is not in our project folder
#We need the file path
with open("C:\\Users\\BC RACHOSHI\\Desktop\\File detection.txt") as file:
    print(file.read())

#To check if file is closed or not we use:
print(file.closed)  #Should print true, as file closes after being opened

#In the case a file is not found:

try:
    with open("doesn't exist.txt") as file:
        print(file.read())

except Exception as a:
    print(a)
    print("That file doesn't exist :(")