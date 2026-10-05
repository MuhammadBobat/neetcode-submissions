class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        lookup = set(nums)
        counts = [1] * len(nums)
        if len(nums) == 0:
            return 0
        for num in nums:
            count = 1
            #If predecessor is not in lookup, then it is a starting number
            if (num - 1) not in lookup:
                inc = num + 1
                while inc in lookup:
                    count += 1
                    inc += 1
                counts[nums.index(num)] = count
        
        largest = 1
        for count in counts:
            if count > largest:
                largest = count

        return largest

        
