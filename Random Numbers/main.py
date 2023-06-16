import random

#to generate a random number from 1 to 6
x= random.randint(1,6)
#We can also generate a random floating number
y=random.random()

#We can also generate a random choice
mylist=['rock','paper','scissors']
z=random.choice(mylist)

#we can also shufffle a list
cards = [1,2,3,4,5,6,7,8,9,"J","Q","k","A"]
random.shuffle(cards)

print(x)
print(y)
print(z)
print(cards)
