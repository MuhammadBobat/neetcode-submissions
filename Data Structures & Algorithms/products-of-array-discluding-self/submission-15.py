class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # output = [0] * len(nums)
        # for i in range(len(nums)):
        #     prefix = 1
        #     suffix = 1
        #     total = 1
        #     for j in range(0, i):
        #         prefix *= nums[j]
        #     for k in range(i+1, len(nums)):
        #         suffix *= nums[k]
        #     total = prefix * suffix

        #     output[i] = total
        # return output

        output = [0] * len(nums)
        prefix = 1
        suffix = 1
        for i in range(len(nums)):
            output[i] = prefix
            prefix *= nums[i]
        for i in range(len(nums) -1, -1, -1):
            output[i] *= suffix
            suffix *= nums[i]

        return output
        





        


    






