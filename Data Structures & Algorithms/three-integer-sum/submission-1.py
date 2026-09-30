class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        result = []

        for i, num in enumerate(nums):
            #Remove repeats 
            if i > 0 and nums[i-1] == num:
                continue
            
            lo = i + 1
            hi = len(nums) - 1
            while lo < hi:
                summ = num + nums[lo] + nums[hi]
                if summ == 0:
                    result.append([num, nums[hi], nums[lo]])
                    lo += 1
                    while lo < hi and nums[lo] == nums[lo-1]:
                        lo += 1

                elif summ < 0:
                    lo += 1
                else:
                    hi -= 1
            
        return result
