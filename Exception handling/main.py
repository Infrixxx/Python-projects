#Exception =    event detected during execution
#               that interrupts the flow of the program

#Example of program that will intentional cause an exception

#numerator=int(input("Enter a number to divide   :"))
#denominator=int(input("Enter a number to divide by:    "))
#result=numerator/denominator
#print(result)

#five divided by zero will cause an exception, because division by zero is impossible
#we will need to surround code that may cause an exception in a try block



try:
    numerator = int(input("Enter a number to divide:    "))
    denominator = int(input("Enter a number to divide by: "))
    result = numerator / denominator
    print(result)
#we create an exception block that will take in zero division errors
#except  ZeroDivisionError:
    #print("We can't divide by zero, bhari")

#We can also write an exception for the case in which
# user enters string instead of number
#except ValueError:
    #print("Enter numbers only please")

#we can keep the except Exception
#in case there is an exception we cannot anticipate
#if code fails to run due to error it will print the below message
#except Exception:
    #print("Something went wrong")


#WE CAN ALSO USE : as e to handle exception, this will print the reason for exception

except  ZeroDivisionError as e:
    print(e)
    print("We can't divide by zero, bhari")


except ValueError as e:
    print(e)
    print("Enter numbers only please")


except Exception as e:
    print(e)
    print("Something went wrong")

#We can print our result if there are no exceptions
else:
    print(result)

#finally block will always execute regardless of the exception
finally:
    print("This will always execute")