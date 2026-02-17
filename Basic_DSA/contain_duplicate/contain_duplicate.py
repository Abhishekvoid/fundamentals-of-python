"""
Contains Duplicate

    -> Given an integer array nums, return true if any value appears more than once in the array, otherwise return false.

    Example 1:

        nums = [1,2,3,3]

        output: True
    
    Example 2:

        nums = [1, 2, 3, 4]
        
        output: False

    approch:

        1. a empty seen.

        2. loop throw the array and if not seen move each int in seen and if seen return False
"""


def contains_duplicate(nums: int) -> bool:

    seen = set()

    for num in nums:

        if num in seen:
            return True
    
        seen.add(num)

    return False

print(contains_duplicate([1,2,3,4,1]))        # True
print(contains_duplicate([1,2,3,4]))          # False
print(contains_duplicate([1,1,1,3,3,4,3,2]))  # True