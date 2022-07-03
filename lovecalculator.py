# 🚨 Don't change the code below 👇
print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
lower_name1 = name1.lower()
lower_name2 = name2.lower()
lower_name = lower_name1 + lower_name2

a1 = lower_name.count("t")
b1 = lower_name.count("r")
c1 = lower_name.count("u")
d1 = lower_name.count("e")

x = a1+b1+c1+d1 

a2 = lower_name.count("l")
b2 = lower_name.count("o")
c2 = lower_name.count("v")
d2 = lower_name.count("e")

y = a2+b2+c2+d2
lovescore= int(str(x) + str(y))

if (lovescore < 10 or lovescore > 90):
    print(f"Your score is {lovescore}, you go together like coke and mentos")
elif(40 <= lovescore <= 50 ):
    print(f"Your score is {lovescore}, you are alright together.")
else:
    print(f"Your score is {lovescore}.")