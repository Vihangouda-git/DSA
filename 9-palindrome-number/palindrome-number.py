class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        s=str(x)
        k=s[::-1]
        if s==k:
            return True
        else:
            return False