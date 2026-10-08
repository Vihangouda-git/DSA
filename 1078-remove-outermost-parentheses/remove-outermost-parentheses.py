class Solution(object):
    def removeOuterParentheses(self, s):
        a = 0
        ans = ""
        for i in s:
            if i == "(":
                if a > 0:
                    ans += i
                a += 1
            else:
                a -= 1
                if a > 0:
                    ans += i
        return ans