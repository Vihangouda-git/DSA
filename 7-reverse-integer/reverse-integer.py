class Solution(object):
    def reverse(self, x):
        c = 0
        if x < 0:
            c += 1
            x *= -1
        s = str(x)
        s = s[::-1]
        x = int(s)
        if c == 1:
            x *= -1
        if x < -2147483648 or x > 2147483647:
            return 0
        return x