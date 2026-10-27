class Solution:
    def findMin(self, nums: List[int]) -> int:
        l = 0
        r = len(nums) - 1

        while l <= r:
            mid = (l+r) // 2
            if nums[mid] <= nums[-1]:
                # I am in the RHS
                r = mid
            else:
                l = mid + 1

            if l == mid:
                return nums[l]