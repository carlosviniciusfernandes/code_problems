# https://leetcode.com/problems/sliding-window-maximum/

#! Timesout!
class Solution1:
    def maxSlidingWindow(self, nums: list[int], k: int) -> list[int]:

        max_values = []
        for i in range(len(nums) -k + 1):
            w = nums[i:i+k]
            max_values.append(max(w))
        return max_values

from collections import deque

#? Monotonically decreasing queue
class Solution2:
    def maxSlidingWindow(self, nums: list[int], k: int) -> list[int]:
        output = []
        q = deque() #index
        l = r = 0

        while r < len(nums):
            while q and nums[q[-1]] < nums[r]:
                q.pop()
            q.append(r)

            if l > q[0]:
                q.popleft()

            if (r + 1) >= k:
                output.append(nums[q[0]])
                l += 1

            r += 1

        return output