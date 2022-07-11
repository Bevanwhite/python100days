# 🚨 Don't change the code below 👇
student_heights = input("Input a list of student heights ").split()
for n in range(0, len(student_heights)):
  student_heights[n] = int(student_heights[n])
# 🚨 Don't change the code above 👆

#Write your code below this row 👇
number_of_height,total_count = 0,0
for i in student_heights:
    total_count += i
    number_of_height += 1
print(f"{round(total_count/number_of_height)}")