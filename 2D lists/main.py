# 2D lists = list of lists

drinks= ['coffee',"soda","tea"]
dinner=['pizza',"hamburger", "hotdog"]
dessert=["Cake","ice cream"]

food=[drinks,dinner,dessert]

#This is a more complex line I created to practice
#print(str(food[0][2]).capitalize()+' and '+str(food[2][0])+ ' go well together.')

#A list in a list has indexes, the list becomes the index and the elements also index
#For example, in the list above, drinks is[0] and its contents soda[1]
#so to print soda. we say print(food[0][1])

print(food[0][1]) 