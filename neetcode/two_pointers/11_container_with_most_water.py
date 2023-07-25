# https://leetcode.com/problems/container-with-most-water/

#* BRUTE Force solution with all possible areas, hence O(n²), timesout!!

class Solution1:
    def maxArea(self, height: list[int]) -> int:
        l = 0
        r = len(height) - 1
        h = max(height)

        ans = 0
        while l < r:
            area = min(height[l], height[r]) * (r-l)
            ans = max(ans, area)
            if height[l] < height[r]:
                l += 1
            else:
                r -= 1

            if (r-l) * h <= ans: #? makes it run faster the test cases
                break

        return ans

