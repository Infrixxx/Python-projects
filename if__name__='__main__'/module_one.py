#***********************************
#if __name__=='__main__'
#***********************************

#1. Module can run as a standalone program
#2. Module can be imported and used by other modules

#Python intepreter sets "special variables" , one of which is __name__
#Pyhon will assign the __name__ variable a value of '__main__' if it's
#the initial module being run

#checking to see if module is being run directly or indirectly
#if __name__=='__main__':
   # print("Running this module directly")
#else:
    #print("running other module indirectly")

#************************************************************

#say in module one there is a function we would like to access in module two

def hello():
    print('Hello!')

if __name__=='__main__':
    #since we cannot run the function from module one as a standalone functioin
    # we then check if the module is the main one
    #then we call the function
    hello()
