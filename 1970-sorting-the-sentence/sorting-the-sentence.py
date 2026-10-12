class Solution(object):
    def sortSentence(self, s):
        l = s.split()
        l1 = [""] * len(l)

        for i in l:
            c = int(i[-1])
            l1[c - 1] = i[:-1]

        return " ".join(l1)