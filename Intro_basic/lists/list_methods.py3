# Lists and Tuples in Python
# This script demonstrates various operations on lists and tuples, including counting, inserting, popping, slicing, sorting, and more.

# ------------------------------------------------------------------------------------
# Example List
# Lists are mutable and can store multiple items of different types.
# ------------------------------------------------------------------------------------

example_list = ["JD", "Cody", "Josh", "Your mom", "Your mom"]
print("Example List:", example_list)

# ------------------------------------------------------------------------------------
# Counting Occurrences in a List
# The `count()` method counts the number of occurrences of a specified item.
# ------------------------------------------------------------------------------------

# Count occurrences of "Your mom"
print("\nCounting Occurrences:")
print('Number of "Your mom" in example_list:',
      example_list.count("Your mom"))  # Output: 2

# ------------------------------------------------------------------------------------
# Example: Counting Votes
# A practical example of counting occurrences in a list of votes.
# ------------------------------------------------------------------------------------

votes = ["Jake", "Jake", "Laurie", "Laurie", "Laurie", "Jake", "Jake", "Jake", "Laurie", "Cassie",
         "Cassie", "Jake", "Jake", "Cassie", "Laurie", "Cassie", "Jake", "Jake", "Cassie", "Laurie"]

# Count votes for each candidate
vote_count = [["Jake", votes.count("Jake")],
              ["Laurie", votes.count("Laurie")],
              ["Cassie", votes.count("Cassie")]]

print("\nVotes List:", votes)
print("Vote Count:", vote_count)

# ------------------------------------------------------------------------------------
# Inserting Items into a List
# The `insert()` method adds an item at a specified index.
# ------------------------------------------------------------------------------------

# Insert "Your Dad" at the second-to-last position
example_list.insert(-1, "Your Dad")
# Output: ['JD', 'Cody', 'Josh', 'Your mom', 'Your Dad', 'Your mom']
print("\nAfter Inserting 'Your Dad':", example_list)

# ------------------------------------------------------------------------------------
# Removing Items from a List
# The `pop()` method removes and returns the item at the specified index.
# If no index is provided, it removes the last item.
# ------------------------------------------------------------------------------------

# Remove the last item
print("\nPopped Item:", example_list.pop())  # Output: "Your mom"
# Output: ['JD', 'Cody', 'Josh', 'Your mom', 'Your Dad']
print("List After Pop:", example_list)

# ------------------------------------------------------------------------------------
# Creating Lists with `range()`
# The `range()` function generates a sequence of numbers, which can be converted to a list.
# ------------------------------------------------------------------------------------

# Range from 0 to 10 (not inclusive)
example_list_2 = range(10)
# Output: [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
print("\nRange from 0 to 10:", list(example_list_2))

# Range from 2 to 10 (not inclusive)
example_list_3 = range(2, 10)
# Output: [2, 3, 4, 5, 6, 7, 8, 9]
print("Range from 2 to 10:", list(example_list_3))

# Range from 2 to 10, incrementing by 2
example_list_4 = range(2, 10, 2)
print("Range from 2 to 10, incrementing by 2:",
      list(example_list_4))  # Output: [2, 4, 6, 8]

# ------------------------------------------------------------------------------------
# Finding the Length of a List
# The `len()` function returns the number of items in a list.
# ------------------------------------------------------------------------------------

# Length of example_list
print("\nLength of example_list:", len(example_list))  # Output: 5

# Length of example_list_2
print("Length of example_list_2:", len(example_list_2))  # Output: 10

# ------------------------------------------------------------------------------------
# Slicing Lists
# Slicing allows you to extract a portion of a list.
# ------------------------------------------------------------------------------------

example_list_5 = ["a", "b", "c", "d", "e", "f", "g"]

# Slice from index 0 to 5 (not inclusive)
example_list_5_sliced = example_list_5[0:5]
# Output: ['a', 'b', 'c', 'd', 'e']
print("\nSliced List (0:5):", example_list_5_sliced)

# First 5 elements
# Output: ['a', 'b', 'c', 'd', 'e']
print("First 5 Elements:", example_list_5[:5])

# First 3 elements
print("First 3 Elements:", example_list_5[:3])  # Output: ['a', 'b', 'c']

# Last 2 elements
print("Last 2 Elements:", example_list_5[-2:])  # Output: ['f', 'g']

# All elements except the last one
# Output: ['a', 'b', 'c', 'd', 'e', 'f']
print("All Elements Except Last:", example_list_5[:-1])

# ------------------------------------------------------------------------------------
# Sorting Lists
# The `sort()` method sorts the list in place, while `sorted()` returns a new sorted list.
# ------------------------------------------------------------------------------------

# Sort votes alphabetically
votes.sort()
print("\nSorted Votes:", votes)

# Sort votes in reverse order
votes.sort(reverse=True)
print("Reverse-Sorted Votes:", votes)

# Create a new sorted list
names_sorted = sorted(votes)
print("Names Sorted:", names_sorted)

# ------------------------------------------------------------------------------------
# Key Takeaways
# - Lists are mutable and versatile, allowing operations like insertion, deletion, and sorting.
# - Tuples are immutable and useful for storing fixed data.
# - Both lists and tuples support operations like slicing, counting, and finding length.
# ------------------------------------------------------------------------------------
