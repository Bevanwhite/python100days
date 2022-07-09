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
user_number = int(input("what do you choose? Type 0 for Rock, 1 for paper and 2 for scissors\n"))
images = [rock,paper,scissors]

computer_number = random.randint(0,2)

if(-1>=user_number or user_number>=3): 
    print("you have entered a wrong number.\n You loose\ntry 0,1,2")
else:
    print(f"your choice:\n {images[user_number]}")
    print(f"computer choice:\n {images[computer_number]}")
    if user_number == 0 and computer_number == 2:
        print("you win")
    elif user_number == 2 and computer_number == 0:
        print("you loose")
    elif user_number < computer_number:
        print("you loose")
    elif user_number > computer_number:
        print("you win")
    elif user_number == computer_number:
        print("it's a draw")
    