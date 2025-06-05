class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:

        output = [0] * len(nums)
        output[0] = nums[0]
        for x in range(1,len(nums)):
                output[x] = output[x-1] + nums[x]
        
        return output
