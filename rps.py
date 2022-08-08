# random module functionality
import random

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

# Getting user input, storing this for choice of Rock, Paper or Scissors
user_choice = int(
    input('What do you choose? Type 0 for Rock, 1 for Paper and 2 for Scissors \n'))

# Storing all 3 variables in a list to randomise and select from
rps = [rock, paper, scissors]

# randomly generating a number based on length of list and using it to select list index
computer_rps = random.randint(0, len(rps) - 1)
computer_choice = rps[computer_rps]

# we cover each user choice and within those calculate each possible computer choice
if user_choice == 0:
    print(rps[0])
    if computer_rps == 0:
        print(computer_choice)
        print('ITS A DRAW!')
    elif computer_rps == 1:
        print(computer_choice)
        print('PC wins')
    else:
        print(computer_choice)
        print('You win')
elif user_choice == 1:
    print(rps[1])
    if computer_rps == 0:
        print(computer_choice)
        print('You win')
    elif computer_rps == 1:
        print(computer_choice)
        print('ITS A DRAW!')
    else:
        print(computer_choice)
        print('PC wins')
elif user_choice == 2:
    print(rps[2])
    if computer_rps == 0:
        print(computer_choice)
        print('PC wins')
    elif computer_rps == 1:
        print(computer_choice)
        print('You win')
    else:
        print(computer_choice)
        print('ITS A DRAW!')
else:
    print('Hmm, that\s not right')
