"""Generate a random number between 1 and 9 (including 1 and 9). Ask the user to guess the number, then tell them whether they guessed too low, too high, or exactly right. (Hint: remember to use the user input lessons from the very first exercise)
Extras:
Keep the game going until the user types “exit”
Keep track of how many guesses the user has taken, and when the game ends, print this out."""

import random
number = random.randint(1,100)
count = 0
answer = input("do you want to guess the number - yes/exit : ").lower()
while answer != 'exit':
      guess = int(input("Guess the number!! : "))
      count +=1
      if number == guess:
          print("you guessed the correct number: {}".format(number))
          break
      elif number != guess:
          print("you guess the wrong number!!")
          if number>guess:
             print("Hint: You need to add {} number to generate the desired result ".format(number-guess))
          elif number < guess:
               print("Hint: You need to subtract {} to generate the desired result ".format(guess-number))
          answer = input("do you want to try again: yes/exit : ").lower()
          if answer == 'exit':
                print("total attempts you made are {}".format(count))
                exit()

      else:
            print("out of range.....Please enter within range : ")
            answer = input("do you want to try again: yes/exit : ").lower()
            if answer == 'exit':
                print("total attempts you made are {}".format(count))
                exit()
print("you guessed right....you Won!! congratulations.")
print("total attempts you made are {}".format(count))


