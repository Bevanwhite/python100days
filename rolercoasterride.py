height = int(input("what is your height? cm:"))
bill = 0
if(height>120):
    print("you can ride the roler coaster. welcome aborad")
    age = int(input("what is your age? "))
    
    if(age<12):
        print("ticket price is $5")
        bill = 5
    elif(12<age<18):
        print("ticket price is $7")
        bill = 7
    elif(age>18):
        print("ticket price is $12")
        bill = 12

    picture_taken= input("do you like to capture in the moment? Y or N :")
    if(picture_taken == "Y"):
        print("it will be $3 for the photo")
        bill += 3

    print(f"it will be all together ${bill}")
else:
    print("can't ride the rolercoaster ride come back when you are taller than  120cm ")
