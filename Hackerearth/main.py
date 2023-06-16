#First project


N=int(input('Enter any number from 0 to 10'))

while not(N>=0 and N<=10):
    N=int(input('Enter any number from 0 to 10'))

K=input("Please enter helloworld: ").lower()
S=len(K)
while not(S>=1 and S<=15):
    S=int(input("Please enter helloworld: "))

print(N*2)
print(K)
