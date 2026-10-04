from collections import Counter, defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groupDict = defaultdict(list)
        for s in strs:
            alpha = [0] * 26
            for char in s:
                alpha[ord(char) - ord('a')] += 1
            
            groupDict[tuple(alpha)].append(s)
        
        return list(groupDict.values())