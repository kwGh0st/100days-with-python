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

options = [rock, paper, scissors]

print("Welcome in the \"Rock\", \"Paper\", \"Scissors\" game! \n")
player1_choose = int(input("What do you choose? Type '1' for Rock, '2' for Paper or '3' for Scissors \n"))

player2_choose = random.randint(1, 3)

print(f"You choose: \n {options[player1_choose - 1]  }" )
print(f"Computer choose: \n {options[player2_choose - 1]  }")

player_win = "You won!"
computer_win = "You lose!"

if player1_choose == player2_choose:
    print("It's a draw!")
elif player1_choose == 1 and player2_choose == 2:
    print(computer_win)
elif player1_choose == 1 and player2_choose == 3:
    print(player_win)
elif player1_choose == 2 and player2_choose == 1:
    print(player_win)
elif player1_choose == 2 and player2_choose == 3:
    print(computer_win)
elif player1_choose == 3 and player2_choose == 1:
    print(computer_win)
elif player1_choose == 3 and player2_choose == 2:
    print(player_win)