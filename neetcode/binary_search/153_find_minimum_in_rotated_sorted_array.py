# https://leetcode.com/problems/find-minimum-in-rotated-sorted-array/

class Solution1:
    def findMin(self, nums: list[int]) -> int:
        l = 0
        r = len(nums) - 1

        minimum = float("inf")

        while l <= r:
            i = (l + r) // 2
            minimum = min(minimum, nums[i])

            if nums[i] > nums[r]:
                l = i + 1
            else:
                r = i - 1

        return minimum

class Solution2:
    def findMin(self, nums: list[int]) -> int:
        return min(nums) #* For python, just running the inbuilt functions will be faster then loops since the underlying implementation runs in C