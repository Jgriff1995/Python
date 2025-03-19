# ------------------------------------------------------------------------------------
# For Loops: Introduction
# A for loop is a type of definite iteration. It allows you to iterate over a collection
# (like a list) and perform an action on each element.
# ------------------------------------------------------------------------------------

# ------------------------------------------------------------------------------------
# General Structure of a For Loop
# The structure of a for loop is as follows:
#
# for <temporary variable> in <collection>:
#   <action>
#
# - `for` keyword: Indicates the start of a for loop.
# - `<temporary variable>`: Represents the current element in the collection.
# - `in` keyword: Separates the temporary variable from the collection.
# - `<collection>`: The collection of elements to iterate over (e.g., a list).
# - `<action>`: The code to execute on each iteration.
# ------------------------------------------------------------------------------------

# ------------------------------------------------------------------------------------
# Example: Printing Ingredients
# Let’s use a list of ingredients to demonstrate a for loop.
# ------------------------------------------------------------------------------------

ingredients = ["milk", "sugar", "vanilla extract", "dough", "chocolate"]

# For loop to print each ingredient
print("Ingredients:")
for ingredient in ingredients:
    print(ingredient)

# Output:
# milk
# sugar
# vanilla extract
# dough
# chocolate

# ------------------------------------------------------------------------------------
# Temporary Variables
# The temporary variable's name is arbitrary and does not need to be defined beforehand.
# However, it’s best practice to use descriptive names for clarity.
# ------------------------------------------------------------------------------------

# Example 1: Using a generic temporary variable
print("\nIngredients (using 'i' as the temporary variable):")
for i in ingredients:
    print(i)

# Example 2: Using a descriptive temporary variable
print("\nIngredients (using 'item' as the temporary variable):")
for item in ingredients:
    print(item)

# ------------------------------------------------------------------------------------
# Indentation in For Loops
# Everything indented under the `for` loop declaration is part of the loop body and will
# execute on every iteration. Forgetting to indent will result in an IndentationError or
# unexpected behavior.
# ------------------------------------------------------------------------------------

# Correct indentation
print("\nIngredients with correct indentation:")
for ingredient in ingredients:
    print(ingredient)  # This is part of the loop body

# Incorrect indentation (uncomment to see the error)
# for ingredient in ingredients:
# print(ingredient)  # This will raise an IndentationError

# ------------------------------------------------------------------------------------
# One-Line For Loops
# Python allows you to write simple for loops in a single line. However, this is only
# recommended for simple actions. Complex actions should be written on multiple lines
# for readability.
# ------------------------------------------------------------------------------------

# One-line for loop
print("\nIngredients (one-line for loop):")
for ingredient in ingredients:
    print(ingredient)

# ------------------------------------------------------------------------------------
# Best Practices for For Loops
# 1. Use descriptive temporary variable names.
# 2. Ensure proper indentation for the loop body.
# 3. Avoid one-line loops for complex actions.
# ------------------------------------------------------------------------------------

# ------------------------------------------------------------------------------------
# Practice Exercise
# Create a list of your favorite fruits and use a for loop to print each fruit.
# ------------------------------------------------------------------------------------

# Example Solution
favorite_fruits = ["apple", "banana", "strawberry", "mango"]

print("\nMy Favorite Fruits:")
for fruit in favorite_fruits:
    print(fruit)

# Output:
# apple
# banana
# strawberry
# mango
