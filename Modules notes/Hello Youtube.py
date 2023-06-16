# Module:   A file containing python code
#           used with modular programming
#           which is a concept of separating a program into parts.
#           Our main module is Hello youtube
#           We create a module filled with message functions called messages
#           We do so by creating a new python file, called messages
#           To use the messages we need to import the module Messages

#import Messages
#To use a function from the module:
# we type The_name_of_the_module.the_name_of_the_function
#so Messages.hello() will call the hello function found in the Messages module

#Messages.bye()
#Messages.hello()

#We can also make it more efficient by importing the module as something.
#Say we import Messages as M

import Messages as M

#Now we can write M.function() this will work the same as Messages.function()

print(M.hello())

#Another way to call functions within a module is to use
from Messages import hello,bye
#So we no longer need to use
#function name and function, we can call the function directly.

print(bye())

#Another to import everything(all functions) is to say:
#from Messages import *
#Not recommended if working on a big project as this can
#result in a naming conflict, because some of these modules have similar names.

#Python has a list of pre-written modules we have access to
#To get the list of these modules we just need to type help("modules")

help("modules")

#Can also go to the python site