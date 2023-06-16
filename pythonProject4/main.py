#learnt code revision

#string slicing

website="http://Boitumelo.com"
website01='http://Charles.com'

cut=slice(7,-4)
#This is using the slicing method
#print(website[cut])
#This is using the indexing method
#print(website[7:-4])


age=input("What is your age")
age=int(age)
#age+=1

if age==100:
    print("Your are a century old" )

elif age < 0:
    print("You are not yet born")

elif age>18:
    print("You are an adult")
else:
    print("You are a child")

print(age)
