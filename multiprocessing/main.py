#**************************************************
# Python multiprocessing
#**************************************************
#multiprocessing=   running tasks in parallel on different cpu cores, bypasses GIL used for threading.
#                   mutliprocessing =   better for cpu bound tasks (heavy cpu usage)
#                   multithreading  =   better for io bound tasks(waiting around)
#                   with multithreading we limited to one thread at a time
#                   with multiprocessing we can proccesses parallel to one another on different cpu cores.

from multiprocessing import Process, cpu_count
import time

def counter(num):
    count =  0
    while  count<num:
        count+=1


def main(): #we will create process in our function

    #a= Process(target=counter, args=(1000000000,)) #args=will get the number from the user, this will count till one billion
    #a.start()
    # a.join()    #main process will wait for child process to finish


#**************************************************************************************
#   TO MAKE THE CODE RUN FASTER WE SPLIT THE COUNT AMOUNT TO 2 AND JOIN THE TWO THREADS
#   Splitting this will divert the process to all available cores
#   Creating more threads than availale cores will result in the code running slower
#**************************************************************************************
    print(cpu_count())  #This shows how many cores are on my computer
                        #The cpu count is 6
                        #since I can run six processess, I am creating two additional processes
                        #So this will take longer

    a = Process(target=counter, args=(125000000,))
    b = Process(target=counter, args=(125000000,))
    c = Process(target=counter, args=(125000000,))
    d = Process(target=counter, args=(125000000,))
    e = Process(target=counter, args=(125000000,))
    f = Process(target=counter, args=(120000000,))
    g = Process(target=counter, args=(125000000,))
    h = Process(target=counter, args=(125000000,))

    a.start()
    b.start()
    c.start()
    d.start()
    e.start()
    f.start()
    g.start()
    h.start()

    a.join()
    b.join()
    c.join()
    d.join()
    e.join()
    f.join()
    g.join()
    h.join()

    print("finished in: ", time.perf_counter(),"seconds")
if __name__=="__main__" :    #this is so if we create a child process it will copy our module but not execute it
    main()


