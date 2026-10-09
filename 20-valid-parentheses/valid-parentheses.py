class Solution(object):
    def isValid(self, s):
        l = []

        for i in s:
            if i == "(" or i == "[" or i == "{":
                l.append(i)

            else:
                if len(l) == 0:
                    return False

                a = l.pop()

                if i == ")" and a != "(":
                    return False
                if i == "]" and a != "[":
                    return False
                if i == "}" and a != "{":
                    return False

        return len(l) == 0