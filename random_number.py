# 1. When the game starts. Print the name of game and ask the user for his/her name.
# 2. randomly generate a number between 1 to 10 and ask the user to guess the number
# 3. If user's guess is correct print win message else print loss message
import random
game = "Random selection of Number"
print(game)

user = input("Please enter your name: ")
print(f"Hello {user}, Welcome to the Game")

def game():
    number = random.randint(1,5)

    num = int(input("Guess the number between 1 to 5: "))

    if num == number:
        print(f"Congratulation {user} You won the Game, {user} you choosed {num} and the random number is {number}")
    else:
        print(f"You loose the Game, {user} you choosed {num} and the random number is {number}")

    user_decision = input("Do you wanna play again?, type yes if you want to play again: ")
    if user_decision == "yes":
        game()
    else:
        print(f"Bye, Bye {user}")


game()





