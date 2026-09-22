class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        first = {}
        second = {}
        for char in s:
            if char in first:
                first[char] += 1
            else:
                first[char] = 1

        for char in t:
            if char in second:
                second[char] += 1
            else:
                second[char] = 1

        if first == second:
            return True

        return False
