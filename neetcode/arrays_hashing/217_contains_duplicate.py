# https://leetcode.com/problems/contains-duplicate/

from typing import List

#? Solution 2 is slightly more perfoment as for certain cases it does not run the entire nums list

class Solution1:

    def containsDuplicate(self, nums: List[int]) -> bool:

        nums_set = set(nums)
        if len(nums_set) < len(nums):
            return True
        else:
            return False


class Solution2:

    def containsDuplicate(self, nums: List[int]) -> bool:
        hashset = set()

        for n in nums:
            if n in hashset:
                return True
            hashset.add(n)
        return False