# Walrus Operator :=

#new to python 3.8
#assignment expression aka walrus operator
#assigns values to variables as part of a larger expression


#happy=True
#print(happy)

#print(happy=True)   #we cannot do this usinng the standard assignment sign
                    #This is when we use the walrus operator

print(happy:=True)

foods=list()
while True:
    food=input("What food do you like?:  ").lower()
    if food=="quit":
        break
    foods.append(food) #adds input to the list

#Now let's write the program using a walrus operator

while food:= input("What food do you like?:  ")!='quit':
    foods.append(food)
