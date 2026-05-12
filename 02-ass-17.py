# 17.Find the greatest number. 
# ○ Task: Write a program to find greatest number from three number 
# ○ Input: Prompt the user to enter three numbers. 
# ○ Output: Display the greatest number.


first = int(input("Enter first number : "))
second = int(input("Enter second number : "))
third = int(input("Enter third number : "))
print()

if first > second and first > third:
    print(f"Greatest Number : {first}")

elif second > first and second > third:
    print(f"Greatest Number : {second}")

elif third > first and third > second:
    print(f"Greatest Number : {third}")
else:
    print("Something Went Wrong")