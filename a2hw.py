
print("Welcome to the Student Grade Calculator!")
name = input("Enter the student's name: ")
roll_no = input("Enter the roll number: ")

print("Enter marks out of 100 for each subject:")
math = float(input("Math: "))
science = float(input("Science: "))
english = float(input("English: "))
history = float(input("History: "))
computer = float(input("Computer: "))
total = math + science + english + history + computer
percentage = (total / 500) * 100

if percentage >= 90:
    grade = "A+"
elif percentage >= 80:
    grade = "A"
elif percentage >= 70:
    grade = "B"
elif percentage >= 60:
    grade = "C"
elif percentage >= 50:
    grade = "D"
else:
    grade = "F"
if percentage >= 33:
    result = "Pass"
else:
    result = "Fail"

print("\n--- Report Card ---")
print(f"Name: {name}")
print(f"Roll Number: {roll_no}")
print(f"Total Marks: {total}/500")
print(f"Percentage: {percentage:.2f}%")
print(f"Grade: {grade}")
print(f"Result: {result}")
if grade == "A+":
    print("Excellent performance! Keep it up!")
elif grade == "A":
    print("Great job! You can aim for A+ next time.")
elif grade == "B":
    print("Good work! Try to improve further.")
elif grade == "C":
    print("Fair effort. More practice will help.")
elif grade == "D":
    print("You passed, but you should work harder.")
else:
    print("You need to study more. Don't give up!")