# https://leetcode.com/problems/group-anagrams/

from collections import defaultdict
from typing import List

#! trick here is that dicts accept tuples as the hash key
#? python's defaultdict helps a lot here as it avoid having to check if the key exits, we just provide a 'list' as the default factory

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        ans = defaultdict(list) # -> python's list callable that creates and empty list

        for s in strs:
            count = [0] * 26
            for c in s:
                count[ord(c) - ord("a")] += 1
            ans[tuple(count)].append(s)
        return ans.values()
