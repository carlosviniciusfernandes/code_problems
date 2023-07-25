# https://leetcode.com/problems/longest-repeating-character-replacement/

class Solution1:
    def characterReplacement(self, s: str, k: int) -> int:
        count = {}
        res = 0

        l = 0
        maxf = 0
        for r in range(len(s)):
            count[s[r]] = 1 + count.get(s[r], 0)
            maxf = max(maxf, count[s[r]])

            while (r - l + 1) - maxf > k:
                count[s[l]] -= 1
                l += 1
            res = max(res, r - l +1)

        return res


class Solution2:
    def characterReplacement(self, s: str, k: int) -> int:
        count = {}

        l = 0
        maxf = 0
        for r in range(len(s)):
            count[s[r]] = 1 + count.get(s[r], 0)
            maxf = max(maxf, count[s[r]])

            #? using if instead while we endup increment both 'l' and 'r' on each round of the loop,
            #? keeping the maximum windows size that occured until the for loop is existed
            #? in other words, once we get a maximum window size, we slide the two pointers together,
            #? keeping the window size until the end
            if (r - l + 1) - maxf > k:
                count[s[l]] -= 1
                l += 1

        return (r - l + 1)
