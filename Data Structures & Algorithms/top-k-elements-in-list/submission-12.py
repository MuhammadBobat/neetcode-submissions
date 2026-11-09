from collections import Counter
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        buckets = [[] for i in range(len(nums) + 1)]
        res = []

        # Creating a count of each num in nums
        count = Counter(nums)

        # Populating our bucket sort
        for key, value in count.items():
            buckets[value].append(key)

        # Return the top k from our bucket
        for i in range(len(buckets) - 1, -1, -1):
            for num in buckets[i]:
                if len(res) == k:
                    return res
                res.append(num)

        
        return res
        
