#slicing = create a substing by extracting elements from another string
#To slice a string we csn either use:
#           indexing[] or slice()
#           [start:stop:step]


name= "Boitumelo Rachoshi"

first_name  = name[6]
#print(first_name)

#To slice an entire portion of the string
first_name=name[0:8] #the first index is inclusive of the character, the last index is exlcusive
#print(first_name) #This wont type Boitumelo instead it will type Boitumel

#so to get Boitumelo
first_name=name[0:9]

#You can also write first_name[0:9] as:
first_name=name[:9]#python assumes the empty space is zero

#print(first_name)

#last name
last_name=name[10:18]

#You can also have last name equal to every character after the 10th index
last_name=name[10:]
#print(last_name)

#Step is how much we increasing our index by, from start to stop
#lets say we count every second name
#funky_name=name[0:9:2]

#print(funky_name)

#   if you leave start and stop empty, python will assume that the indexing is
#   from beginning to end, taking every second letter from 0

funky_name=name[::2]
print(funky_name)

#To reverse name, we use negative 1, so it will count backwards

reverse_name=name[::-1]
print(reverse_name)

#For the slice function, we can use it
#Slice works the same as the index function, just that we use round brackets and commas
#The characters are all indexed and for positive index there's a negative index, the last character index is -1
#websites all have different lenght so we will use negative index for the stop, unlike the start.
#we want our slice to start at 7 and end at -4, so we can get the website name
website="http://google.com"

website1="http://wikipedia.com"

slice=slice(7,-4)   #  you can also include step in the slice, say step of 2, this will take every second character starting
                    #  from the initial character used as the initial to the character before the end.



#  we use website[slice] instead of slice because that will return the slice as a variable
print(website[slice])
print(website1[slice])
