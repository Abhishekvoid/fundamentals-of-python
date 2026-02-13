from typing import List

class Solution:

    def twosum(self, nums: List[int], target: int) -> List[int]:

        for i in range(len(nums)):
            for j in range(len(nums)):
                if nums[i] + nums[j] == target:
                    return nums[i, j]
            return []