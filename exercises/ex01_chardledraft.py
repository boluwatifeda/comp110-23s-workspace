"""EX01 - Chardle - A cute step toward Wordle."""

_author_ = "730597726"

word: str = input ("Enter a 5-character word:")

if(len(word) > 5):
    print("Character must be 5 characters long.")
if(len(word) < 5):
    print("Character must be 5 characters long.")
if(len(word) == 5):
    
    character: str = input ("Enter a single character:")
    if(len(character) == 1):
        print("Searching for " + character + " within " + word + ".")
    if(len(character) != 1):
        print("Error: Must be a single character.")

count: int = 0
if(character == word[len(word)-5]):
    print(character + " found at index 0.")
    count = count + 1
if(character == word[len(word)-4]):
    print(character + " found at index 1.")
    count = count + 1
if(character == word[len(word)-3]):
    print(character + " found at index 2.")
    count = count + 1
if(character == word[len(word)-2]):
    print(character + " found at index 3.")
    count = count + 1
if(character == word[len(word)-1]):
    print(character + " found at index 4.")
    count = count + 1
if(count == 0):
    print("No instances of " + character + " found in " + word + ".")
if(count == 1):
    print("1 instance of " + character + " found in " + word + ".")
if(count > 1 ):
    print(count + "instances of " + character + " found in " + word + ".")

