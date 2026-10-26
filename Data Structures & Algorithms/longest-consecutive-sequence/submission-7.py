from collections import Counter, defaultdict
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        seen = set(nums)
        output = 0
        starts = []
        for num in nums:
            if (num - 1) not in seen:
                starts.append(num)

        for i in range(len(starts)):
            res = 1
            val = starts[i]
            while (val + 1) in seen:
                val += 1
                res += 1
            
            output = max(res, output)
        
        return output