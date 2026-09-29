class Solution:
    def maxArea(self, heights: List[int]) -> int:
        best = 0
        l = 0
        r = len(heights) - 1

        while l < r:
            amount = min(heights[l], heights[r]) * (r-l)
            if amount > best:
                best = amount
            if heights[l] > heights[r]:
                r -= 1
            else:
                l += 1

            

        return best        