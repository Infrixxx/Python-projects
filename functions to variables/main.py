def hello():
    print("Hello")

print(hello)    #This will print where the function
                # is within the computer's memory.
#we can assign the address to a variable
hi=hello
print(hi)

#if we call the hi() it will call the hello function

hi()
hello() #we can also use this to call the hello function,
        # so our function has two names

Say=print

#so we can use print or say

Say("Woooaaa, I cant believe this works")