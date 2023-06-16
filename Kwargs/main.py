#  Kwargs   =   This is a parameter that will pack all arguments into a dictionary
#               Useful so that a functin can accept a varying amounnt of keyword arguments

#This is an example of a function that only takes two arguments
#def hello(first, last):
    #print('Hello '+first+'  '+last)

#hello(first= Boitumelo, last=Rachoshi,middle=Charles)

#Since the arguments above are three and the function can only take in two
# arguments, we will need to make one function that can take an unlimited
# number of arguments

#def hello(**kwargs):
    #print("Hello "+kwargs['first']+' '+kwargs['last'])
#Although it can take unlimited arguments, this function only prints first and last name
#hello(first= 'Boitumelo', last='Rachoshi',middle='Charles')

#To create a function that prints all the names that are passed through the dictionary

def hello(**kwargs):
    print("Hello", end=' ')
    for key,value in kwargs.items():
        #we need the Value not the names and since we want it horizontal we need to use end=''
        print(value,end=' ')

hello(first= 'Boitumelo', last='Rachoshi',middle='Charles')