# reduce() =    apply a function to an iterable and reduce it to a single cumulative value.
#               performs a function on first two elements and repeats process until 1 value remains
#
# reduce(function, iterable)

import functools

letters= ["H","E","L","L","O"]
word = functools.reduce(lambda x,y: x+y, letters)   #our reduce function applies our function
                                                    #to the first two elements within our iterable
                                                    #Then we repeat the process using the result from
                                                    #the first time we used the function.
print(word)

factorial= [5,4,3,2,1]

result = functools.reduce(lambda a,b: a*b,factorial)

print(result)

