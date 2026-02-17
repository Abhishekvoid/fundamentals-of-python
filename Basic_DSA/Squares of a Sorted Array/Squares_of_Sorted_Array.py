"""
977. Squares of sorted array

Given an integer array nums sorted in non-decreasing order, return an array of the squares of each number sorted in non-decreasing order.

Example 1:

Input: nums = [-4,-1,0,3,10]
Output: [0,1,9,16,100]


Explanation: After squaring, the array becomes [16,1,0,9,100].
After sorting, it becomes [0,1,9,16,100].


Example 2:

Input: nums = [-7,-3,2,3,11]
Output: [4,9,9,49,121]


Constraints:

    1 <= nums.length <= 104
    -104 <= nums[i] <= 104
    nums is sorted in non-decreasing order.
 

Follow up: Squaring each element and sorting the new array is very trivial, could you find an O(n) solution using a different approach?


approch:

    Two pointers:

    1.
        left = 0                           1st index
        right = len(nums) - 1              2nd index

        result = [0] * len(nums)  # result will store a array 0 which is = size of nums, this will use to store your squared num
        
        idx = nums - 1 = this will start from the end and store num in result fromt the end 


    2. while left <= right, left_sq  = left * left, right_sq = right * right

    3. if left is > right:

        result[idx] = right_sq
        right += 1

        or

        otherwise

        result[idx] = left_sq
        left += 1
    
    idx -= 

return result

"""


def sorted_squares(nums: list[int]) -> list[int]:

    n = len(nums)
    left = 0
    right = n - 1

    idx = n - 1
    result = [0] * n

    while left <= right:

        left_sq = nums[left] * nums[left]
        right_sq = nums[right] * nums[right]

        if left_sq > right_sq:

            result[idx] = left_sq
            left += 1

        else:

            result[idx] = right_sq
            right -= 1
        idx -= 1
    return result
    


print(sorted_squares(nums = [-4,-1,0,3,10]))