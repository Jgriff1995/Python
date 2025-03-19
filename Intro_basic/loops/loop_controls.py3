# ------------------------------------------------------------------------------------
# Loop Control: Break
# The `break` statement is used to immediately terminate a loop when a specific condition
# is met. This is useful for stopping iteration early, especially when searching for a
# value in a large list.
# ------------------------------------------------------------------------------------

# ------------------------------------------------------------------------------------
# Example: Searching for an Item in a List
# Let’s search for the item "knit dress" in a list of items on sale. Once the item is
# found, we’ll stop the loop using `break`.
# ------------------------------------------------------------------------------------

items_on_sale = ["blue shirt", "striped socks",
                 "knit dress", "red headband", "dinosaur onesie"]

print("Checking the sale list!")

# For loop to search for "knit dress"
for item in items_on_sale:
    print(item)
    if item == "knit dress":
        print("Found it!")
        break  # Exit the loop immediately

print("End of search!")

# Output:
# Checking the sale list!
# blue shirt
# striped socks
# knit dress
# Found it!
# End of search!

# ------------------------------------------------------------------------------------
# Breaking Down the Example
# - The loop iterates through each item in `items_on_sale`.
# - When the item "knit dress" is found, the `break` statement is executed.
# - The loop terminates immediately, skipping the remaining items.
# ------------------------------------------------------------------------------------

# ------------------------------------------------------------------------------------
# Why Use `break`?
# - Efficiency: Stops the loop as soon as the desired condition is met, saving time and
#   resources, especially with large datasets.
# - Simplicity: Avoids unnecessary iterations once the goal is achieved.
# ------------------------------------------------------------------------------------

# ------------------------------------------------------------------------------------
# Practice Exercise
# Use a `while` loop to search for the number 7 in the following list. Once found, print
# "Found 7!" and stop the loop.
# numbers = [1, 3, 5, 7, 9, 11, 13]
# ------------------------------------------------------------------------------------

# Example Solution
numbers = [1, 3, 5, 7, 9, 11, 13]

# Initialize an index variable
index = 0

print("\nSearching for the number 7:")
while index < len(numbers):
    print("Checking:", numbers[index])
    if numbers[index] == 7:
        print("Found 7!")
        break  # Exit the loop immediately
    index += 1  # Move to the next number

# Output:
# Searching for the number 7:
# Checking: 1
# Checking: 3
# Checking: 5
# Checking: 7
# Found 7!

# ------------------------------------------------------------------------------------
# Key Takeaways
# - The `break` statement immediately terminates a loop when executed.
# - It is useful for stopping iteration early, especially in search scenarios.
# - `break` can be used in both `for` loops and `while` loops.
# ------------------------------------------------------------------------------------

# ------------------------------------------------------------------------------------
# Loop Control: Continue
# The `continue` statement is used to skip the current iteration of a loop and move to the
# next iteration. This is useful when you want to ignore certain elements or conditions
# without terminating the loop entirely.
# ------------------------------------------------------------------------------------

# ------------------------------------------------------------------------------------
# Example: Skipping Negative Numbers
# Let’s use a `continue` statement to print only the positive numbers from a list.
# ------------------------------------------------------------------------------------

big_number_list = [1, 2, -1, 4, -5, 5, 2, -9]

print("\nPrinting Only Positive Numbers:")
for i in big_number_list:
    if i <= 0:
        continue  # Skip the current iteration if the number is not positive
    print(i)

# Output:
# 1
# 2
# 4
# 5
# 2

# ------------------------------------------------------------------------------------
# Breaking Down the Example
# - The loop iterates through each number in `big_number_list`.
# - If the number is less than or equal to 0, the `continue` statement is executed.
# - The `continue` statement skips the rest of the loop body for the current iteration.
# - Only positive numbers are printed.
# ------------------------------------------------------------------------------------

# ------------------------------------------------------------------------------------
# Why Use `continue`?
# - Selective Iteration: Allows you to skip specific elements or conditions without
#   terminating the loop.
# - Cleaner Code: Avoids deeply nested `if` statements by handling exceptions early.
# ------------------------------------------------------------------------------------

# ------------------------------------------------------------------------------------
# Practice Exercise
# Use a `for` loop to iterate through the following list of words. Print only the words
# that start with the letter "s".
# words = ["apple", "banana", "strawberry", "kiwi", "mango", "starfruit"]
# ------------------------------------------------------------------------------------

# Example Solution
words = ["apple", "banana", "strawberry", "kiwi", "mango", "starfruit"]

print("\nPrinting Words That Start with 's':")
for word in words:
    if not word.startswith("s"):
        continue  # Skip the current iteration if the word doesn't start with "s"
    print(word)

# Output:
# strawberry
# starfruit

# ------------------------------------------------------------------------------------
# Key Takeaways
# - The `continue` statement skips the current iteration and moves to the next one.
# - It is useful for filtering out unwanted elements or conditions.
# - `continue` can be used in both `for` loops and `while` loops.
# ------------------------------------------------------------------------------------

# ------------------------------------------------------------------------------------
# Nested Loops
# Nested loops are loops inside other loops. They are useful for iterating through
# multi-dimensional data structures, such as lists of lists.
# ------------------------------------------------------------------------------------

# ------------------------------------------------------------------------------------
# Example: Printing Students in Project Teams
# Let’s use nested loops to print each student in a list of project teams.
# ------------------------------------------------------------------------------------

project_teams = [["Ava", "Samantha", "James"],
                 ["Lucille", "Zed"], ["Edgar", "Gabriel"]]

print("\nPrinting Each Team:")
for team in project_teams:
    print(team)

# Output:
# ['Ava', 'Samantha', 'James']
# ['Lucille', 'Zed']
# ['Edgar', 'Gabriel']

print("\nPrinting Each Student:")
# Outer loop: Iterate through each team
for team in project_teams:
    # Inner loop: Iterate through each student in the current team
    for student in team:
        print(student)

# Output:
# Ava
# Samantha
# James
# Lucille
# Zed
# Edgar
# Gabriel

# ------------------------------------------------------------------------------------
# Breaking Down the Example
# - The outer loop iterates through each team in `project_teams`.
# - The inner loop iterates through each student in the current team.
# - This allows us to access and print each individual student.
# ------------------------------------------------------------------------------------

# ------------------------------------------------------------------------------------
# Why Use Nested Loops?
# - Multi-dimensional Data: Useful for working with lists of lists, matrices, or other
#   nested data structures.
# - Complex Iteration: Allows you to perform operations on each element within nested
#   collections.
# ------------------------------------------------------------------------------------

# ------------------------------------------------------------------------------------
# Practice Exercise
# Use nested loops to print each number in the following list of lists:
# number_grid = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
# ------------------------------------------------------------------------------------

# Example Solution
number_grid = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

print("\nPrinting Each Number in the Grid:")
# Outer loop: Iterate through each row
for row in number_grid:
    # Inner loop: Iterate through each number in the current row
    for number in row:
        print(number)

# Output:
# 1
# 2
# 3
# 4
# 5
# 6
# 7
# 8
# 9

# ------------------------------------------------------------------------------------
# Key Takeaways
# - Nested loops are loops inside other loops.
# - They are useful for iterating through multi-dimensional data structures.
# - The outer loop controls the higher-level iteration, while the inner loop handles
#   the lower-level iteration.
# ------------------------------------------------------------------------------------
