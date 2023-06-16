# list = used to store multiple items in a single variable

food= ["pizza", 'hamburger', 'hotdog','sphaghetti']

#This will print the list of food
#print(food)

#To access elements in the list, we will need to use the index
#This will print the element 2, which is hotdog
#print(food[2])

#To print the list in order we use a for loop
#This will print the list per item
#for l in food:
    #if l=='pizza':
       #pass
    #else:
        #print(l)

#To add things to list we make  use of the .append code

#food.append("Burrito")

#print("list without Burrito added:      "+str(food))

#To remove things from the list, say we want to remove hotdog we use list.remove('item to be removed')

#food.remove('hotdog')

#print("\n\nlist without hotdog:       "+str(food))

#pop is used to remove the last element in the list
food.pop()
print(food)

#sort will sort the elements alphabetically
food .sort()

for x in food:
    print(x)

#To clear the list we use clear, this wont print anything as list is cleared
food.clear()

print('')

