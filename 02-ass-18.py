# 18.Authentication System 
# ○ Task: Write a program to authenticate a user by validating their username and 
# password. 
# ○ Predefined Credentials: 
# ■ Username: user1 
# ■ Password: pass@123 
# ○ Input: Prompt the user to input their username and password. 
# ○ Output: 
# ■ If the credentials match, display "Authentication successful." 
# ■ If they do not match, display "Authentication failed." 


username = "user1" 
password = "pass@123" 

user = input("Enter Your Username : ")
passwd = input("Enter Your Password : ")

if username == user and password == passwd:
    print("Authentication successful.")
else:
     print("Authentication failed.")