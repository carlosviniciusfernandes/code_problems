# https://leetcode.com/problems/permutation-in-string/

from collections import Counter, defaultdict

#! Extremely Slow
class Solution1:

    def get_char_count(self, s: str) -> dict:
        chars_count = defaultdict(int)
        for char in s:
            chars_count[char] += 1
        return chars_count

    def checkInclusion(self, s1: str, s2: str) -> bool:
        window_size = len(s1)

        s1_chars = self.get_char_count(s1)

        for l in range(len(s2)):
            r = l + window_size

            if r > len(s2):
                break

            sub = s2[l:r]
            sub_chars = self.get_char_count(sub)
            if s1_chars == sub_chars:
                return True

        return False

#! A bit slow, but good
class Solution2:

    def checkInclusion(self, s1: str, s2: str) -> bool:
        window_size = len(s1)

        if window_size > len(s2):
            return False

        s1_chars = Counter(s1)

        sub_chars = Counter(s2[0:window_size])
        if sub_chars == s1_chars:
            return True

        for i in range(len(s2) - window_size):
            sub_chars[s2[i]] -= 1
            if sub_chars[s2[i]] < 1:
                del sub_chars[s2[i]]
            sub_chars[s2[i + window_size]] += 1

            if sub_chars == s1_chars:
                return True
        return False

#! Fastest solution
class Solution3:

    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False

        #? s1 and s2 are english lower case letters, hence there 26 possible values
        count_s1 = [0] * 26
        count_s2 = [0] * 26

        def _get_index_for_letter(letter:str)-> int:
            return ord(letter) - ord('a')

        for i in range(len(s1)):
            count_s1[_get_index_for_letter(s1[i])] += 1
            count_s2[_get_index_for_letter(s2[i])] += 1

        if count_s1 == count_s2:
            return True

        window_size = len(s1)
        for i in range(len(s2) - window_size):
            count_s2[_get_index_for_letter(s2[i])] -= 1
            count_s2[_get_index_for_letter(s2[i + window_size])] += 1
            if count_s1 == count_s2:
                return True

        return False
