
from collections import Counter
s = "pwwkew"
seen = Counter()
max_lenght = 0
left = 0

for right, char in enumerate(s):
    
    seen[char] += 1
    
    while seen[char] > 1:
        seen[s[left]] -= 1
        left += 1
        
    
    max_lenght= max(max_lenght, right - left+1)

print(max_lenght)