# Args  =   Parameter that will pack all arguments into a tuple.
#           Useful so that a function can accept a varying amount of arguments

#This is a  function that takes in two numbers and adds them together, returning the result.
#This cannot work in a case where we need to add 3 or more numbers
def add(num1,num2)  :
    sum= num1+num2
    return sum

#This is why we make use of Args
#We use the asterisk to pack the arguments and passing theem into a tuple,
#def add(*pack) :
    #You not oblidged to name it pack, you can name it anything as long as
    # the asterisk is included
    #sum= 0
    #for i in pack:
        #This adds all values that where passed in the tuple together
        #sum +=i
    #return sum

#print(add(1,2,3,4,5,6))


#To add stuff to function after we have used our tupple
def add(*stuff) :
    sum= 0
    #we create a list from the tuple
    stuff=list(stuff)
    #We index the list and define the first index
    stuff[0]=0
    for i in stuff:
        sum+=i
    return sum

print(add(1,2,3,4,5,6))
