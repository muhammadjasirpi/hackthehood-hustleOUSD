def cat_greeting():
    print ("Cat says meow")
cat_greeting

def genereate_superhero_power():
    ##print("Flying")
    user_name = input("Enter your superhero name: ")
    super_power = input("Enter your super power: ")
    print(f"{user_name} has the power of {super_power}!")
genereate_superhero_power()

def cat_greeting_loop():
    for i in range(5):
        print("Cat says meow")
cat_greeting_loop()

def generate_multiple_powers():
    powers = ["Flying, Super Strength, Invisibility"]
    for power in powers:
        print ("".join(powers))
generate_multiple_powers()

