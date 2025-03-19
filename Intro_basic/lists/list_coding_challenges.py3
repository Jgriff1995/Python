# Python Challenges Reference File
# This file contains a collection of Python challenges with well-formatted output and comments.
# Each function is preserved as-is, with no changes to the logic.

# Coding Challenge 2: Append Sum of Last Two Elements
# This function takes a list and appends the sum of the last two elements three times to the list, then returns the modified list.
def append_sum(my_list):
    [my_list.append(my_list[-2] + my_list[-1]) for i in range(3)]
    return my_list


print("Append Sum:")
print(append_sum([1, 1, 2]))  # Output: [1, 1, 2, 3, 5, 8]
print(append_sum([2, 5]))     # Output: [2, 5, 7, 12, 19]
print()

# Coding Challenge 3: Compare List Lengths
# This function compares the lengths of two lists. If the first list is longer or equal in length, it returns the last element of the first list. Otherwise, it returns the last element of the second list.


def larger_list(my_list1, my_list2):
    if len(my_list1) >= len(my_list2):
        return my_list1[-1]
    else:
        return my_list2[-1]


print("Larger List:")
print(larger_list([4, 10, 2, 5], [-10, 2, 5, 10]))  # Output: 5
print()

# Coding Challenge 4: Check Item Frequency
# This function checks if a given item appears more than `n` times in a list. It returns `True` if the condition is met, otherwise `False`.


def more_than_n(my_list, item, n):
    if my_list.count(item) > n:
        return True
    else:
        return False


print("More Than N:")
print(more_than_n([2, 4, 6, 2, 3, 2, 1, 2], 2, 3))  # Output: True
print()

# Coding Challenge 5: Combine and Sort Lists
# This function takes two lists, combines them into one, sorts the combined list, and returns the sorted result.


def combine_sort(my_list1, my_list2):
    return sorted(my_list1 + my_list2)


print("Combine Sort:")
# Output: [-10, 2, 2, 4, 5, 5, 10, 10]
print(combine_sort([4, 10, 2, 5], [-10, 2, 5, 10]))
print()

# Coding Challenge 6: Count Numbers Divisible by 10
# This function counts how many numbers in a list are divisible by 10 and returns the count.


def divisible_by_ten(nums):
    counter = 0
    for i in nums:
        if i % 10 == 0:
            counter += 1
    return counter


def divisible_by_ten2(nums):
    return sum(1 for num in nums if num % 10 == 0)


print("Divisible by Ten:")
print(divisible_by_ten([20, 25, 30, 35, 40]))  # Output: 3
print()

# Coding Challenge 7: Add Greetings to Names
# This function takes a list of names and returns a new list with each name prefixed by "Hello, ".


def add_greetings(names):
    new_greetings = []
    for name in names:
        new_greetings.append(f"Hello, {name}")
    return new_greetings


def add_greetings2(names):
    return [f"Hello, {name}" for name in names]


print("Greetings:")
# Output: ['Hello, Owen', 'Hello, Max', 'Hello, Sophie']
print(add_greetings(["Owen", "Max", "Sophie"]))
print()

# Coding Challenge 8: Delete Starting Even Numbers
# This function removes elements from the beginning of a list if they are even, stopping at the first odd number.


def delete_starting_evens(my_list):
    while len(my_list) > 0 and my_list[0] % 2 == 0:
        my_list = my_list[1:]
        pass
    return my_list


def delete_starting_evens(my_list):
    for i in range(len(my_list)):
        if my_list[i] % 2 != 0:
            return my_list[i:]
    return []


print("Delete Starting Evens:")
print(delete_starting_evens([4, 8, 10, 11, 12, 15]))  # Output: [11, 12, 15]
print(delete_starting_evens([4, 8, 10]))             # Output: []
print()

# Coding Challenge 9: Extract Elements at Odd Indices
# This function returns a new list containing elements from the input list that are at odd indices.


def odd_indices(my_list):
    new_list = [my_list[i] for i in range(len(my_list)) if i % 2 != 0]
    return new_list


def odd_indices2(my_list):
    return [my_list[i] for i in range(1, len(my_list), 2)]


print("Odd Indices:")
print(odd_indices([4, 3, 7, 10, 11, -2]))  # Output: [3, 10, -2]
print()

# Coding Challenge 10: Calculate Exponents for Bases and Powers
# This function takes two lists, `bases` and `powers`, and returns a list of all possible base^power combinations.


def exponents(bases, powers):
    answers = []
    for base in bases:
        for power in powers:
            answers.append(base ** power)
    return answers


def exponents2(bases, powers):
    return [base ** power for base in bases for power in powers]


print("Exponents:")
# Output: [2, 4, 8, 3, 9, 27, 4, 16, 64]
print(exponents([2, 3, 4], [1, 2, 3]))
print()

# Coding Challenge 11: Return the List with the Larger Sum
# This function compares the sums of two lists and returns the list with the larger sum. If sums are equal, it returns the first list.


def larger_sum(lst1, lst2):
    sum = 0
    sum2 = 0
    for i in lst1:
        sum += i
    for i in lst2:
        sum2 += i
    if sum >= sum2:
        return lst1

    if max(sum, sum2) == sum:
        return lst1
    else:
        return lst2


def larger_sum2(lst1, lst2):
    return lst1 if sum(lst1) >= sum(lst2) else lst2


print("Larger Sum:")
print(larger_sum([1, 9, 5], [2, 3, 7]))  # Output: [1, 9, 5]
print()

# Coding Challenge 12: Sum Elements Until Total Exceeds 9000
# This function sums elements of a list until the total exceeds 9000, then returns the total.


def over_nine_thousand(lst):
    total = 0
    for num in lst:
        total += num
        if total > 9000:
            break
    return total

# Their approach more readable


def over_nine_thousand2(lst):
    sum = 0
    for number in lst:
        sum += number
        if sum > 9000:
            break
    return sum


print("Over Nine Thousand:")
print(over_nine_thousand([8000, 900, 120, 5000]))  # Output: 9020
print()

# Coding Challenge 13: Find the Maximum Number in a List
# This function returns the maximum number in a list.


def max_num(nums):
    max = nums[0]
    for num in nums:
        if num > max:
            max = num
    return max


def max_num2(nums):
    return max(nums)


print("Max Number:")
print(max_num([50, -10, 0, 75, 20]))  # Output: 75
print()

# Coding Challenge 14: Find Indices Where Values in Two Lists Are Equal
# This function returns a list of indices where the values in two input lists are equal.


def same_values(list1, list2):
    answer = []
    for i in range(len(list1)):
        if list1[i] == list2[i]:
            answer.append(i)
    return answer


def same_values2(list1, list2):
    return [i for i in range(len(list1)) if list1[i] == list2[i]]


print("Same Values:")
print(same_values([5, 1, -10, 3, 3], [5, 10, -10, 3, 5]))  # Output: [0, 2, 3]
print()

# Coding Challenge 15: Check if One List is the Reverse of the Other
# This function checks if the second list is the reverse of the first list and returns `True` or `False`.


def reversed_list(list1, list2):
    for i in range(len(list1)):
        if list1[i] != list2[len(list2) - 1 - i]:
            return False
    return True


def reversed_list2(list1, list2):
    return list1 == list2[::-1]


print("Reversed List:")
print(reversed_list([1, 2, 3], [3, 2, 1]))  # Output: True
print(reversed_list([1, 5, 3], [3, 2, 1]))  # Output: False
