import random

def play():
    options = ["Rock","Paper","Scissors"]
    AI = random.choice(options)
    user = input("Pick either Rock, Paper or Scissors: ")
    user = user.lower()
    if user == 'rock' or 'paper' or 'scissors':
        print ("The computer has drawn %s, you chose %s " % (AI,user))
    if user == 'rock':
        if AI == 'Rock':
            print ('Tie Game')
        elif AI == 'Paper':
            print ('AI Wins')
        else:
            print ('User Wins')
    if user == 'paper':
        if AI == 'Rock':
            print ('User Wins')
        elif AI == 'Paper':
            print ('Tie Game')
        else:
            print ('AI Wins')
    if user == 'scissors':
        if AI == 'Rock':
            print ('AI Wins')
        elif AI == 'Paper':
            print ('User Wins')
        else:
            print ('Tie Game')
play()
while True:
    answer = input("do you want to play again?, enter Yes to play or No to stop ")
    answer = answer.lower()

    if answer == 'yes':
        play()
    elif answer == 'no':
        break
    else:
        print("Error, wrong user input")
