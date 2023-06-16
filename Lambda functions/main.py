#Lambda function = function written in 1 line using lambda keyboard
#                  accepts any number of arguments, but only have one expression.
#                   (think of it as a shortcut)
#                   (useful if needed for a short period of time, throw-away)

#lambda parameters: expression

#def double(x):
#    return x*2

#print(double(5))

#Now let's write the above function as a lamba function

double = lambda x:x*2 #we say lamba parameter: function/expression
print(double(5))

#Now say we want to multiply two numbers

multiply= lambda x,y : x*y
print(multiply(2,4))

#Now say we want to add three numbers together
add= lambda x,y,z : x+y+z
print(add(1,5,7))

#string function
full_name= lambda first_name,middle_name, Last_name: first_name+" "+middle_name+' '+Last_name
print(full_name(Last_name='Rachoshi',first_name='Boitumelo', middle_name='Charles'))

#function to check age
age_check=lambda age:True if age>=18 else False
print(age_check(18))

multiply=lambda z,a :z*a

print("Be back by "+str(multiply(4,2))+"pm")