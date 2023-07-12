# https://leetcode.com/problems/valid-anagram/

#? NOTE Solution2 run slightly slower on due the way python runs the for loop, but both are close
#! Solution3 is basicaly cheat

class Solution1:
    def isAnagram(self, s: str, t: str) -> bool:

        if len(s) != len(t):
            return False

        hash_s = set(s)
        hash_t = set(t)

        if hash_t != hash_s:
            return False

        frequency_hash_s = {}
        frequency_hash_t = {}

        for item in hash_s:
            frequency_hash_t[item] = s.count(item)

        for item in hash_t:
            frequency_hash_s[item] = t.count(item)

        if frequency_hash_s == frequency_hash_t:
            return True

        return False


class Solution2:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        countS, countT = {}, {}

        for i in range(len(s)):
            countS[s[i]] = 1 + countS.get(s[i], 0)
            countT[t[i]] = 1 + countT.get(t[i], 0)
        return countS == countT


from collections import Counter

class Solution3:

    def isAnagram(self, s: str, t: str) -> bool:
        return Counter(s) == Counter(t)