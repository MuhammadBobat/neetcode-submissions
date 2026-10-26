from collections import Counter
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        buckets = [[] for i in range(len(nums) + 1)]
        output = []

        counts = Counter(nums)
        for key, value in counts.items():
            buckets[value].append(key)

        for i in range(len(buckets) - 1, -1, -1):
            for num in buckets[i]:
                output.append(num)
                k -= 1

            if k == 0:
                return output