class Solution(object):
    def minInsertions(self, s):
        a = 0
        b = 0
        for i in s:
            if i == "(":
                a += 2
                if a % 2 == 1:
                    b += 1
                    a -= 1
            else:
                a -= 1
                if a < 0:
                    b += 1
                    a = 1
        return a + b