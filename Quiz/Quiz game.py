#We going to create a quiz game
#We need to first consider how the skeleton of this game will be

#We going to need four functions

#----------------------
def new_game():
    guesses=[]
    correct_guesses=0
    question_num=1

    #This prints all the questions
    for key in questions:
        #we can print something to seperate the questions
        print("----------------------")
        print(key)
        #to display the different options for each question
        # we can use a nested for loop
        for i in options[question_num-1]:   #since we set the variable to
                                            # 1 we subtract one, to begin
                                            #at index 0, rather than print
                                            #all options
            print(i)
        #To create a variable that will take in user input
        guess=input("Enter (A,B,C or D): ")

        guess=guess.upper()#since strings are case sensitive
                            # we need to convert them to upper case

        #This will add the guess to the list of guesses
        guesses.append(guess)

        #The key is the correct answer
        correct_guesses+=check_answer(questions.get(key),guess)
        #Now we need to incremenet our question number for every iteration
        question_num+=1     #This will all the options for each question

    display_score(correct_guesses, guesses)



#----------------------
def check_answer(answer,guess):
    #To check our answer is equal to guess
    if answer==guess:
        print("Correct!")
        return 1
    else:
        print('Wrong!')
        return 0

#since we are returning values, we need to assign the point
#we may or may not receive.

#----------------------
def display_score(correct_guesses, guesses):
    print('----------------------')
    print("Results : ")
    print("Answers: ",end='  ')
    for i in questions:
        print(questions.get(i),end='  ')
    print()

    print("Guesses: ", end="  ")
    for i in guesses:
        print(i,end='  ')
    print()

    Score=(correct_guesses/len(questions))*100
    print("Your score is "+str(Score)+"%")


#----------------------
def play_again():

    response=input("Do you want to play again? Yes or No:")
    response=response.upper()

    if response=="YES":
        return True
    else:
        return False


#We going to need to create a dictionary
# to store the question and the answer

questions={"1. Who created python":"A","2. What year was python created":"B",
           "3. Python is tributed to which comedy group?: ":"C",
           "4. Is earth round":"A"}

#we need a collection to hold the possible answers to the list
#so we will need to create a 2D list

options=[["A. 116", "B. 117", "C. 118", "D. 119"],
         ["A. Whale", "B. Crocodile", "C. Elephant", "D. Ostrich"],
         ["A. 206", "B. 207", "C. 208", "D. 209"],
         ["A. Mercury", "B. Venus", "C. Earth", "D. Mars"]]

#First we call in the new game function to create a new game
new_game()

#Loop for playing again
while   play_again():
    new_game()

print("Byeeee!!!")