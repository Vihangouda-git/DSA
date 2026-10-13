class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        l=[]
        r=[]
        for i in s:
            l.append(i)
        for i in t:
            r.append(i)
        l.sort()
        r.sort()
        s=""
        t=""
        for i in l:
            s+=i
        for i in r:
            t+=i

        if s==t:
            return True
        return False