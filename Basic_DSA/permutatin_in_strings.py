from collections import Counter
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        
        
        s1_count =  Counter(s1)
        window_count = Counter()
        
        left = 0
        window_size = len(s1)
        for right, value in enumerate(s2):
            
            window_count[value] += 1
            
            if right - left + 1 > window_size:
                
                window_count[s2[left]] -= 1
                
                if window_count[s2[left]] ==0:
                    del window_count[s2[left]]
                    
                left +=1
            
            if window_count ==  s1_count:
                return True
        
        return False