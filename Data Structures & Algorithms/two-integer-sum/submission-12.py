class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        num_dict = {}
        output = []
        for i in range(len(nums)):
            difference = target - nums[i]
            if difference in num_dict:
                if i < num_dict[difference]:
                    output.append(i)
                    output.append(num_dict[difference])
                else:
                    output.append(num_dict[difference])
                    output.append(i)

                    
            num_dict[nums[i]] = i

            
        
        return output

        
