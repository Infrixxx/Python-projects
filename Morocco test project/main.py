# Morocco win test


Morroco=None

while True:
    k=input('Is the African dream still running? yes/no').lower()
    if k==('yes'):
        y=input("Did we win?").lower()
        if y==("yes"):
            print("finals here we go")
        else:
            print("Penalties here we go")
        break
    else:
        print("We try again in 4 yearss")
        break

def Morocco_goal():
    print("For africa!!!!!")

def France_goal():
    k=input("Was it Mbappe?")
    if k==('yes'):
        print("My ninja turtle")
    else:
        print("Well done european Africa")

France_goal()
Morocco_goal()

smallest = None
print("Before:", smallest)
for itervar in [3, 41, 12, 9, 74, 15]:
    if smallest is None or itervar < smallest:
        smallest = itervar
        break
    print("Loop:", itervar, smallest)
print("Smallest:", smallest)