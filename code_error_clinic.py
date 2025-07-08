# Code Snippet 1: runtime error (ZeroDivisionError)
x = 10
y = 2
result = x / y
print("Result:", result)

# Code Snippet 2: runtime error (IndexError)
numbers = [1, 2, 3, 4, 5]
for i in range(len(numbers)):
    print(numbers[i])  # fixed to avoid index out of range

# Code Snippet 3: syntax error (missing colon)
def calculate_area(radius):
    area = 3.14 * radius ** 2
    return area
radius = 5
print(calculate_area(radius))

# Code Snippet 4: syntax error (missing colons)
def is_even(number):
    if number % 2 == 0:
        return True
    else:
        return False

print(is_even(4))
print(is_even(7))

# Code Snippet 5: syntax error (missing colon)
for i in range(5):
    print(i)

# Code Snippet 6: syntax error (invalid string concatenation)
def greet(name):
    return "Hello, " + name
print(greet("Alice"))

# Code Snippet 7: syntax error (indentation)
numbers = [1, 2, 3, 4, 5]
sum_numbers = 0
for number in numbers:
    sum_numbers += number
print("Sum of numbers:", sum_numbers)

# Code Snippet 8: no error (correct logic)
def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)
print(factorial(5))

# Code Snippet 9: logical error (condition always true)
name = input("Enter your name: ")
if name == "Alice" or name == "Bob" or name == "bob" or name == "alice":
    print("Hello, " + name)
else:
    print("Hello, stranger!")

# Code Snippet 10: runtime error (ZeroDivisionError)
def divide_numbers(x, y):
    if y == 0:
        return "Cannot divide by zero."
    result = x / y
    return result
num1 = 10
num2 = 0
print(divide_numbers(num1, num2))
