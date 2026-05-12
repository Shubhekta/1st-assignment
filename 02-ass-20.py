# 20.Library Charge Calculation 
# ○ Task: Write a program to calculate the library charges based on the number of 
# days a book has been borrowed. 
# ○ Charge Criteria: 
# ■ Up to 5 days: ₹2/day. 
# ■ 6 to 10 days: ₹3/day. 
# ■ 11 to 15 days: ₹4/day. 
# ■ More than 15 days: ₹5/day. 
# ○ Output: Display the total charges.

days = int(input("Enter the Number of Days a book has been borrowed : "))
print()

if days <= 5:
    lib_charge = days * 2
    print(f"The Library Charge for {days} days : {lib_charge}")

elif days >= 6 and days <= 10:
    lib_charge = days * 3
    print(f"The Library Charge for {days} days : {lib_charge} ")

elif days >= 11 and days <= 15:
    lib_charge = days * 4
    print(f"The Library Charge for {days} days : {lib_charge} ")

elif days > 15:
    lib_charge = days * 5
    print(f"The Library Charge for {days} days : {lib_charge} ")
else:
    print("Something Went Wrong")
