#thread =   a flow of execution. Like a seperate order of instructions.
#           However each thread takes a turn running to achieve concurrency
#           GIL =  (global interpreter lock)
#           allows only one thread to hold the control of the python intepreter at any one time


#cpu bound = program/ task spends most of it's time waiting for internal events (CPU intensive)
#            use multiprocessing.

#io bound = program/ task spends most of it's time waiting for external events  (user input,web scraping)
#           use multithreading

import threading
import time

def eat_breakfast():
    time.sleep(3)
    print("You eat breakfast")

def drink_coffee():
    time.sleep(4)
    print("You drink coffee")
def study():
    time.sleep(5)
    print("You finish studying")

#eat_breakfast()
#drink_coffee()
#study()

#*************************************************************************
#Multithreading is shown above, as we have three functions running concurrently
#**************************************************************************

#Since we have a thread responsible for running each thread concurrently unlike
#previous function, the program only takes 5 seconds to run.
#The main thread calls the active count function and enumerate function before the other threads
#As the main thread doesn't wait for the other threads but runs at the same time with them.

x= threading.Thread(target=eat_breakfast, args=())
x.start() #we have an additional thread responsible for breakfast

y= threading.Thread(target=drink_coffee, args=())
y.start() #we have an additional thread responsible for drinking coffee

z= threading.Thread(target=study, args=())
z.start() #we have an additional thread responsible for study

#************************************************************************************
#Say we would like the main thread to wait around for the first thread.
x.join()    #This will make the main wait until the first thread is called
y.join()
z.join()

print(threading.active_count()) # active count of threads running.
print(threading.enumerate())    #list of all running threads
print(time.perf_counter())      #calls peformance function which shows how long main thread takes to complete.
