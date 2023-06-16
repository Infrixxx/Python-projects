#User input, we use fuction input() to get input

#input('What is your name:   ')

#input can be stored in a variable

name=input('What is your name ? ')
age=input('How old are you ?')
height=float(input("how tall are you ?")) #since it is a decimal number, we will cast it to float

#age+=1    #This will give an error as you can't cocnatenate str with int
age=int(age)
age+=1

#This will print the string plus your input after accepting your input
print("Your name is "+name)

#print('You are '+ age+' old') #This line wont work because it is adding string to integer to fix we must convert to string
print('You are '+ str(age)+' years old')

#print the height, we will cast it to string

print("You are "+str(height)+"cm tall")

