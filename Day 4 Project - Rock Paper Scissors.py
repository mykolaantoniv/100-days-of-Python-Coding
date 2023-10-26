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
user_choice = input("What do you choose? Type 0 for Rock, 1 for paper or 2 for Scissors. \n")

#Convert user number in to figure
if user_choice == "0":
  print(rock)
elif user_choice == "1":
  print(paper)
elif user_choice == "2":
  print(scissors)
else:
  print("You put wrong number!")

#Convert pc choice number in to figure
#pc_choice = random.randint(0, 2)
pc_choice = "2"

if pc_choice == "0":
  print(rock)
elif pc_choice == "1":
  print(paper)
else:
  print("Computer choice:", scissors)

#Find a winner
if user_choice == "0" and pc_choice == "0":
  print("One more time!")
elif user_choice == "0" and pc_choice == "1":
  print("You win!")
elif user_choice == "0" and pc_choice == "2":
  print("You lose!")
elif user_choice == "1" and pc_choice == "0":
  print("You win!")
elif user_choice == "1" and pc_choice == "1":
  print("One more time!")
elif user_choice == "1" and pc_choice == "2":
  print("You lose!")
elif user_choice == "2" and pc_choice =="0":
  print("You lose!")
elif user_choice == "2" and pc_choice =="1":
  print("You win!")
elif user_choice == "2" and pc_choice =="2":
  print("One more time!")