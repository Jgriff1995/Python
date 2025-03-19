# =============================================
# Dictionary Comprehension and Operations
# =============================================

# Dictionary comprehension allows you to create dictionaries in a concise and elegant way.
# This file demonstrates dictionary comprehension and various dictionary operations.

# =============================================
# 1. Dictionary Comprehension Basics
# =============================================

# Example: Creating a dictionary from two lists using dictionary comprehension.

names = ['Jenny', 'Alexus', 'Sam', 'Grace']
heights = [61, 70, 67, 64]

# Using dictionary comprehension to pair names with heights.
students = {key: value for key, value in zip(names, heights)}
# students is now {'Jenny': 61, 'Alexus': 70, 'Sam': 67, 'Grace': 64}

# Explanation:
# 1. zip(names, heights) pairs elements from both lists into tuples.
# 2. The dictionary comprehension iterates through these tuples.
# 3. Each tuple is unpacked into key and value, creating a key-value pair in the dictionary.

# =============================================
# 2. Dictionary Comprehension with zip()
# =============================================

# Example: Creating a dictionary from two lists using zip() and dictionary comprehension.

drinks = ["espresso", "chai", "decaf", "drip"]
caffeine = [64, 40, 0, 120]

# Using zip() to pair drinks with caffeine levels.
zipped_drinks = zip(drinks, caffeine)
drinks_to_caffeine = {key: value for key, value in zipped_drinks}

# Result: {'espresso': 64, 'chai': 40, 'decaf': 0, 'drip': 120}

# =============================================
# 3. Building a Music Streaming Service
# =============================================

# Example: Creating a dictionary of songs and their play counts using dictionary comprehension.

songs = ["Like a Rolling Stone", "Satisfaction", "Imagine",
         "What's Going On", "Respect", "Good Vibrations"]
playcounts = [78, 29, 44, 21, 89, 5]

# Using dictionary comprehension to create the 'plays' dictionary.
plays = {key: value for key, value in zip(songs, playcounts)}

print("Plays Dictionary:")
print(plays)  # Output: {'Like a Rolling Stone': 78, 'Satisfaction': 29, ...}

# Adding new songs and updating play counts.
plays["Purple Haze"] = 1
plays["Respect"] = 94

# Creating a nested dictionary for a music library.
library = {"The Best Songs": plays, "Sunday Feelings": {}}

print("\nMusic Library:")
print(library)

# =============================================
# 4. Using .get() for Safe Dictionary Access
# =============================================

# Example: Using .get() to safely access dictionary values with a default fallback.

user_ids = {"teraCoder": 100019, "pythonGuy": 182921,
            "samTheJavaMaam": 123112, "lyleLoop": 102931, "keysmithKeith": 129384}

# Getting the value for an existing key.
tc_id = user_ids.get("teraCoder")
print("\nUser ID for teraCoder:", tc_id)  # Output: 100019

# Getting the value for a non-existent key with a default value.
stack_id = user_ids.get("superStackSmash", 100000)
print("User ID for superStackSmash:", stack_id)  # Output: 100000

# =============================================
# 5. Dictionary Operations in a Game Context
# =============================================

# Example: Managing a player's inventory and health points in a game.

available_items = {"health potion": 10, "cake of the cure": 5, "green elixir": 20,
                   "strength sandwich": 25, "stamina grains": 15, "power stew": 30}
health_points = 20

# Using .pop() to consume items and update health points.
health_points += available_items.pop("stamina grains", 0)
health_points += available_items.pop("power stew", 0)
health_points += available_items.pop("mystic bread", 0)

print("\nUpdated Inventory:", available_items)
print("Updated Health Points:", health_points)

# =============================================
# 6. Working with Dictionary Keys and Values
# =============================================

# Example: Extracting keys and values from dictionaries.

user_ids = {"teraCoder": 100019, "pythonGuy": 182921,
            "samTheJavaMaam": 123112, "lyleLoop": 102931, "keysmithKeith": 129384}
num_exercises = {"functions": 10, "syntax": 13, "control flow": 15,
                 "loops": 22, "lists": 19, "classes": 18, "dictionaries": 18}

# Extracting keys from dictionaries.
users = user_ids.keys()
lessons = num_exercises.keys()

print("\nUsers:", users)
print("Lessons:", lessons)

# Summing values in a dictionary.
total_exercises = sum(num_exercises.values())
print("Total Exercises:", total_exercises)

# =============================================
# 7. Iterating Over Dictionary Items
# =============================================

# Example: Iterating over key-value pairs in a dictionary.

pct_women_in_occupation = {"CEO": 28, "Engineering Manager": 9,
                           "Pharmacist": 58, "Physician": 40, "Lawyer": 37, "Aerospace Engineer": 9}

# Printing formatted strings using dictionary items.
for occupation, percentage in pct_women_in_occupation.items():
    print(f"Women make up {percentage} percent of {occupation}s.")

# =============================================
# 8. Tarot Card Spread Example
# =============================================

# Example: Simulating a tarot card reading using dictionary operations.

tarot = {1: "The Magician", 2: "The High Priestess", 3: "The Empress", 4: "The Emperor",
         5: "The Hierophant", 6: "The Lovers", 7: "The Chariot", 8: "Strength",
         9: "The Hermit", 10: "Wheel of Fortune", 11: "Justice", 12: "The Hanged Man",
         13: "Death", 14: "Temperance", 15: "The Devil", 16: "The Tower", 17: "The Star",
         18: "The Moon", 19: "The Sun", 20: "Judgement", 21: "The World", 22: "The Fool"}

# Creating a tarot card spread.
spread = {}
spread["past"] = tarot.pop(13)
spread["present"] = tarot.pop(22)
spread["future"] = tarot.pop(10)

# Displaying the tarot spread.
print("\nYour Tarot Spread:")
for key, value in spread.items():
    print(f"Your {key} is the {value} card.")
