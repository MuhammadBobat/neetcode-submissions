class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        output = []
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                if nums[i] + nums[j] == target:
                    if i < j:
                        output.append(i)
                        output.append(j)
                    else:
                        output.append(j)
                        output.append(i)

                
                j = j+1
            i = i+1
        return output
        
