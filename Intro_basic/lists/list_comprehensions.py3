# ------------------------------------------------------------------------------------
# List Comprehensions: Introduction
# List comprehensions are a concise and elegant way to create lists in Python. They allow
# you to generate a new list by applying an expression to each element in an existing
# collection (like a list).
# ------------------------------------------------------------------------------------

# ------------------------------------------------------------------------------------
# Example: Doubling Numbers Using a For Loop
# Let’s start by doubling each number in a list using a traditional for loop.
# ------------------------------------------------------------------------------------

numbers = [2, -1, 79, 33, -45]
doubled = []

for number in numbers:
    doubled.append(number * 2)

print("Doubled Numbers (For Loop):", doubled)

# Output:
# Doubled Numbers (For Loop): [4, -2, 158, 66, -90]

# ------------------------------------------------------------------------------------
# Example: Doubling Numbers Using List Comprehension
# Now, let’s solve the same problem using a list comprehension.
# ------------------------------------------------------------------------------------

numbers = [2, -1, 79, 33, -45]
doubled = [num * 2 for num in numbers]

print("\nDoubled Numbers (List Comprehension):", doubled)

# Output:
# Doubled Numbers (List Comprehension): [4, -2, 158, 66, -90]

# ------------------------------------------------------------------------------------
# Breaking Down the List Comprehension
# The general structure of a list comprehension is:
#
# new_list = [<expression> for <element> in <collection>]
#
# - `<expression>`: The operation applied to each element (e.g., `num * 2`).
# - `<element>`: The variable representing each element in the collection (e.g., `num`).
# - `<collection>`: The original list or iterable (e.g., `numbers`).
# ------------------------------------------------------------------------------------

# ------------------------------------------------------------------------------------
# Why Use List Comprehensions?
# - Conciseness: Achieve the same result with less code.
# - Readability: Write cleaner and more elegant code.
# - Efficiency: Often faster than traditional loops for simple operations.
# ------------------------------------------------------------------------------------

# ------------------------------------------------------------------------------------
# Practice Exercise
# Use a list comprehension to create a new list that contains the squares of all numbers
# in the following list:
# numbers = [1, 2, 3, 4, 5]
# ------------------------------------------------------------------------------------

# Example Solution
numbers = [1, 2, 3, 4, 5]
squared = [num ** 2 for num in numbers]

print("\nSquared Numbers (List Comprehension):", squared)

# Output:
# Squared Numbers (List Comprehension): [1, 4, 9, 16, 25]

# ------------------------------------------------------------------------------------
# Key Takeaways
# - List comprehensions are a concise way to create lists.
# - They consist of an expression, a variable, and a collection.
# - They are ideal for simple transformations and filtering operations.
# ------------------------------------------------------------------------------------


# ------------------------------------------------------------------------------------
# List Comprehensions: Conditionals
# List comprehensions can incorporate conditional logic to filter or transform elements
# based on specific conditions. This makes them even more powerful and flexible.
# ------------------------------------------------------------------------------------

# ------------------------------------------------------------------------------------
# Example: Doubling Only Negative Numbers Using a For Loop
# Let’s start by doubling only the negative numbers in a list using a traditional for loop.
# ------------------------------------------------------------------------------------

numbers = [2, -1, 79, 33, -45]
only_negative_doubled = []

for num in numbers:
    if num < 0:
        only_negative_doubled.append(num * 2)

print("Doubled Negative Numbers (For Loop):", only_negative_doubled)

# Output:
# Doubled Negative Numbers (For Loop): [-2, -90]

# ------------------------------------------------------------------------------------
# Example: Doubling Only Negative Numbers Using List Comprehension
# Now, let’s solve the same problem using a list comprehension with a conditional.
# ------------------------------------------------------------------------------------

numbers = [2, -1, 79, 33, -45]
negative_doubled = [num * 2 for num in numbers if num < 0]

print("\nDoubled Negative Numbers (List Comprehension):", negative_doubled)

# Output:
# Doubled Negative Numbers (List Comprehension): [-2, -90]

# ------------------------------------------------------------------------------------
# Breaking Down the List Comprehension with Conditionals
# The general structure of a list comprehension with a conditional is:
#
# new_list = [<expression> for <element> in <collection> if <condition>]
#
# - `<expression>`: The operation applied to each element (e.g., `num * 2`).
# - `<element>`: The variable representing each element in the collection (e.g., `num`).
# - `<collection>`: The original list or iterable (e.g., `numbers`).
# - `<condition>`: A filter that determines whether the element is included (e.g., `num < 0`).
# ------------------------------------------------------------------------------------

# ------------------------------------------------------------------------------------
# Example: Using If-Else in List Comprehensions
# We can also use if-else logic directly in list comprehensions to apply different
# transformations based on a condition.
# ------------------------------------------------------------------------------------

numbers = [2, -1, 79, 33, -45]
doubled = [num * 2 if num < 0 else num * 3 for num in numbers]

print("\nDoubled Negatives and Tripled Positives (List Comprehension):", doubled)

# Output:
# Doubled Negatives and Tripled Positives (List Comprehension): [6, -2, 237, 99, -90]

# ------------------------------------------------------------------------------------
# Key Notes on Syntax
# - When using only an `if` condition (no `else`), the conditional goes after the `for` loop.
#   Example: `[num * 2 for num in numbers if num < 0]`
# - When using `if-else`, the conditional goes before the `for` loop.
#   Example: `[num * 2 if num < 0 else num * 3 for num in numbers]`
# - Incorrect placement of conditionals will result in a `SyntaxError`.
# ------------------------------------------------------------------------------------

# ------------------------------------------------------------------------------------
# Practice Exercise
# Use a list comprehension to create a new list that contains:
# - The square of each even number.
# - The cube of each odd number.
# in the following list:
# numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# ------------------------------------------------------------------------------------

# Example Solution
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
transformed = [num ** 2 if num % 2 == 0 else num ** 3 for num in numbers]

print("\nTransformed Numbers (List Comprehension):", transformed)

# Output:
# Transformed Numbers (List Comprehension): [1, 4, 27, 16, 125, 36, 343, 64, 729, 100]

# ------------------------------------------------------------------------------------
# Key Takeaways
# - List comprehensions can include conditionals to filter or transform elements.
# - Use `if` after the `for` loop for filtering.
# - Use `if-else` before the `for` loop for conditional transformations.
# - Proper syntax placement is crucial to avoid errors.
# ------------------------------------------------------------------------------------
