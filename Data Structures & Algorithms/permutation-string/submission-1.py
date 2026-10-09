from collections import Counter, defaultdict
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        l = 0
        find = Counter(s1)
        seen = defaultdict(int)

        if len(s1) > len(s2):
            return False

        for i in range(len(s1)):
            seen[s2[i]] += 1
        if seen == find:
            return True
        
        for r in range(len(s1), len(s2)):
            seen[s2[r]] += 1
            if seen[s2[l]] > 1:
                seen[s2[l]] -= 1
            else:
                del seen[s2[l]]
            
            # now check if the dicts are the same
            if seen == find:
                return True

            l += 1
        
        return False
            