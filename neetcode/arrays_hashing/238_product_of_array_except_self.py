# https://leetcode.com/problems/product-of-array-except-self/

from typing import List

#! Solution1 brute force -> execution time out!!!

class Solution1:
    def multiply_elements(self, nums: List[int]) -> int:
        if len(nums) <= 0:
            return 0
        res = nums[0]
        for n in nums[1:]:
            res *= n
        return res

    def productExceptSelf(self, nums: List[int]) -> List[int]:
        ans = []
        for i, n in enumerate(nums):
            nums_copy = [*nums]
            nums_copy.pop(i)
            ans.append(self.multiply_elements(nums_copy))
        return ans

#? Solution 2 works but there is additional pass of the 'nums' list to count the zeros

class Solution2:

    def get_full_product(self, nums:List[int]) -> int:
        full_product = nums[0]
        for n in nums[1:]:
            full_product *= n
        return full_product

    def productExceptSelf(self, nums: List[int]) -> List[int]:
        zeros = nums.count(0)
        if zeros > 1: # len size always > 2
            return [0] * len(nums)

        if zeros == 1:
            pos_zero = nums.index(0)
            res = [0] * len(nums)
            nums.pop(pos_zero)
            full_product = self.get_full_product(nums)
            res[pos_zero] = full_product
            return res

        full_product = self.get_full_product(nums)
        res = [full_product]*len(nums)
        for i, val in enumerate(nums):
            res[i] //= val
        return res

#? Solution 3 is theorecatlly the fastest, but how python for loop works, it is pretty much scored the same as Solution 2 on avg
#! trick is pass twice the array from opposite direction, accumulating the product of prefix/postfix values

class Solution3:

    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = [1] * (len(nums))

        prefix = 1
        for i in range(len(nums)):
            res[i] = prefix
            prefix *= nums[i]
        postfix = 1
        for i in range(len(nums) - 1, -1, -1):
            res[i] *= postfix
            postfix *= nums[i]
        return res
