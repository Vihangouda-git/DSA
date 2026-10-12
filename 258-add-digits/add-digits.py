class Solution(object):
    def addDigits(self, num):
        """
        :type num: int
        :rtype: int
        """
        while (True):
            s=str(num)
            c=0
            for i in s:
                v=int(i)
                c+=v
            num=c
            if num<10:
                return num