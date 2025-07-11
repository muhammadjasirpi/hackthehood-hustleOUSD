# lab 3

# task 1: working with strings
food = 'bolognese'
print(food[:3])   # prints first three characters
print(food[-3:])  # prints last three characters
first_last = food[0] + food[-1] # combines first and last character
print(first_last)  
food_list = food.split()
print(food_list)
joined_food = ' '.join(food_list)  # joins the list back into a string
print(joined_food)

# task 2: working with lists
number_list = [1,39109212, 81, 291, -712, 12, 2]
number_list.append(100)  # adds 100 to the end of the list
print(number_list)
number_list.insert(3, 0)  # inserts 0 at the 3rd index
print(number_list)
number_list.pop()
print(number_list)  # removed the last element
number_list.remove(12)  # removes 12
print(number_list)

#task 3: working with dictionaries

books = {
    "George Orwell": "1984",
    "Jane Austen": "Pride and Prejudice",
    "J.K. Rowling": "Harry Potter and the Sorcerer's Stone",
    "F. Scott Fitzgerald": "The Great Gatsby"
} # defines the dictionary with 4 keys-values

print("Authors:", list(books.keys())) #prints all keys

print("Book Titles:", list(books.values()))# prints all values

print("Book by Jane Austen:", books.get("Jane Austen")) # get the value for a specific key

books.pop(list(books.keys())[2]) 
print(books) # removes the 3rd key-value pair

del books[list(books.keys())[0]]
print(books) #removes the 1st key-value pair