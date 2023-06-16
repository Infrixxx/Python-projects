#if statement = a block of code that will execute if it's condition is true

age=int(input("How old are you?"))

#if age >=18:
    #print("You are an adult!")



#elif age < 0:
    # if age is below zero, we use else or if statement(elif)
    #we can use unlimited amounts of elif statement
    #print("You are not yet born.")


#elif age==100:
    #order of the if statement matters, since we have set the first if statement
    #to say you an adult the condition if met will print you an adult despite the user saying they 100 years old.
    #print("You are a century old")


#else:
    # if condition is false, we add an else statement
    # indetation must be directly below the if statement
    #if the if satement and elif statement are both false
    #print("You are a child! :D")


#In order to fix this and have the first statement of the century go through, we make it the initial conditon


if age==100:

    print("You are a century old")

elif age >=18:
    print("You are an adult!")

elif age < 0:

    print("You are not yet born.")

else:

    print("You are a child! :D")

#we go down the order of the code until we reach the else statement.
