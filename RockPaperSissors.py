import random
Rock = """
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
"""

Paper = """
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
"""
Scissors = """
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
"""
rps = [Rock,Paper,Scissors]
num = int(input("Rock Paper and Scissors game, choose 1 for Rock, 2 for Paper and 3 for Scissors :- "))
computer_number = random.randint(1,3)
if num<0 and num>3:
    print("Invalid Choice")
    quit()


print("Your Choice:- ")
print(rps[num-1])

print('\n')
print("Computer Choice :- ")
print(rps[computer_number-1])

if num == 1 and computer_number == 3:
    print("You Win")
elif num == 2 and computer_number == 1:
    print("You Win")
elif num == 3 and computer_number == 2:
    print("You Win")
elif num == computer_number:
    print("Draw")
else:
    print("You Loose")





