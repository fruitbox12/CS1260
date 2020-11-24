###DISCLAMER MY PROFESSOR TOLD ME TO USE GLOBAL VARIABLES I HAVE NO IDEA WHY

"""

GO 

CREATE TABLE CS1270(

	A INT NULL,
	B NCHAR(10) NULL
);

GO

INSERT INTO CS1270(A,B) VALUES(1, 'Player2')
INSERT INTO CS1270(A,B) VALUES(2, 'Player2')
INSERT INTO CS1270(A,B) VALUES(3, 'Player2')
INSERT INTO CS1270(A,B) VALUES(4, 'Player2')
INSERT INTO CS1270(A,B) VALUES(5, 'Player2')

go 

SELECT * FROM CS1270
"""
import random
from random import randint
import pyodbc
import tkinter as tk

driver= '{SQL Server Native Client 11.0}'

conn = pyodbc.connect(
    Trusted_Connection='Yes',
    Driver='{ODBC Driver 11 for SQL Server}',
    Server='OOF',
    Database='SQLContactsBackup'
)



window = tk.Tk()
window.geometry("400x300")
window.title("Rock Paper Scissors Game")
PlayerScore = 0
ComputerScore = 0
PlayerChoice = ""
ComputerChoice = 0
 
computerOptions = ["rock", "paper", "scissors"]


class gameLogic:
    def __init__(self):

        

        def randomize():
            return computerOptions[randint(0, 2)]

        conn1 = conn
        # CRUD Functions
        def create(conn):
                    print("Create")
                    global PlayerScore
                    global ComputerScore

                    cursor = conn.cursor()
                    cursor.execute(
                        'insert into CS1270(a,b) values(?,?);',
                        (PlayerScore, ComputerScore)
                    )
                    conn.commit()
                    read(conn)
                    
        def read(conn):
                    print("Read")
                    cursor = conn.cursor()
                    cursor.execute("select * from CS1270")
                    for row in cursor:
                        print(f'row = {row}')
                    print()
                    
        def update(conn):
                    global PlayerScore
                    global ComputerScore
                    print("Update")
                    cursor = conn.cursor()
                    cursor.execute(
                        'update CS1270 set b = ? where a = ?;',
                        (PlayerScore, ComputerScore)
                    )
                    conn.commit()
                    read(conn)

        def delete(conn):
                    print("Delete")
                    cursor = conn.cursor()
                    cursor.execute(
                        'delete from CS1270 where a  < 0;'
                    )
                    conn.commit()
                    read(conn)

        # Game Functions
        def choiceNum(choice):
            playeroptions = {'rock': 0, 'paper': 1, 'scissors': 2}
            return playeroptions[choice]
         
         
        def numChoice(number):
            playeroptions = {0: 'rock', 1: 'paper', 2: 'scissors'}
            return playeroptions[number]
         
         
        def result(human_choice):
            global PlayerScore
            global ComputerScore
            ComputerChoice = randomize()
            user = choiceNum(human_choice)
            comp = ComputerScore
            if (user == comp):
                print("Tie")
                
            elif ((user - comp) % 3 == 1):
                print("You win")
                PlayerScore += 1
            else:
                print("Player 2 wins")
                ComputerScore += 1
            update(conn)
            text_area = tk.Text(master=window, height=20, width=30, bg="white")
            text_area.grid(column=0, row=4)
            answer = "Your Choice: {uc} \nOther Players Choice : {cc} \n Your Score : {u} \n Other Players : {c} \n Highest Scores : {uu} ".format(
                uc=PlayerChoice, cc=ComputerChoice, u=PlayerScore, c=ComputerScore, uu = update(conn))
            text_area.insert(tk.END, answer)
             

         ###global variables are not ideal, 
        def rock():
            global PlayerChoice
            global computerOptions
         
            PlayerChoice = "rock"
            result(PlayerChoice)
         
         
        def paper():
            global PlayerChoice
            global computerOptions
         
            PlayerChoice = "paper"
            result(PlayerChoice)
         
         
        def scissor():
            global PlayerChoice
            global computerOptions
            PlayerChoice = "scissors"
            result(PlayerChoice)
         
 
            
        def window1():
            label = tk.Label(text="")
            guiButton = tk.Button()

            rockButton = tk.Button(text="       Rock       ",bg="green",command=rock)
            rockButton.grid(column=0,row=1)
            paperButton = tk.Button(text="       Paper      ",bg="red",command=paper)
            paperButton.grid(column=0,row=2)
            scissorButton = tk.Button(text="      Scissor     ",bg="yellow",command=scissor)
            scissorButton.grid(column=0,row=3)
            window.mainloop()
            label = tk.Label(
                text="",
                foreground="white",  # Set the text color to white
                background="black"  # Set the background color to black
            )


        window1()
        read(conn)
        create(conn)
        delete(conn)

        
obj = gameLogic()
conn.close()

