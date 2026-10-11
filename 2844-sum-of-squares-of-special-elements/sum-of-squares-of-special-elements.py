class Solution(object):
    def sumOfSquares(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n=len(nums)
        s=0
        for i in range(len(nums)):
            if n%(i+1)==0:
                c=nums[i]**2
                s+=c
        return s