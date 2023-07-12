# https://leetcode.com/problems/two-sum/

#* Brute force would be make all combinations of 2 numbers and take the sum, but it does require a lot of runtime
#! The more perfomant solution runs the array, creating a hashmap of the differences between a given element and the target value
#! if two distinct numbers have the same diff, we found the solution

class Solution(object):

    @staticmethod
    def twoSum(nums: list[int], target: int) -> bool:

        seen = {}
        for i, val in enumerate(nums):
            x = target - val
            if x in seen:
                return [seen[x], i]
            seen[val] = i

