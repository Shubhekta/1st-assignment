# 8. Task: Validating Email Domain 
# ● Objective: You will implement a javascript program to validate the domain of a 
# user's email address. The program will check if the email contains a specific 
# domain (e.g. "gmail.com"). 
# Problem Statement: 
# You are building a registration system that only accepts email addresses from a certain 
# domain (e.g. "gmail.com"). Your task is to: 
# 1. Prompt the user to enter their email address. 
# 2. Check if the entered email address contains the domain "gmail.com". 
# 3. Display whether the email is eligible for registration based on the domain 
# check. 
# 4. Print a message to inform the user if their email is eligible for registration 
# or not.

# 8. Task: Validating Email Domain 
 
email = input("Enter Your Email: ")
#Check if the entered email address contains the domain "gmail.com". 
domain = "gmail.com"

if domain in email:
    print("Yor Are Eligible for Registration")
else:
    print("Email is Not Eligible for Registration")
    
