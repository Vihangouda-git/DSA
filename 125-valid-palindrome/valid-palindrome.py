class Solution(object):
    def isPalindrome(self, s):
        s = s.lower()
        s1 = ""

        for i in s:
            if i.isalnum():
                s1 += i

        a = s1[::-1]

        if a == s1:
            return True
        return False