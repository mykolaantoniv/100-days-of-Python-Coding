rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
import random

#Get user choice
user_choice = input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors. \n")

#Convert user number in to figure
if user_choice == "0":
  print("Your choice:", rock)
elif user_choice == "1":
  print("Your choice:", paper)
elif user_choice == "2":
  print("Your choice:", scissors)
else:
  print("You put wrong number!")

#Convert pc choice number in to figure

pc_choice = str(random.randint(0, 2))

if pc_choice == "0":
  print("Computer choice:", rock)
elif pc_choice == "1":
  print("Computer choice:", paper)
else:
  print("Computer choice:", scissors)


# Determine the winner
if user_choice == pc_choice:
    print("It's a tie!")
elif (user_choice == "0" and pc_choice == "2") or (user_choice == "1" and pc_choice == "0") or (user_choice == "2" and pc_choice == "1"):
    print("You win!")
else:
    print("You lose!")