#Time module
#epoch = a date and time from which a computer measures system time

import time

#print(time.ctime(10000))    #this will take a time expressed in seconds and converts it to string
                            #epoch= when your computer thinks time began

#print(time.time())          # return current seconds since epoch, using your computer clock

#To retrieve current date and time

#print(time.ctime(time.time()))

#another way is to create local time object

#time_object=time.localtime()
#print(time_object)

#You can get the UTC time too by
#time_object=time.gmtime()

#to convert time object to readable object we need to format it
#local_time=time.strftime("%B %d %Y %H:%M:%S ",time_object) # store to a variable
#print(local_time)

#time_string ="20 December,  2022"
#time_object=time.strptime(time_string, "%d %B,  %Y") # This will cast the string to a time object
#print(time_object)

#time_tuple=(2020,4,20,4,20,0,0,0,0)    #Time tuple
#time_string= time.asctime(time_tuple)  #time.asctime() converts a time tuple to a string
#print(time_string)

#time_tuple=(2020,4,20,4,20,0,0,0,0)    #Time tuple
#time_string= time.mktime(time_tuple)  #converts the tuple to seconds since epoch
#print(time_string)
