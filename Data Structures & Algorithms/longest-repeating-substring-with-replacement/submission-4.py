from collections import defaultdict
class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        best = 0
        l = 0

        counts = defaultdict(int)
        for r in range(len(s)):
            counts[s[r]] += 1
            
            if ((r-l+1) - (max(counts.values()))) > k:
                counts[s[l]] -= 1
                l += 1
                if counts[s[l]] == 0:
                    del counts[s[l]]
            else:
                best = max(best, (r-l+1))
        
        return best