# https://leetcode.com/problems/longest-substring-without-repeating-characters/

class Solution1:
    @staticmethod
    def lengthOfLongestSubstring(s: str) -> int:
        longest = 0
        char_last_occurences = {}

        l = 0
        for r, char in enumerate(s):
            if char in char_last_occurences:
                l = max(char_last_occurences[char] + 1, l) # TODO clarify this!!!

            longest = max(longest, r - l + 1)
            char_last_occurences[char] = r

        return longest

class Solution2:

    @staticmethod
    def lengthOfLongestSubstring(s):
        dct = {}
        max_so_far = curr_max = start = 0
        for index, i in enumerate(s):
            if i in dct and dct[i] >= start:
                max_so_far = max(max_so_far, curr_max)
                curr_max = index - dct[i]
                start = dct[i] + 1
            else:
                curr_max += 1
            dct[i] = index
        return max(max_so_far, curr_max)

class Solution3:
    def lengthOfLongestSubstring(self, s: str) -> int:
        charSet = set()
        l = 0
        res = 0

        for r in range(len(s)):
            if s[r] in charSet: #? in theory, as soon it finds the first duplicate, it just needs to remove 1 element from the set
                charSet.remove(s[l])
                l += 1
            charSet.add(s[r])
            res = max(res, r - l + 1)
        return res