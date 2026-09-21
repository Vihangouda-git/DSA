class Solution(object):
    def moveZeroes(self, nums):
        c = 0
        i = 0

        while i < len(nums):
            if nums[i] == 0:
                nums.pop(i)
                c += 1
            else:
                i += 1

        for i in range(c):
            nums.append(0)