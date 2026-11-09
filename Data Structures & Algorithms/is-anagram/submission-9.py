from collections import defaultdict
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        count = defaultdict(int)
        count2 = defaultdict(int)

        for char in s:
            count[char] += 1
        
        for char in t:
            count2[char] += 1
        
        if count == count2:
            return True
        
            
        return False