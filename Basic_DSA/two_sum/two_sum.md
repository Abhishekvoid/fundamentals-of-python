# Two Sum
 
    Easy 

    Given an array of integers nums and an integer target, return the indices i and j such that nums[i] + nums[j] == target and i != j.

    You may assume that every input has exactly one pair of indices i and j that satisfy the condition.

Return the answer with the smaller index first.

Example 1:

    Input: 
    nums = [3,4,5,6], target = 7

    Output: [0,1]
    Explanation: nums[0] + nums[1] == 7, so we return [0, 1].

Example 2:

    Input: nums = [4,5,6], target = 10

    Output: [0,2]

Example 3:

    Input: nums = [5,5], target = 10

    Output: [0,1]


Constraints:

    2 <= nums.length <= 1000
    -10,000,000 <= nums[i] <= 10,000,000
    -10,000,000 <= target <= 10,000,000
    Only one valid answer exists.


# approch:

    -> nums = [3,4,5,6], target = 7

        1. we have to find the pairs so we gonna use dict.

        2. a seen = {}, dict

        3. run a loop, first index[0] -> target  - 3 = 4, is 4 in seen ? no. save 3 in seen
            i=0, num=3: need 7-3=7 → 4 in seen? No → seen[3]=0
            i=1, num=4: need 7-4=3 → 3 in seen? YES! → return [0,1]
