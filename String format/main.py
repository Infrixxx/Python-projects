# str.format    =    optional method that gives users
#                    more control when displaying output


#animal='cow'
#item='Moon'

#print('The '+animal+' jumped over the '+item)

#The {} work as a place holder for a value or variable
#We can format the string using the .format command
#can use animal,item or 'cow','moon'
#print('The {} jumped over the {}'.format(item,animal))


#We can index, using positional argument
#print('The {1} jumped over the {0}'.format(item,animal)) #Positional argument


#print('The {animal} jumped over the {item}'.format(item='moon',animal='cow'))#Keyword argument

#A more elegant way of doing this
#text= "The {} jumped over the {}"
#print(text.format('cow','moon'))

#name= 'Boitumelo'

#print('Hello my name is {}'.format(name))
#To add some padding
#print('Hello my name is {:10} .Nice to meet you'.format(name))
#print('Hello my name is {:>20} .Nice to meet you'.format(name)) #right aligned
#print('Hello my name is {:<20} .Nice to meet you'.format(name))#Left aligned
#print('Hello my name is {:^20} .Nice to meet you'.format(name))#center aligned

#if we need to add keyword or positional argument, we do so before the colon

#print('Hello my name is {item:^20} .Nice to meet you'.format(name='Boitumelo',animal='cow',item='tv'))#center aligned

#Formatting numbers

number= 3.14159
#f is for float
#.2f is to display the first two digits after the decimal, since we placed 2
print('The number pi is {:.2f}'.format(number))

number=1000
#To place a comma at the thousand place we do the following
print('The number pi is {:,}'.format(number))

#To convert to binary
print('The number pi is {:b}'.format(number))

#To display as octo
print('The number pi is {:o}'.format(number))

#To display in hexadecimal, lower case x is lower case e
print('The number pi is {:x}'.format(number))

#To display scientific notation
print('The number pi is {:E}'.format(number))