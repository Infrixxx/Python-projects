# Higher order function = a function that either
#                         1. accepts a function as an argument
#                                   or
#                         2. returns a function
#                         (In python, functions are also treated as objects)


#Example of higher order function that accepts a function as an argument
def loud(text):
    return text.upper()

def quiet(text):
    return text.lower()

def hello(func): #we naming the argument func- short for function
    text= func('Hello')
    print(text)

hello(loud) #we calling the hello function and
            #we passing in loud as the argument
            #text=loud('Hello')
            #we sending the string that says 'Hello to the loud function'
            #and returning it in upper case
            #then we printing it as text


#Example of a higher order function that returns a function
def divisor(x):
    def dividend(y):
        return y/x
    return dividend
#To access th dividend function, I first need to call the divisor function
#and pass in a number to serve as a divisor.

divide=divisor(2)   #we passing in 2 as x
                    #we skipping the dividend function
                    #as we haven't called it.
                    #returning the dividend
print(divide(10))   #so now we calling in dividend and passing in 10
                    #so y is 10 and x is still 2, so 10/2 =5