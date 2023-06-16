# daemon thread =   a thread that runs in the background, not important for program to run
#                   your program will not wait for daemon threads to complete before exiting
#                   non-daemon threads cannot normally be killed, stay alive until task is complete
#
#                   ex. background tasks, garbage collection, waiting for input, long-running process

import threading
import time

def timer():            #Function to describe how long someone is logged in
    print()
    count= 0
    while True:
        time.sleep(1)
        count+=1
        print("logged in for : ", count,"seconds") #This will print how long you logged in

x= threading.Thread(target=timer,daemon=True)   #thread x will be in charge of our timer and run it concurrently,
                                    # while we waiting for some user input.
x.start()                           #We can change our thread into a daemon thread so that when we
                                    # wish to exit, it exits. By addiing the "daemon=True"
                                    #This will kill the thread upon input from the user

#x.setDaemon(True)                   #This is to change thread to non daemon or daemon. Need to be done before start function
print(x.isDaemon())                 #This is to check if function is daemon or not

answer = input("Do you wish to exit?")