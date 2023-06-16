# Loop control statements = change a loop's execution from it's normal sequence

#break=         used to terminate the loop entirely
#continue=      skips to the next iteration of the loop
#pass=          does nothing, acts as a placeholder

#while True:
    #name=input('Enter your name')
    #If name is not empty, then the loop breaks and the code ends
    #if name !=  '':
       #break

#now for the continue statement

phone_number='123-456-7890'

for i in phone_number:
    #Continue is to skip the iteration of the condition that is put in place if true.
    #Here the code is to skip the condition in which the i iteration is equal to -
    if i== "-":
        continue
        #This will print the phone without the dash and also print it  horizontally.
    print(i, end='')

for i in range (1,21):

    if i==13:
        #when i==13, it won't do anything, it will  pass the iteration
        pass
    else:
        print(i)