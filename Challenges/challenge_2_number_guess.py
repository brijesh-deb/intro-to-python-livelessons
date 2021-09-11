"""
Number guessing game
The number to guess will be from 1 to 20 (inclusive).
The user will have 3 guesses to guess the number correctly.
After each wrong guess, the user will be told whether to
guess higher or lower next time.
If the user doesn't win, tell them the number.
"""
import random

def run_game():
    answer = random.randint(1, 20)
    count =0
    while(count<3):
        guess = int(input("Make a guess: "))
        if(guess== answer):
            print("Guessed correct")
            break
        elif(guess<answer):
            print("Guess higher number")
        else:
            print("Guess lower number")
        count = count+1

run_game()
