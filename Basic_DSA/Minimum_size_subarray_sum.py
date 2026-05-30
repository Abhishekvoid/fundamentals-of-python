from typing import List
class Solution:
    
    def minSubArrayLen(self,target: int, num: List[int]) -> int:
        
        left = 0
        current_sum = 0
        ans = len(num) + 1
        
        for right, value in enumerate(num):
            
            current_sum += value
            
            while current_sum >= target:
                ans = min(ans, right - left +1)
                current_len -= num[left]
                left += 1
                
                
        return 0 if ans == len(num)+2 else ans