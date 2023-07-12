# https://leetcode.com/problems/valid-palindrome/description/

class Solution1:
    @staticmethod
    def isPalindrome(s: str) -> bool:
        cleaned_string = ''
        for char in s.lower():
            if char.isalnum():
                cleaned_string += char

        # return cleaned_string == cleaned_string[::-1]
        result = True
        for i in range(len(cleaned_string)):
            result = cleaned_string[i] == cleaned_string[-i -1]
            if not result:
                break

        return result

#? Both solutions have similar perfomance

class Solution2:
    def isPalindrome(self, s: str) -> bool:
        l, r = 0, len(s) - 1
        while l < r:
            while l < r and not self.alphanum(s[l]):
                l += 1
            while l < r and not self.alphanum(s[r]):
                r -= 1
            if s[l].lower() != s[r].lower():
                return False
            l += 1
            r -= 1
        return True

    # Could write own alpha-numeric function
    def alphanum(self, c):
        return (
            ord("A") <= ord(c) <= ord("Z")
            or ord("a") <= ord(c) <= ord("z")
            or ord("0") <= ord(c) <= ord("9")
        )


from unittest import TestCase

class TestSolution(TestCase):
    cases = [
        ("A man, a plan, a canal: Panama", True),
        ("race a car", False),
        (" ", True)
    ]

    def test_solution(self):
        for i, case in enumerate(self.cases):
            with self.subTest(case, i=i):
                expected = case[1]
                output = Solution1.isPalindrome(case[0])
                self.assertEqual(output, expected)
