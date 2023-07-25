# https://leetcode.com/problems/minimum-window-substring/

#! Failed test cases

class Solution1:
    def minWindow(self, s: str, t: str) -> str:
        if len(t) > len(s):
            return ""

        substring_set = set(t)

        string_set = set(s)
        if not all([char in string_set for char in set(substring_set)]):
            return ""

        min_sub = s
        l , r =  0, len(s)

        while l < r:
            if s[r - 1] not in substring_set:
                r -= 1

            if all([char in s[l:r] for char in set(substring_set)]):
                if len(s[l:r]) < len(min_sub):
                    min_sub = s[l:r]

            l += 1

        return min_sub

class Solution2:
   def minWindow(self, s: str, t: str) -> str:
        if t == "":
            return ""

        countT, window = {}, {}
        for c in t:
            countT[c] = 1 + countT.get(c, 0)

        have, need = 0, len(countT)
        res, resLen = [-1, -1], float("infinity")
        l = 0
        for r in range(len(s)):
            c = s[r]
            window[c] = 1 + window.get(c, 0)

            if c in countT and window[c] == countT[c]:
                have += 1

            while have == need:
                # update our result
                if (r - l + 1) < resLen:
                    res = [l, r]
                    resLen = r - l + 1
                # pop from the left of our window
                window[s[l]] -= 1
                if s[l] in countT and window[s[l]] < countT[s[l]]:
                    have -= 1
                l += 1
        l, r = res
        return s[l : r + 1] if resLen != float("infinity") else ""