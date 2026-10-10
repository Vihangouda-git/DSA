class Solution(object):
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        a=len(nums)
        for i in range(0,a+1):
            if i not in nums:
                return i
        