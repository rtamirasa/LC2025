class Solution(object):
    def buildArray(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        return [nums[num] for num in nums]
        #return [nums[num] for num in nums]
    #i would solve this by first mapping each index into a new array
    #so say go through nums at that index = value in nums put the number there
