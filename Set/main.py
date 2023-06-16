# Set= COllection which is unorderd, unindexd. No duplicate values

utensils={"fork",'spoon','knife'}
dishes={'bowl',"plate","cup"}


#We can add elements to set
#utensils.add('Napkin')



#e can remove items from a set
#utensils.remove('knife')



#We can also clear a set
#utensils.clear()



#We can also add sets together, this will add all elements
# found in our utensils set to our dishes set
#dishes.update(utensils)



#We can also form a new set from two sets
dinner_table=utensils.union(dishes)



#This will print the elements in the set in any order, this is essential
#It is faster than a list and used to check if element is in a set
#NO DUPLICATE VALUES
#for x in utensils:
   # print(x)


#This will print all the elements in the dishes set
#for x in dishes:
    #print(x)

#This will print all the elements in the dinner_table
for x in dinner_table:
    print(x)


#To compare utensils against dishes, this will print
# what utensils has that dishes doesn't

print(utensils.difference(dishes))

#To compare dishes against utensils, this will print
# what dishes has that utensils doesn't
print(dishes.difference(utensils))

#We can also print where the elements intersect between the two sets
print(dishes.intersection(utensils))
