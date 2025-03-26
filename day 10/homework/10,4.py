password = "pass123"
user_password = input("enter your password: ")

while user_password != password:
    print("Incorrect password. Try again")
    user_password = int("enter your password: ")

print("Correct password. You have successfully logged in.")