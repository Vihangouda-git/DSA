class Solution(object):
    def search(self, nums, target):
        l = 0
        r = len(nums) - 1

        while l <= r:
            i = (l + r) // 2

            if nums[i] == target:
                return i
            elif nums[i] < target:
                l = i + 1
            else:
                r = i - 1

        return -1