# map() =   applies a function to each item in an iterable (list,tuple,etc.)
#
#map(function, iterable)

#This is dollars
store = [("shirt",20.00),
         ("pants",25.00),
         ("jacket",50.00),
         ("socks",10.00)]

to_euros = lambda data: (data[0],data[1]*0.82)  #data[0] represents the first column,
                                                #data[1] represents the second column
                                                #The first column will remain the same
                                                #But the data in the second column will
                                                #be multiplied by 0.82

#to_dollars= lambda data: (data[0],data[1]/0.82)

store_euros =list(map(to_euros,store))# we passed our map object with our function and iterable
                                      # And then we pass it into a list.

for i in store_euros:
    print(i)



