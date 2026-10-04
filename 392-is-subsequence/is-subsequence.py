class Solution(object):
    def isSubsequence(self, s, t):
        s = "".join(reversed(s))
        l = list(s)

        for i in t:
            if len(l) > 0:
                a = len(l)
                if i == l[a-1]:
                    l.pop()

        if len(l) == 0:
            return True
        else:
            return False