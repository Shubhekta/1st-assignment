# 3. Task: Retirement Age Calculator 
# ● Objective: Write a program that prompts the user for their age and tells them how 
# many years until they reach retirement age (65). 
# ● Hints: 
# ○ Ask the user to input their age. 
# ○ Calculate how many more years they have until they reach 65 years of 
# age. 
# ○ Display the number of years left until retirement or a message if the user 
# has already reached retirement age. 

# 3. Task: Retirement Age Calculator 
#Display the number of years left until retirement or a message if the user 
#has already reached retirement age.

retirement_age = 65
print(f"Retirement Age is: {retirement_age}")
print()

current_age = int(input("Enter the Current Age: "))
print()

if current_age < retirement_age:
   #formula for remaining years of retirement 
    left_years = retirement_age - current_age
    print(f"The Number of Years left until Retirement : {left_years}")
else:
    print("The User has Already Reached Retirement Age.")