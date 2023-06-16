# filter()  =   creates a collection of elements from an
#               iterable for which a function returns True

#filter(function, iterable)

friends= [("Rachel",19),
          ("Monica",18),
          ("Phoebe",17),
          ("Joey",16),
          ("Chandler",21),
          ("Ross",20)]

age = lambda  data: data[1] >=18

drinking_buddies=list(filter(age, friends))  #This is to cast the friends list to a list after filtering it'

for i in drinking_buddies:
    print(i)