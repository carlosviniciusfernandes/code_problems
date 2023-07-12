# https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/

#? uses a helper hash map like the version 1 of the problem
class Solution1:
    def twoSum(self, numbers: list[int], target: int) -> list[int]:

        diff_hash = {}
        for idx, val in enumerate(numbers):
            diff = target - val
            if diff in diff_hash:
                return [diff_hash[diff]+1, idx+1]
            diff_hash[val] = idx

#? Takes advantage that the array is sorted
class Solution2:
    def twoSum(self, numbers: list[int], target: int) -> list[int]:
        l, r = 0, len(numbers) - 1

        while l < r:
            curSum = numbers[l] + numbers[r]

            if curSum > target:
                r -= 1
            elif curSum < target:
                l += 1
            else:
                return [l + 1, r + 1]

