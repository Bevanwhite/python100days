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

#Write your code below this line 👇
import random
number = int(input("what do you choose? Type 0 for Rock, 1 for paper and 2 for scissors\n"))
if(number==0):
    print(f"your choice:\n {rock}")
elif(number==1):
    print(f"your choice:\n {paper}")
elif(number==2):
    print(f"your choice:\n {scissors}")

number1 = random.choice(['rock','paper','scissors'])

if(-1>=number or number>=3): 
    print("you have entered a wrong number \ntry 0,1,2")
elif(number1 == 'rock'):
    print(f"computer choice:\n {rock}")
    if number == 0:  # 'rock'
        print("it's a draw")
    elif number == 1: # 'paper'
        print("you win")
    elif number == 2: # 'scissors'
        print("you loose")
elif(number1 == 'paper'):
    print(f"computer choice:\n {paper}")
    if number == 0:  # 'rock'
        print("you loose")
    elif number == 1: # 'paper'
        print("it's a draw")
    elif number == 2: # 'scissors'
        print("you win")
elif(number1 == 'scissors'):
    print(f"computer choice:\n {scissors}")
    if number == 0:
        print("you win")
    elif number == 1:
        print("you loose")
    elif number == 2:
        print("it's a draw")

    