
# Contains Duplicate

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

        