class Solution(object):
    def maxDepth(self, s):
        """
        :type s: str
        :rtype: int
        """
        a=0
        b=0
        for i in s:
            if i=="(":
                a+=1
                b=max(a,b)
            elif i==")":
                a-=1
        return b