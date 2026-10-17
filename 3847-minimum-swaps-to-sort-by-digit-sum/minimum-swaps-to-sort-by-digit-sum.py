class Solution(object):
    def minSwaps(self, nums):
        l = []
        for i in nums:
            s = str(i)
            c = 0
            for j in s:
                v = int(j)
                c += v
            l.append((c, i))
        a = sorted(l)
        b = [i[1] for i in a]
        d = {v: i for i, v in enumerate(nums)}
        c = 0
        for i in range(len(nums)):
            if nums[i] != b[i]:
                j = d[b[i]]
                d[nums[i]] = j
                d[b[i]] = i
                nums[i], nums[j] = nums[j], nums[i]
                c += 1
        return c