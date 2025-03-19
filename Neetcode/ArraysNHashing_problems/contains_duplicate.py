"""
! This is a test of ! feature
? What is this doing ?
todo: something
//  something
* somthing
"""

def hasDuplicate(nums: list[str]) -> bool:

    num_set = set(nums)

    return len(num_set) == len(nums)


print(hasDuplicate([1, 2, 3, 3]))
print(hasDuplicate([1, 2, 3, 4]))

