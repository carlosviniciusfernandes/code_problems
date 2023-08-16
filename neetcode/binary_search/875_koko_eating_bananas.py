# https://leetcode.com/problems/koko-eating-bananas/
from math import ceil

class Solution:
    def minEatingSpeed(self, piles: list[int], h: int) -> int:
        #! Imagine an integer array of speeds sorted from 1 to max. We are going to iterate through it using bynary search
        l = 1
        r = max(piles)
        res = r

        while l <= r:
            k = (l+r) // 2

            totalTime = 0
            for p in piles:
                totalTime += ceil(p /k)
            if totalTime <= h:
                res = min(res, k)
                r = k - 1
            else:
                l = k + 1

        return res

