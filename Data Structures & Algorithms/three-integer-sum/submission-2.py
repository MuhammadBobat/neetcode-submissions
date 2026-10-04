class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []
        
        for i in range(len(nums)):
            lo = i + 1
            hi = len(nums) - 1

            if i > 0 and nums[i] == nums[i - 1]:
                continue

            while lo < hi:
                if nums[i] + nums[lo] + nums[hi] < 0:
                    lo += 1
                elif nums[i] + nums[lo] + nums[hi] > 0:
                    hi -= 1
                else:
                    res.append([nums[i], nums[lo], nums[hi]])
                    lo += 1
                    hi -= 1
                    while lo < hi and nums[lo] == nums[lo - 1]:
                        lo += 1
                    while lo < hi and nums[hi] == nums[hi + 1]:
                        hi -= 1
        
        return res


