# ------------------------------------------------------------------------------------
# While Loops: Introduction
# A while loop is a type of indefinite iteration. It performs a set of instructions as
# long as a given condition is true.
# ------------------------------------------------------------------------------------

# ------------------------------------------------------------------------------------
# General Structure of a While Loop
# The structure of a while loop is as follows:
#
# while <conditional statement>:
#   <action>
#
# - `while` keyword: Indicates the start of a while loop.
# - `<conditional statement>`: A condition that is checked before each iteration.
# - `<action>`: The code to execute as long as the condition is true.
# ------------------------------------------------------------------------------------

# ------------------------------------------------------------------------------------
# Example: Printing Integers 0 Through 3
# Let’s use a while loop to print integers 0 through 3.
# ------------------------------------------------------------------------------------

count = 0
print("\nWhile Loop Example:")
while count <= 3:
    # Loop Body
    print(count)
    count += 1  # Increment count by 1

# Output:
# 0
# 1
# 2
# 3

# ------------------------------------------------------------------------------------
# Breaking Down the While Loop
# - `count` is initially 0. The condition `count <= 3` is true, so the loop body executes.
# - Inside the loop body, `count` is printed and then incremented by 1.
# - The loop continues until `count` becomes 4, at which point the condition is no longer true.
# ------------------------------------------------------------------------------------

# ------------------------------------------------------------------------------------
# Indentation in While Loops
# Similar to for loops, everything indented under the `while` loop declaration is part
# of the loop body and will execute on every iteration while the condition is true.
# Forgetting to indent will result in an IndentationError or unexpected behavior.
# ------------------------------------------------------------------------------------

# Correct indentation
print("\nWhile Loop with Correct Indentation:")
count = 0
while count <= 3:
    print(count)  # This is part of the loop body
    count += 1

# Incorrect indentation (uncomment to see the error)
# count = 0
# while count <= 3:
# print(count)  # This will raise an IndentationError
# count += 1

# ------------------------------------------------------------------------------------
# One-Line While Loops
# Python allows you to write simple while loops in a single line. However, this is only
# recommended for simple actions. Complex actions should be written on multiple lines
# for readability.
# ------------------------------------------------------------------------------------

# One-line while loop
print("\nOne-Line While Loop:")
count = 0
while count <= 3:
    print(count)
    count += 1  # Output: 0 1 2 3

# ------------------------------------------------------------------------------------
# Key Differences Between For and While Loops
# - For loops are used for definite iteration (when the number of iterations is known).
# - While loops are used for indefinite iteration (when the number of iterations depends
#   on a condition).
# ------------------------------------------------------------------------------------

# ------------------------------------------------------------------------------------
# Practice Exercise
# Write a while loop that prints numbers from 5 down to 1.
# ------------------------------------------------------------------------------------

# Example Solution
print("\nCountdown from 5 to 1:")
countdown = 5
while countdown >= 1:
    print(countdown)
    countdown -= 1  # Decrement countdown by 1

# Output:
# 5
# 4
# 3
# 2
# 1

# ------------------------------------------------------------------------------------
# While Loops: Lists
# While loops aren’t just for counting! They can also be used to iterate through lists,
# similar to how we use for loops. Let’s explore how to use a while loop to iterate
# through a list.
# ------------------------------------------------------------------------------------

# ------------------------------------------------------------------------------------
# Example: Iterating Through a List of Ingredients
# Let’s use a while loop to print each ingredient in our list.
# ------------------------------------------------------------------------------------

ingredients = ["milk", "sugar", "vanilla extract", "dough", "chocolate"]

# Get the length of the list
length = len(ingredients)

# Initialize an index variable
index = 0

print("\nWhile Loop with Lists:")
while index < length:
    print(ingredients[index])  # Print the current ingredient
    index += 1  # Increment the index to access the next element

# Output:
# milk
# sugar
# vanilla extract
# dough
# chocolate

# ------------------------------------------------------------------------------------
# Breaking Down the While Loop with Lists
# - `length = len(ingredients)`: Stores the length of the list (5 in this case).
# - `index = 0`: Initializes a variable to track the current position in the list.
# - `while index < length`: The loop runs as long as the index is less than the list length.
# - `print(ingredients[index])`: Prints the element at the current index.
# - `index += 1`: Increments the index to access the next element in the list.
# ------------------------------------------------------------------------------------

# ------------------------------------------------------------------------------------
# Why Use a While Loop with Lists?
# While loops are useful when you need more control over the iteration process, such as
# when the stopping condition depends on more than just the length of the list.
# ------------------------------------------------------------------------------------

# ------------------------------------------------------------------------------------
# Practice Exercise
# Use a while loop to iterate through the following list of numbers and print each number:
# numbers = [10, 20, 30, 40, 50]
# ------------------------------------------------------------------------------------

# Example Solution
numbers = [10, 20, 30, 40, 50]

# Get the length of the list
length_numbers = len(numbers)

# Initialize an index variable
index_numbers = 0

print("\nWhile Loop with Numbers:")
while index_numbers < length_numbers:
    print(numbers[index_numbers])  # Print the current number
    index_numbers += 1  # Increment the index to access the next element

# Output:
# 10
# 20
# 30
# 40
# 50

# ------------------------------------------------------------------------------------
# Key Takeaways
# - While loops can iterate through lists using an index variable.
# - The `len()` function is used to determine the length of the list.
# - The index variable is incremented on each iteration to access the next element.
# - While loops provide more flexibility for complex iteration logic.
# ------------------------------------------------------------------------------------
