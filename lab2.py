# Lab 2: Python Profiles

## step 1
name = "Jasir Muhammad"
name_lowercase = "jasir muhammad"
name_halfuppercase = "Jasir muhammad"
name_halflowercase = "jasir Muhammad"
first_name = "Jasir"Add commentMore actions
last_name = "Muhammad"

## step 2
nickname = "Sire"
nickname_lowercase = "sire"
## step 3
age = 14

## step 4
used_python = True

## step 5
Hobbies = ["gaming", "reading", "coding", "sports", "exercise"]

## step 6
favorite_thing = {"I love money", "I love food", "I love games", "I love books"}

## Variable Tester
input_name = input("Enter name here:")
if input_name == name or  input_name == name_lowercase or input_name == name_halfuppercase or input_name == name_halflowercase:
    print("Welcome to the lab, " + first_name + "!")Add commentMore actions
    input_nickname = input("Enter correct nickname here:")
    if input_nickname == nickname or input_nickname == nickname_lowercase:
        print("Nickname confirmed.")
        input_age = input("Enter user's age for passage:")
        if input_age == str(age):
            print("Age confirmed.")
            input_password = input("Tell me the password: ")
            if input_password == "password123":
                print("Access granted.")
                print(favorite_thing)
            else:
                print("Incorrect password. Access denied.")
        else:
            print("Age does not match. Access denied.")
    else:
        print("Nickname does not match. Access denied.")
else:
    print("Access denied. You are not " + name + ".")