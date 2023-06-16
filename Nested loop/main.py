# nested loops= The 'inner loop' will finish all of it's iteration before
#               finishing one iteration of the 'outer loop'

#We are going to build a rectangle using nested loops
#We will cast the input of the user into integers

rows=int(input('How many rows:      ?'))
columns=int(input('How many columns:    ?'))
symbol=input("Enter a symbol to use :   ")

for i in range(rows) :
    for j in range(columns):
        print(symbol, end='')
    print()

for i in range(5):
    print(i,end='')