from collections import defaultdict, Counter
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = Counter(nums)
        output = []
        buckets = [[] for i in range(len(nums) + 1)]

        for key, value in count.items():
            buckets[value].append(key)
        
        for i in range(len(buckets) - 1, -1, -1):
            for element in buckets[i]:
                output.append(element)
            if len(output) == k:
                return output
        
        





