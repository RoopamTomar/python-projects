import random
name = input("enter your name : ").title()
print("Hello {} Welcome to Hangman Game".format(name))

print("Disclaimer: You need to guess the word within n+2 number of tries else you will lose the game where n is the length of the word")
print("lets start playing!!!")


words = ["apple","mango","orange","pomogranate","watermelon"]
word = random.choice(words)
attempt = len(word)+2
print("choosen word is having {} number of characters and its a fruit.".format(len(word)))
guesses = ""

while attempt > 0:
    guess = input("\nenter the alphabet:")
    guesses += guess
    set_g = set(guesses)
    set_w = set(word)
    if set_g.intersection(set_w) == set_w:
        yes = input("you left with {} attempts ,do you want to exit,press y:".format(attempt))
        print("you won!!")
        exit()

    elif guess in word:
       for char in word:
           if char in guesses:
               print(char, end="")

           else:
               print("_", end="")
       attempt -= 1




    elif guess not in word:
         print("Try again!! incorrect")
         continue
         attempt -= 1


    elif attempt == 0:
          print("out of attempts")






