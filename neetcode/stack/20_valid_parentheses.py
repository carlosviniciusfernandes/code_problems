# https://leetcode.com/problems/valid-parentheses/

class Solution:
    def isValid(self, s: str) -> bool:
        brackets_map = {
            '(':')',
            '[':']',
            '{':'}'
        }

        stack = []

        for c in s:
            if not stack and c not in brackets_map:
                return False
            if c in brackets_map:
                stack.append(c)
                continue

            if brackets_map[stack[-1]] == c:
                stack.pop()
            else:
                return False

        return not stack #? True if all character are poped from the stack

