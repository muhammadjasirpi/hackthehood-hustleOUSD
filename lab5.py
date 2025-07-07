def cat_greeting():
    print("Cat says meow")
cat_greeting()

def generate_superhero_power():
    user_name = input("Enter your superhero name: ")
    super_power = input("Enter your super power: ")
    message = user_name + " has the power of " + super_power + "!"
    return message
generate_superhero_power()

def cat_greeting_loop():
    greetings = ["meow", "purr", "hiss", "mew"]
    for i in greetings:
        print("Cat says", i)
cat_greeting_loop()

def generate_multiple_powers():
    powers = ["Flying", "Super Strength", "Invisibility"]
    for power in powers:
        print(power)
generate_multiple_powers()

