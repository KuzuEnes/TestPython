import random

player = input("Enter the player's name: ")


computer_list = ["rock","paper","scissors",]
computer_choice = random.choice(computer_list)

player_choice = input("Type rock, paper or scissors  ").lower()
print("Computer chose " + computer_choice)

if player_choice == computer_choice:
      print("Draw!")

elif ((player_choice == "rock" and computer_choice == "scissors") or ( player_choice =="paper" and computer_choice == "rock") or (player_choice == "scissors" and computer_choice == "paper")):
      print(  "You Won!! ")

else:
      print("Computer Won!! ")




