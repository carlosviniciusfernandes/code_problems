# https://leetcode.com/problems/top-k-frequent-elements/

from typing import List
from collections import defaultdict

#! trick is bucket sort, we are looking for a given frequency ("key"), what is the list of value with that frequency

class Solution:
    @staticmethod
    def topKFrequent(nums: List[int], k: int) -> List[int]:
        count = defaultdict(int)
        freq = [[] for i in range(len(nums)+1)] #!list of lists simplifies instead of a dict of lists

        for n in nums:
            count[n] += 1

        for n, c in count.items():
            freq[c].append(n)

        res = []
        #! leverage the way 'count' keys are sorted
        for i in range(len(freq) - 1, 0, -1): #? does this work out of luck?
            res += freq[i]
            if len(res) == k:
                return res
