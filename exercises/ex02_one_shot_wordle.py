"""EX02 - One-Shot Wordle - Loops!"""
__author__ = "730597726"

SECRET: str = "python"

guess: str = input(f"What is your {len(SECRET)}-letter guess? ")

playing: bool = True

WHITE_BOX: str = "\U00002B1C"
GREEN_BOX: str = "\U0001F7E9"
YELLOW_BOX: str = "\U0001F7E8"

alternate_index: int = 0
secret_index: int = 0
emoji_string: str = ""
contains: bool = False

while playing:
    while(len(guess) != 6):
        guess = str(input(f"That was not {len(SECRET)} letters! Try again: "))
    
    if(guess != SECRET):
        while secret_index < len(SECRET):
            contains = False
            if guess[secret_index] == SECRET[secret_index]: 
                emoji_string = emoji_string + GREEN_BOX
            else:
                alternate_index = 0
                while alternate_index < len(SECRET) and not(contains):
                    contains = False
                    if guess[secret_index] == SECRET[alternate_index]:
                        contains = True
                    alternate_index = alternate_index + 1
                if contains == True:
                    emoji_string = emoji_string + YELLOW_BOX
                if contains == False:
                    emoji_string = emoji_string + WHITE_BOX      
            secret_index = secret_index + 1
        print(emoji_string)
        print("Not quite. Play again soon!")
        playing = False
    if(guess == SECRET):
        while secret_index < 6:
            if guess[secret_index] == SECRET[secret_index]:
                emoji_string = emoji_string + GREEN_BOX
            secret_index = secret_index + 1
        print(emoji_string)
        print("Woo! You got it!")
        playing = False