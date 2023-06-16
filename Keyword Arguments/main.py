# Keyword Arguments =   arguments preceded by an identifier when we pass them to a function
#                       The order of the arguments doesn't matter, unlike positional arguments.
#                       Python knows the name of the arguments that our function receives

#Example of the use of a positional argument

def hello(first,middle,last):
    print("Hello " +first+' '+middle+' '+last )

#We using positional arguments, so the order of the argument does matter.
#hello('Boitumelo','Charles','Rachoshi')

#To use keyword arguments, we make use of the = sign within the function

hello(last='Rachoshi',first='Boitumelo',middle='Charles')