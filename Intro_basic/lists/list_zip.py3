# ------------------------------------------------------------------------------------
# Python's zip() Function
# The zip() function is a built-in function that allows you to combine associated data-sets
# without needing to rely on multi-dimensional lists. It pairs elements from multiple
# iterables (like lists) into tuples.
# ------------------------------------------------------------------------------------

# ------------------------------------------------------------------------------------
# Example Data Set
# Let's use a list of student names and their associated heights as our example data set.
# ------------------------------------------------------------------------------------

names = ["Jenny", "Alexus", "Sam", "Grace"]
heights = [61, 70, 67, 64]

print("Names:", names)
print("Heights:", heights)

# ------------------------------------------------------------------------------------
# Using zip() to Combine Lists
# The zip() function takes two (or more) lists as inputs and returns a zip object.
# This object contains pairs of elements, where each pair contains one element from each
# of the input lists.
# ------------------------------------------------------------------------------------

# Combine names and heights using zip()
names_and_heights = zip(names, heights)

# ------------------------------------------------------------------------------------
# Understanding the Zip Object
# The zip object is a memory-efficient iterator. It doesn't store the data directly but
# instead provides a way to access the paired elements.
# ------------------------------------------------------------------------------------

# Output: <zip object at 0x7f1631e86b48>
print("\nZip Object:", names_and_heights)

# ------------------------------------------------------------------------------------
# Converting the Zip Object to a List
# To make the zip object usable, we can convert it into a list using the list() function.
# ------------------------------------------------------------------------------------

converted_list = list(names_and_heights)
# Output: [('Jenny', 61), ('Alexus', 70), ('Sam', 67), ('Grace', 64)]
print("\nConverted List:", converted_list)

# ------------------------------------------------------------------------------------
# Observations About the Converted List
# 1. The data set is now a list of tuples.
# 2. Each tuple contains one element from each of the input lists.
# 3. Tuples are immutable, meaning their contents cannot be changed after creation.
# ------------------------------------------------------------------------------------

# ------------------------------------------------------------------------------------
# Practical Example: Using zip() with More Than Two Lists
# The zip() function can also work with more than two lists. Let's add a list of ages.
# ------------------------------------------------------------------------------------

ages = [25, 30, 28, 22]

# Combine names, heights, and ages using zip()
names_heights_ages = zip(names, heights, ages)

# Convert the zip object to a list
converted_list_2 = list(names_heights_ages)
# Output: [('Jenny', 61, 25), ('Alexus', 70, 30), ('Sam', 67, 28), ('Grace', 64, 22)]
print("\nConverted List with Ages:", converted_list_2)

# ------------------------------------------------------------------------------------
# Unzipping a Zipped List
# You can also "unzip" a zipped list back into individual lists using the zip() function
# with the * operator.
# ------------------------------------------------------------------------------------

# Unzip the converted_list back into names and heights
unzipped_names, unzipped_heights = zip(*converted_list)

# Output: ('Jenny', 'Alexus', 'Sam', 'Grace')
print("\nUnzipped Names:", unzipped_names)
print("Unzipped Heights:", unzipped_heights)  # Output: (61, 70, 67, 64)

# ------------------------------------------------------------------------------------
# Key Takeaways
# - The zip() function pairs elements from multiple iterables (like lists) into tuples.
# - The result is a zip object, which can be converted into a list for easier use.
# - zip() works with any number of iterables.
# - You can "unzip" a zipped list back into individual lists using the * operator.
# ------------------------------------------------------------------------------------

# ------------------------------------------------------------------------------------
# Practice Exercise
# 1. Create two lists: one with student grades and another with their corresponding subjects.
# 2. Use zip() to combine them into a list of tuples.
# 3. Print the result.
# ------------------------------------------------------------------------------------

# Example Solution
grades = [85, 90, 78, 92]
subjects = ["Math", "Science", "History", "English"]

# Combine grades and subjects using zip()
grades_and_subjects = zip(grades, subjects)

# Convert to a list
grades_subjects_list = list(grades_and_subjects)
# Output: [(85, 'Math'), (90, 'Science'), (78, 'History'), (92, 'English')]
print("\nGrades and Subjects:", grades_subjects_list)

# ------------------------------------------------------------------------------------
# End of File
# ------------------------------------------------------------------------------------
