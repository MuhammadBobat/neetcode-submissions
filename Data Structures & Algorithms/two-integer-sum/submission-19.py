class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        numdict = {}
        for i in range(len(nums)):
            difference = target - nums[i]

            if difference in numdict:
                if numdict[difference] < i:
                    return [numdict[difference], i]
                else:
                    return [i, numdict[difference]]
            
            numdict[nums[i]] = i
        
