# https://leetcode.com/problems/longest-consecutive-sequence/

#! Solution1 by definition is not a O(n) because sort is O(nlog(n))
#! even tough it runs really fast in python

class Solution1:
    def longestConsecutive(self, nums: list[int]) -> int:
        if len(nums) == 0:
            return 0

        nums_set = [*set(nums)]
        nums_set.sort()

        current = 1
        longest = 1
        for i in range(len(nums_set)-1):
            if nums_set[i] + 1 != nums_set[i+1]:
                current = 1
            else:
                current += 1

            if current > longest:
                longest = current

        return longest

#? Altough solution 2 is technically O(n), it runs way slower in practice

class Solution2:
    def longestConsecutive(self, nums: list[int]) -> int:
        numSet = set(nums)
        longest = 0

        for n in nums:
            # check if its the start of a sequence
            if (n - 1) not in numSet:
                length = 1
                while (n + length) in numSet:
                    length += 1
                longest = max(length, longest)
        return longest

#? Variation of Solution2 but runs much fast, on par with Solution1

class Solution3:
    def longestConsecutive(self, nums: list[int]) -> int:
        nums = set(nums)
        best = 0
        for x in nums:
            if x - 1 not in nums:
                y = x + 1
                while y in nums:
                    y += 1
                best = max(best, y - x)
        return best