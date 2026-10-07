from collections import deque

class Solution(object):
    def removeInvalidParentheses(self, s):
        q = deque([s])
        seen = set([s])
        ans = []
        done = False

        while q:
            a = q.popleft()
            b = 0
            good = True

            for c in a:
                if c == "(":
                    b += 1
                elif c == ")":
                    b -= 1

                    if b < 0:
                        good = False
                        break

            if b != 0:
                good = False

            if good:
                ans.append(a)
                done = True
            if done:
                continue
            for i in range(len(a)):
                if a[i] != "(" and a[i] != ")":
                    continue

                d = a[:i] + a[i + 1:]

                if d not in seen:
                    seen.add(d)
                    q.append(d)

        return ans
