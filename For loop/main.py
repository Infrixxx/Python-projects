import time
# For loop = a statement that will execute a block of code
#            a limited amount of times

#   while loop= unlimited
#   for loop=limited

#i is for index
#when we say for i in range of 10 we counting for index from 0-9
#for i in range(10):
    #print(i)

#To print from 1 to 10 we can say
#for i in range(10):
        #print(i+1)

#range(start,stop,step) this will print from 50 to 100 in steps of 2
#for i in range(50,100+1,2):
    #print(i)

#To print every letter individually per step, each letter printed on a new line
#for i in "Boitumelo Rachoshi":
    #print(i)

#We going to create a countdown, so we need to import time module
for t in range(10,0,-1):
    print(t)
    time.sleep(1)
print ('Happy new year')
