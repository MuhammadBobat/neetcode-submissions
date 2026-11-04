class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # Define dictionaries for each string
        counts = {}
        for char in s:
            if char in counts:
                counts[char] += 1
            else:
                counts[char] = 1
        
        for char in t:
            if char in counts:
                counts[char] -= 1
                if counts[char] == 0:
                    del counts[char]
            else:
                return False
        
        if not counts:
            return True
        
        return False
