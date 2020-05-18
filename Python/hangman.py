import time
import random

print("Welcome to hangman, try to guess a word:")
time.sleep(0.5)
print ("Game has begone")
time.sleep(0.5)

# word list which a random word is picked
words = ["testing"]
answer = random.choice(words)


guesses = ""
turns = 5
wrong = []

while turns > 0:
    num_failed = 0

    for letter in answer:
        if letter in guesses:
            print(letter,)
        else:
            print("_",)
            num_failed += 1

    if num_failed == 0:
        print("Congrats you won!!")
        break
    
    print
    guess = str(input("Guess a letter:"))
    guesses += guess

    if guess not in answer:
        turns -= 1
        print("Wrong character")
        wrong.append(guess)
        print("You have", + turns, "more guesses")
        print("You have already guessed", str(wrong), "incorrectly")
        
        if turns == 0:
            print("You Lose")
            print("The words was"+answer)
