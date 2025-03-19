# Tuples in Python
# This script demonstrates operations on tuples, including indexing, min/max, and appending workarounds.

# ------------------------------------------------------------------------------------
# Example Tuple
# Tuples are immutable and defined using parentheses `()`.
# ------------------------------------------------------------------------------------

example_tuple = (10, 20, 30, 40, 50)
print("Example Tuple:", example_tuple)

# ------------------------------------------------------------------------------------
# Using `.index()` Method
# The `.index()` method returns the index of the first occurrence of a specified value.
# ------------------------------------------------------------------------------------

# Find the index of the value 30
index_of_30 = example_tuple.index(30)
print("\nIndex of 30:", index_of_30)  # Output: 2

# ------------------------------------------------------------------------------------
# Using `min()` and `max()` Functions
# These functions return the smallest and largest values in the tuple, respectively.
# ------------------------------------------------------------------------------------

# Find the minimum value
min_value = min(example_tuple)
print("\nMinimum value:", min_value)  # Output: 10

# Find the maximum value
max_value = max(example_tuple)
print("Maximum value:", max_value)  # Output: 50

# ------------------------------------------------------------------------------------
# Appending to Tuples (Workarounds)
# Tuples are immutable, so you cannot append directly. Use concatenation or convert to a list.
# ------------------------------------------------------------------------------------

# Attempting to append directly (will raise an error)
# example_tuple.append(40)  # AttributeError: 'tuple' object has no attribute 'append'

# Workaround 1: Concatenate tuples
new_tuple = example_tuple + (60,)
# Output: (10, 20, 30, 40, 50, 60)
print("\nNew Tuple after Concatenation:", new_tuple)

# Workaround 2: Convert to list, append, and convert back to tuple
temp_list = list(example_tuple)
temp_list.append(70)
new_tuple = tuple(temp_list)
# Output: (10, 20, 30, 40, 50, 70)
print("New Tuple after List Conversion:", new_tuple)

# ------------------------------------------------------------------------------------
# Using `.count()` Method
# The `.count()` method counts the occurrences of a specified value in the tuple.
# ------------------------------------------------------------------------------------

example_tuple = (10, 20, 30, 20, 40, 20)

# Count occurrences of 20
count_of_20 = example_tuple.count(20)
print("\nCount of 20:", count_of_20)  # Output: 3


# Immutable Nature of Tuples
# Uncommenting the following line will raise an error because tuples are immutable.
# example_tuple[0] = "New Name"  # TypeError: 'tuple' object does not support item assignment

# ------------------------------------------------------------------------------------
# Key Takeaways
# - Tuples are immutable and cannot be modified after creation.
# - Use `.index()` to find the index of a value.
# - Use `min()` and `max()` to find the smallest and largest values.
# - Use concatenation or list conversion to "append" to a tuple.
# ------------------------------------------------------------------------------------
