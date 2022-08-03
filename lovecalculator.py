# 🚨 Don't change the code below 👇
print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
lower_name1 = name1.lower()
lower_name2 = name2.lower()
lower_name = lower_name1 + lower_name2

count_t = lower_name.count("t")
count_r = lower_name.count("r")
count_u = lower_name.count("u")
count_e = lower_name.count("e")

count_of_true = count_t + count_r + count_u + count_e

count_l = lower_name.count("l")
count_o = lower_name.count("o")
count_v = lower_name.count("v")
count_e = lower_name.count("e")

count_of_love = count_l + count_o + count_v + count_e

lovescore = int(str(count_of_true) + str(count_of_love))

if (lovescore < 10 or lovescore > 90):
    print(f"Your score is {lovescore}, you go together like coke and mentos")
elif(40 <= lovescore <= 50 ):
    print(f"Your score is {lovescore}, you are alright together.")
else:
    print(f"Your score is {lovescore}.")