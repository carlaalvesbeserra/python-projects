# Exercise 6 - Validate User Input
# 1. username is no more than 12 characters
# 2. username must not contain spaces
# 3. username must not contain digits

username = input("Please enter your username: ")

if len(username) > 12:
    print("Your username can't be more than 12 characters.")
elif username.find(" ") != -1:
    print("Your username can't have any spaces.")
elif not username.isalpha():
    print("Your username can't have any numbers.")
else:
    print(f"Welcome {username}")
