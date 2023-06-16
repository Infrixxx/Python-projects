# While loop is a block of code that will continue running as long as the codition is true

#while 1==1:
    #print('Infinte print brotha')

#Empty variable, name length is zero
name=''

#We create a conditional while loop where as long as the name is less than zero then the program
# will keep asking you to enter your name and the loop exits the moment the length of the name
# is no longer zero.

#hile len(name)==0:
    #name=input('Enter name : ')

#After the loop is ended when the user enters the name then the code will print Hello "name"
#print('Hello '+name)


name=None #None is the same as null or empty value, same as the above condition

while not name :
    name =input('Type in your name')

print('Welcome back ' + name)
