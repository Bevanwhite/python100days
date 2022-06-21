print("Welcome to the tip calculator!")
totall_bill = float(input("What was the total bill? "))
tip_amount = float(input("How much tip would you like to give? 10, 12, or 15? "))
amountof_people = int(input("How many people to split the bill? "))

amount_with_tip = totall_bill * (100 + tip_amount)/100
per_person = amount_with_tip / amountof_people

print(f"Each person should pay: {round(per_person,2)}")