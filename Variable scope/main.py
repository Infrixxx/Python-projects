#Scope =    the region that a variable is recognized
#           A variable is only available from inside the region it is created.
#           A    global and locally scope versions of a variable a created

def dislay_name():
    name='Boitumelo' #local variable, with local scope, since it is only available inside the function
    print(name)

name='Boitumelo'    #global scope(available inside and outside the function


#This will print the local variable and the global variable
display_name()
print(name)

#Python follows a rule called the LEGB
# L-lOCAL
# E-ENCLOSED
# G-GLOBAL
# B-BUILT-IN
