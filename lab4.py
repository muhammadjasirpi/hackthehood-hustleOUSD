print ("Step 1/Bonus") #Step 1

print("Voting Poll")
input_age = input("Please enter your age: ")
while True:    
    if input_age >= "18":
        print("Step 1 of 2 completed")
        input_citizenship = input("Are you a citizen?: ")
        if input_citizenship == "yes" or input_citizenship == "Yes":
            print("Step 2 of 2 completed")
            print("You can vote!")
            input_exitprogram = input("Would you like to exit the program?(Waring: IF YOU CHOOSE YES THEN YOU WON'T CONTINUE THROUGH THE PROGRAM): ")
            if input_exitprogram == "yes" or input_exitprogram == "Yes":
                print("Exiting the program. Thank you for participating!")
                stop()
            else:
                break
        else:
            print("You are not eligible to vote due to citizenship status.")
            break
    else:
        print("You are not eligible to vote.")
        input_age = input("Would you like to enter another age?: ")
        break
print("Thank you for participating in the voting poll!")

print("Step 2") #Step 2

numbers = [32, -12, 2, 9, -31, 0, 15, -7, 4, 8]
for number in numbers:
    if number < 0:
        print(f"{number} is negative")
    elif number > 0:
        print(f"{number} is positive")
    else:
        print(f"{number} is zero")

print ("Step 3") #Step 3

print("Minecraft Inventory")
print("There are 4 types of blocks in your invitory: coal, dirt, gravel, stone, and diamond")
print("Your job is to find the diamond block in your inventory")
inventory = ["coal", "dirt", "gravel", "stone", "diamond", "dirt", "gravel", "stone", "coal", "dirt"]
for block in inventory:
    if block == "diamond":
        print("You found a diamond!")
        break