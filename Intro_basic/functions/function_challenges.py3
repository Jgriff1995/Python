# Python Challenges Reference File
# This file contains a collection of Python challenges with well-formatted output and comments.
# Each function is preserved as-is, with no changes to the logic.

# =============================================
# Challenge 1: Tenth Power
# Function takes in a number and returns its 10th power.
# =============================================

def tenth_power(num):
    return num ** 10

# Testing the function
print("Challenge 1: Tenth Power")
print(f"1 to the 10th power is {tenth_power(1)}")  # Output: 1
print(f"0 to the 10th power is {tenth_power(0)}")  # Output: 0
print(f"2 to the 10th power is {tenth_power(2)}")  # Output: 1024
print()

# =============================================
# Challenge 2: Square Root
# Function takes in a number and returns its square root.
# =============================================

def square_root(num):
    return num ** 0.5

# Testing the function
print("Challenge 2: Square Root")
print(f"The square root of 16 is {square_root(16)}")  # Output: 4.0
print(f"The square root of 100 is {square_root(100)}")  # Output: 10.0
print()

# =============================================
# Challenge 3: Win Percentage
# Function calculates the win percentage based on wins and losses.
# =============================================

def win_percentage(wins, losses):
    return (wins / (wins + losses)) * 100

# Testing the function
print("Challenge 3: Win Percentage")
print(f"Win percentage for 5 wins and 5 losses: {win_percentage(5, 5)}%")  # Output: 50.0
print(f"Win percentage for 10 wins and 0 losses: {win_percentage(10, 0)}%")  # Output: 100.0
print()

# =============================================
# Challenge 4: Average
# Function calculates the average of two numbers.
# =============================================

def average(num1, num2):
    return (num1 + num2) / 2

# Testing the function
print("Challenge 4: Average")
print(f"The average of 1 and 100 is {average(1, 100)}")  # Output: 50.5
print(f"The average of 1 and -1 is {average(1, -1)}")  # Output: 0.0
print()

# =============================================
# Challenge 5: Remainder
# Function calculates the remainder of a specific operation.
# =============================================

def remainder(num1, num2):
    return (num1 * 2) % (num2 / 2)

# Testing the function
print("Challenge 5: Remainder")
print(f"Remainder for 15 and 14: {remainder(15, 14)}")  # Output: 2.0
print(f"Remainder for 9 and 6: {remainder(9, 6)}")  # Output: 0.0
print()

# =============================================
# Challenge 6: First Three Multiples
# Function prints the first three multiples of a number and returns the third multiple.
# =============================================

def first_three_multiples(num):
    for i in range(4):
        if i < 3:
            print(num * (i + 1))
        else:
            print(f"Returned: {num * i}")
            return num * i

# Testing the function
print("Challenge 6: First Three Multiples")
print("Testing first_three_multiples(10):")
first_three_multiples(10)  # Output: 10, 20, 30, Returned: 30
print("\nTesting first_three_multiples(5):")
first_three_multiples(5)  # Output: 5, 10, 15, Returned: 15
print()

# =============================================
# Challenge 7: Tip Calculator
# Function calculates the tip amount based on the total bill and tip percentage.
# =============================================

def tip(total, percentage):
    return (total * percentage) / 100

# Testing the function
print("Challenge 7: Tip Calculator")
print(f"Tip for a $10 bill with 25% tip: {tip(10, 25)}")  # Output: 2.5
print(f"Tip for a $0 bill with 100% tip: {tip(0, 100)}")  # Output: 0.0
print()

# =============================================
# Challenge 8: James Bond Introduction
# Function creates a James Bond-style introduction.
# =============================================

def introduction2(f, l):
    return f"{l}, {f} {l}"

# Testing the function
print("Challenge 8: James Bond Introduction")
print(introduction2("James", "Bond"))  # Output: Bond, James Bond
print(introduction2("Maya", "Angelou"))  # Output: Angelou, Maya Angelou
print()

# =============================================
# Challenge 9: Dog Years
# Function calculates a person's age in dog years.
# =============================================

def dog_years(name, age):
    return f"{name}, you are {age * 7} years old in dog years"

# Testing the function
print("Challenge 9: Dog Years")
print(dog_years("Lola", 16))  # Output: Lola, you are 112 years old in dog years
print(dog_years("Baby", 0))  # Output: Baby, you are 0 years old in dog years
print()
