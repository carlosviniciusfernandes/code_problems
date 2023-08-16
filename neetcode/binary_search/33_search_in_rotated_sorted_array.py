# https://leetcode.com/problems/search-in-rotated-sorted-array/

class Solution1:
    def search(self, nums: list[int], target: int) -> int:
        l = 0
        r = len(nums) - 1

        #* Find the rorations
        rotations = 0
        while nums[l] > nums[r - rotations]:
            rotations += 1

        #* Check if whithin limits
        if target < nums[l - rotations] or nums[r - rotations] < target:
            return -1

        #* Readjust the pointers
        if target < nums[l]:
            l = r - rotations + 1
        else:
            r = r - rotations

        while l <= r:
            i = (l + r) // 2

            if nums[i] > target:
                r -= 1
            elif nums[i] < target:
                l += 1
            else:
                return i

        return -1

#* Faster solution compare to solution 1 as it does not cycle through to figure out the number of rotations
class Solution2:
    def search(self, nums: list[int], target: int) -> int:
        l, r = 0, len(nums) - 1

        while l <= r:
            mid = (l + r) // 2
            if target == nums[mid]:
                return mid

            # left sorted portion
            if nums[l] <= nums[mid]:
                if target > nums[mid] or target < nums[l]:
                    l = mid + 1
                else:
                    r = mid - 1
            # right sorted portion
            else:
                if target < nums[mid] or target > nums[r]:
                    r = mid - 1
                else:
                    l = mid + 1
        return -1
