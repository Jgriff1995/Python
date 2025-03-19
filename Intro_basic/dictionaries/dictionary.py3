# Python Dictionary Reference Guide
# This file serves as a comprehensive reference for working with Python dictionaries.
# It includes examples, explanations, and well-formatted output for clarity.

# =============================================
# 1. Accessing and Writing Data in a Dictionary
# =============================================

# A dictionary is a collection of key-value pairs.
# Values can be accessed or modified using their corresponding keys.

# Example Dictionary
my_dictionary = {"song": "Estranged", "artist": "Guns N' Roses"}

# Accessing a value using a key
print("Accessing a value in a dictionary:")
print(f"Song: {my_dictionary['song']}")  # Output: Estranged
print()

# Modifying a value using a key
print("Modifying a value in a dictionary:")
my_dictionary["song"] = "Paradise City"
# Output: {'song': 'Paradise City', 'artist': 'Guns N' Roses'}
print(f"Updated dictionary: {my_dictionary}")
print()

# Note: If you try to access a key that doesn't exist, Python will raise a KeyError.
# To avoid this, you can use the .get() method, which returns None (or a default value) if the key is not found.

# =============================================
# 2. Dictionary Value Types
# =============================================

# Python dictionaries can store values of any data type, including strings, integers, lists,
# other dictionaries, booleans, etc. However, keys must be immutable (e.g., strings, numbers, tuples).

# Example Dictionary with Mixed Value Types
mixed_dict = {
    1: 'hello',
    'two': True,
    '3': [1, 2, 3],
    'Four': {'fun': 'addition'},
    5.0: 5.5
}

# Accessing different types of values
print("Accessing values of different types in a dictionary:")
print(f"Key 1: {mixed_dict[1]}")          # Output: hello
print(f"Key 'two': {mixed_dict['two']}")  # Output: True
print(f"Key '3': {mixed_dict['3']}")      # Output: [1, 2, 3]
print(f"Key 'Four': {mixed_dict['Four']}")  # Output: {'fun': 'addition'}
print(f"Key 5.0: {mixed_dict[5.0]}")      # Output: 5.5
print()

# =============================================
# 3. The .pop() Method for Dictionaries
# =============================================

# The .pop() method removes a key-value pair from the dictionary and returns the value.

# Example Dictionary
famous_museums = {
    'Washington': 'Smithsonian Institution',
    'Paris': 'Le Louvre',
    'Athens': 'The Acropolis Museum'
}

# Removing a key-value pair
print("Using the .pop() method to remove a key-value pair:")
removed_value = famous_museums.pop('Athens')
print(f"Removed value: {removed_value}")  # Output: The Acropolis Museum
# Output: {'Washington': 'Smithsonian Institution', 'Paris': 'Le Louvre'}
print(f"Updated dictionary: {famous_museums}")
print()

# Note: If the key does not exist, .pop() will raise a KeyError unless a default value is provided.

# =============================================
# 4. Python Dictionaries Overview
# =============================================

# A Python dictionary is an unordered collection of items stored as key-value pairs.
# Dictionaries are mutable, meaning they can be changed after creation.

# Example Dictionary
my_dictionary = {1: "L.A. Lakers", 2: "Houston Rockets"}
print("Overview of a Python dictionary:")
# Output: {1: 'L.A. Lakers', 2: 'Houston Rockets'}
print(f"Dictionary contents: {my_dictionary}")
print()

# =============================================
# 5. Dictionary Key-Value Methods
# =============================================

# Python provides several methods to access keys, values, and key-value pairs in a dictionary.

# Example Dictionary
ex_dict = {"a": "anteater", "b": "bumblebee", "c": "cheetah"}

# .keys() - Returns a view object containing the dictionary's keys
print("Using .keys() to retrieve dictionary keys:")
print(f"Keys: {ex_dict.keys()}")  # Output: dict_keys(['a', 'b', 'c'])
print()

# .values() - Returns a view object containing the dictionary's values
print("Using .values() to retrieve dictionary values:")
# Output: dict_values(['anteater', 'bumblebee', 'cheetah'])
print(f"Values: {ex_dict.values()}")
print()

# .items() - Returns a view object containing tuples of key-value pairs
print("Using .items() to retrieve key-value pairs:")
# Output: dict_items([('a', 'anteater'), ('b', 'bumblebee'), ('c', 'cheetah')])
print(f"Items: {ex_dict.items()}")
print()

# These methods are useful for iterating over the contents of a dictionary.

# =============================================
# 6. Additional Dictionary Operations
# =============================================

# Updating a dictionary with another dictionary
print("Updating a dictionary with another dictionary:")
update_dict = {"c": "cat", "d": "dog"}
ex_dict.update(update_dict)
# Output: {'a': 'anteater', 'b': 'bumblebee', 'c': 'cat', 'd': 'dog'}
print(f"Updated dictionary: {ex_dict}")
print()

# Merging two dictionaries (Python 3.9+)
print("Merging two dictionaries using the | operator:")
dict1 = {"x": 1, "y": 2}
dict2 = {"y": 3, "z": 4}
merged_dict = dict1 | dict2
print(f"Merged dictionary: {merged_dict}")  # Output: {'x': 1, 'y': 3, 'z': 4}
print()

# Clearing all items from a dictionary
print("Clearing all items from a dictionary:")
ex_dict.clear()
print(f"Cleared dictionary: {ex_dict}")  # Output: {}
print()

# Copying a dictionary
print("Copying a dictionary:")
original_dict = {"name": "Alice", "age": 25}
copied_dict = original_dict.copy()
# Output: {'name': 'Alice', 'age': 25}
print(f"Copied dictionary: {copied_dict}")
print()

# Setting a default value for a key
print("Setting a default value for a key using .setdefault():")
default_value = ex_dict.setdefault("e", "elephant")
# Output: {'e': 'elephant'}
print(f"Dictionary after setting default: {ex_dict}")
print()

# =============================================
# 7. Additional Tips and Best Practices
# =============================================

# - Use dictionaries when you need to store data in a way that allows for fast lookups by key.
# - Dictionary keys must be unique. If you assign a value to an existing key, the old value will be overwritten.
# - Use the .get() method to safely access values without risking a KeyError.
# - Dictionaries are unordered in Python versions prior to 3.7. In Python 3.7+, dictionaries maintain insertion order.

# Example of using .get() to avoid KeyError
print("Using .get() to safely access a non-existent key:")
value = ex_dict.get("d", "Key not found")
print(f"Value for key 'd': {value}")  # Output: Key not found
print()
