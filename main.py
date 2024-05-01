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


choices = [rock, paper, scissors]

userPlayer = int(input("what do you choose? type 0 for rock, 1 for paper, 2 for scissors\n"))
print("You choose: ") 
print(choices[userPlayer])

computerPlayer = random.randint(0,2)
print("Computer choose: ")
print(choices[computerPlayer])


if userPlayer >= 3 or userPlayer < 0: 
  print("You typed an invalid number, you lose!") 
elif userPlayer == 0 and computerPlayer == 2:
  print("You win!")
elif computerPlayer == 0 and userPlayer == 2:
  print("You lose")
elif computerPlayer > userPlayer:
  print("You lose")
elif userPlayer > computerPlayer:
  print("You win!")
elif computerPlayer == userPlayer:
  print("It's a draw")
