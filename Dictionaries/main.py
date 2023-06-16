# Dictionary= A changeable, unordered collection of unique key: value pairs
#             Fast because they use hashing, allow us to access a value quickly


capitals={'USA':'Washington DC',
          'India':'New Delhi',
          "Russia":'Moscow'}

#To print a value of a key
#print(capitals["Russia"])

#If I insert a key that doesn't exist in the dictionary, I will bump into an error
#To check if the key is in the dictionary we use the get command
#This will return none if the key is not in the dictionary
#print(capitals.get('Germany'))

#To print the values we use
#print(capitals.values())

#To print all the items in the dictionary we use:
#print(capitals.items())

#Another way to display all the key value pair in the dictionary

 #for key,value in capitals.items():
    #print(key,value)

#Dictionaries can be changed or updated after the program is running
#capitals.update({'Germany':'Berlin'})

#Pop method to remove key-value pair
#capitals.pop('India')

#To clear everything we use the clear method
#capitals.clear()


for key,value in capitals.items():
    print(key,value)

