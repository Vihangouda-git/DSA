class Solution(object):
    def compress(self, chars):
        """
        :type chars: List[str]
        :rtype: int
        """
        s = ''
        c = 0

        for i in range(len(chars)):
            if i == 0:
                s += chars[0]
                c = 1

            else:
                if chars[i] == chars[i - 1]:
                    c += 1

                else:
                    if c > 1:
                        s += str(c)

                    s += chars[i]
                    c = 1

        # Add the count of the last group
        if c > 1:
            s += str(c)

        # Put the compressed result back into chars
        for i in range(len(s)):
            chars[i] = s[i]

        return len(s)