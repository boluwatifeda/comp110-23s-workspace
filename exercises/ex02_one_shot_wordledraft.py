"""EX02 - One-Shot Wordle - Loops!"""
__author__ = "730597726"

SECRET: str = "python"

guess: str = input("What is your 6-letter guess? ")

playing: bool = True

WHITE_BOX: str = "\U00002B1C"
GREEN_BOX: str = "\U0001F7E9"
YELLOW_BOX: str = "\U0001F7E8"

current_character: int = 0
secret_index: int = 0
emoji_string: str = ""

while playing:
    if(len(guess) > 6):
        guess = str(input("That was not 6 letters! Try again: "))
    if(len(guess) < 6):
        guess = str(input("That was not 6 letters! Try again: "))
    if(len(guess) == 6):
        if(guess != SECRET):
            while secret_index < 6:
                if guess[secret_index] == SECRET[secret_index]: 
                   emoji_string = emoji_string + GREEN_BOX
                else:
                   emoji_string = emoji_string + WHITE_BOX
                secret_index = secret_index + 1
            print(emoji_string)
            print("Not quite. Play again soon!")
            playing = False
        if(guess == SECRET):
            while secret_index < 6:
                if guess[secret_index] == SECRET[secret_index]:
                    emoji_string = emoji_string + GREEN_BOX
                else:
                    emoji_string = emoji_string + WHITE_BOX
                secret_index = secret_index + 1
            print(emoji_string)
            print("Woo! You got it!")
            playing = False