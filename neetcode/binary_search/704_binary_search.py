# https://leetcode.com/problems/binary-search/

class Solution:
    def search(self, nums: list[int], target: int) -> int:
        l = 0
        r = len(nums) - 1

        while l <= r:
            index = (l + r) // 2 # or l + ((r+l) // 2)
            n = nums[index]
            if n < target:
                l = index + 1
            if n > target:
                r = index - 1
            if n == target:
                return index

        return -1
