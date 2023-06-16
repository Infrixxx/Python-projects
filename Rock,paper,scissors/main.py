#We need the computer to make a random choice
#we will need to pick a random choice

import random

#choices=['rock', 'paper','scissors']

#PC=random.choice(choices)
#print(PC)

#player=input('rock,paper or scissors? :')

#print("PC :",PC)
#print("Player: ",player)

#Now what if our player doesn't pick the correct option
#We will write a while loop to avoid this
#player=None
#The loop will keep asking until the answwer is one of the choices
#while player not in choices:
    # we need to initialise player, by saying player=None


    #player = input('rock,paper or scissors? :')
    #Now to account for key sensitivity
    # we will convert all our information to lower case
    #player = input('rock,paper or scissors? :').lower()


#Now we check on the win conditions
#if player==PC:
 #   print("Tie")

#elif player=='rock':
 #   if PC=='paper':
  #      print("You lose")
   # elif PC=="scissors":
    #     print('you win')

#elif player=='paper':
  #  if PC=='scissors':
   #     print("You lose")
   # elif PC=="rock":
#     print('you win')

#elif player=='':
#   if PC=='paper':
#       print("You lose")
 #   elif PC=="scissors":
#       print('you win')

#print("PC :", PC)
#print("Player: ", player)

#To ask if a player wants to play again or play another round,
# would be by putting the above code in a while loop
#make use of the while True loop
while True:
    choices = ['rock', 'paper', 'scissors']

    PC = random.choice(choices)
    player = None
    while player not in choices:
        # we need to initialise player, by saying player=None

        # Player chocie
        player = input('rock,paper or scissors? :').lower()
        print("PC :", PC)
        print("Player: ", player)
    # Win Conditions
    if player == PC:
        print("Tie")


    elif player == 'rock':
        if PC == 'paper':
            print("You lose")
        elif PC == "scissors":
            print('you win')


    elif player == 'paper':
        if PC == 'scissors':
            print("You lose")
        elif PC == "rock":
            print('you win')


    elif player == '':
        if PC == 'paper':
            print("You lose")
        elif PC == "scissors":
            print('you win')

    #Ask the user if they would love to play again
    play_again =    input("Play again, yes/no").lower()



