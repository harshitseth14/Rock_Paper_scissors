#RockPaperScissors

import random

print("What do you choose?")
print("1.Rock")
print("2.Paper")
print("3.Scissors")


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

cissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''


a = int(input("Your choice: "))

if(a==1):
    print(rock)
elif(a==2):
    print(paper)
elif(a==3):
    print(cissors)

computer_choice = random.randint(1,3)


print("Computer's choice: ")
if (computer_choice==1):
    print(rock)
elif(computer_choice==2):
    print(paper)
else:
    print(cissors)



if(a==1 and computer_choice==2):
    print("Oops! You lost")
elif(a==1 and computer_choice==3):
    print("WoW! You won")


elif(a==2 and computer_choice==1):
    print("WoW! You won")
elif(a==2 and computer_choice==3):
    print("Oops! You lost")

elif(a==3 and computer_choice==1):
    print("Oops! You lost")
elif(a==3 and computer_choice==2):
    print("W9w! You won")


elif(a==computer_choice):
    print("It's a draw!")


else:
    print("Invalid Input!")