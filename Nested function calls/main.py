# Nested function calls:    function calls inside other function calls
#                           innermost functions are resolved first
#                           returned value is used as argument for the next outer function

#num=input("Enter a whole positive number")
#num=float(num)
#num=abs(num)
#num=round(num)
#print(num)

#The above can be done with less line of code , using a nested function

print(round(abs(float((input("Enter a whole positive number"))))))