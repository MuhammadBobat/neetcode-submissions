from collections import defaultdict, Counter
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        #Bucket Sort - index represents quantity
        buckets = [[] for i in range(len(nums) + 1)]

        output = []

        count = Counter(nums)
        for key, value in count.items():
            buckets[value].append(key)
        
        for i in range(len(buckets)-1, -1, -1):
            if len(output) == k:
                return output
            else:
                for num in buckets[i]:
                    output.append(num)







