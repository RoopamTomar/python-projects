"""Make a two-player Rock-Paper-Scissors game. (Hint: Ask for player plays (using input), compare them, print out a message of congratulations to the winner, and ask if the players want to start a new game)
Remember the rules:
Rock beats scissors
Scissors beats paper
Paper beats rock"""

player1=input("do you want to play the game:yes/no :").lower()
player2=input("do you want to play the game:yes/no :").lower()

while player1 and player2 == 'yes':
        print("Lets play the game!!")
        print("Rules are:")
        print("Rock beats scissors")
        print("Scissors beats paper")
        print("Paper beats rock")
        input1 = input("Choose Rock/Paper/Scissors").title()
        input2 = input("Choose Rock/Paper/Scissors").title()
        if input1 == 'Rock' and input2 == 'Scissors':
            if input1 == 'Rock' and input2 == 'Scissors':
               print("player1 won!!")
            else:
               print("player2 won!!")
        elif input1 == 'Scissors' and input2 == 'Paper':
            if input1 == 'Scissors' and input2 == 'Paper':
               print("player1 won!!")
            else:
               print("player2 won!!")
        elif input1 == 'Paper' and input2 == 'Rock':
            if input1 == 'Paper' and input2 == 'Rock':
               print("player1 won!!")
            else:
               print("player2 won!!")
        elif input1 == 'Rock' and input2 == 'Paper':
            if input1 == 'Rock' and input2 == 'Paper':
                print("player2 won!!")
            else:
                print("player1 won!!")
        elif input1 == 'Scissors' and input2 == 'Rock':
            if input1 == 'Scissors' and input2 == 'Rock':
                print("player2 won!!")
            else:
                print("player1 won!!")
        elif input1 == 'Paper' and input2 == 'Scissors':
            if input1 == 'Paper' and input2 == 'Scissors':
                print("player2 won!!")
            else:
                print("player1 won!!")
        else:
            if input1 == input2:
               print("tie in this match! try again!!")
        player1=input("do you want to play the game:yes/no").lower()
        player2=input("do you want to play the game:yes/no").lower()

        if player1 and player2 == 'no':
           print("either or both of you dont want to play more")
           exit()
        elif player1 =='yes' and player2 == 'no':
            print("either or both of you dont want to play more")
            exit()
        elif player1 =='no' and player2 == 'yes':
            print("either or both of you dont want to play more")
            exit()