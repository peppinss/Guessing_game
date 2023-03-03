
import random
from art import logo

def userchoice(gamemode):
    gameover = False
    while not gameover:
        while True:
            try:
                user_input = int(input("Make a guess: "))
                break
            except:
                print("it must be a number")
        if user_input == ia:
            print(f"I was thinking about {ia} you're right")
            return
        elif user_input > ia:
            print("Too high")
            gamemode -= 1
            print(f"You have {gamemode} attempts left")
        elif user_input < ia:
            print("Too low")
            gamemode -= 1
            print(f"You have {gamemode} attempts left")
        else:
            print("something went wrong")
        if gamemode == 0:
            print("gameover")
            gameover = True

def difficulty():
    while True:
        user_input = input("Choose a difficulty, Type 'easy' or 'hard' ").lower()
        if user_input == "e" or user_input == "easy":
            return 10
        elif user_input == "h"or user_input == "hard":
            return 5
        else:
            print("i did not understand could you please type it again?")

def main():
    global ia
    print(logo)
    print("Welcome to the number guessing name\n I'm thinking of a number between 1 and 100\n")
    gamemode = difficulty()
    ia = random.choice(range(101))
    userchoice(gamemode)



if __name__ == '__main__':
    playagain = False
    while not playagain:
        main()
        while True:
            input_user = input("Wanna play again?")
            if input_user == "y" or input_user == "yes":
                break
            elif input_user == "n" or input_user == "no":
                playagain = True
                print("Thanks for playing")
                break

