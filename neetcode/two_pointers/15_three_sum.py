# https://leetcode.com/problems/3sum/

#! timeout!!!
class Solution1:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        triplets = set()
        size = len(nums)
        for i in range(size -2):
            for j in range(i+1, size - 1):
                for k in range(j+1, size):
                    if nums[i] + nums[j] + nums[k] == 0:
                        ijk = sorted((nums[i], nums[j], nums[k]))
                        triplets.add(tuple(ijk))
        result = []
        for t in triplets:
            i,j,k = t
            result.append([i, j, k])
        return result


class Solution2:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        res = []
        nums.sort() #! base principle is the initial sorting, also remember O(nlog(n)) < O(n²)

        for i, a in enumerate(nums):
            # Skip positive integers - there can be two other positive numbers, but must be at least one negative
            if a > 0:
                break

            if i > 0 and a == nums[i - 1]:
                continue

            l, r = i + 1, len(nums) - 1
            while l < r:
                threeSum = a + nums[l] + nums[r]
                if threeSum > 0:
                    r -= 1
                elif threeSum < 0:
                    l += 1
                else:
                    res.append([a, nums[l], nums[r]])
                    l += 1
                    r -= 1
                    while nums[l] == nums[l - 1] and l < r:
                        l += 1

        return res