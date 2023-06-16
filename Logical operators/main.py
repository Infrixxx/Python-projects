#logical operators(and,or, not) = are used to check  two or more conditional statements

temp=int(input('What is the temperature outside: ? '))

#This is using the and logic operator
#if temp>=0 and temp<=30:
    #print('The temperature is good today')
    #print('Go outside')

#This is using the or logic operator
#elif temp<0 or temp>30:
    #print('The temperature is very bad')
    #print('Stay inside.')

#This is using the not logic operator
if not(temp>=0 and temp<=30):
    print('The temperature is very bad today.')
    print('Stay inside.')

elif not(temp<0 or temp>30):
    print('The temperature is good today')
    print('Go outside')

