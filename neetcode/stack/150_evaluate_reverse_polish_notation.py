# https://leetcode.com/problems/evaluate-reverse-polish-notation/

#* excellent code
class Solution:
    def evalRPN(self, tokens: list[str]) -> int:
        operations = {
            '+': lambda b,a: a+b,
            '-': lambda b,a: a-b,
            '*': lambda b,a: a*b,
            '/': lambda b,a: int(a/b)
        }

        nums = []
        for token in tokens:
            if token not in operations:
                nums.append(int(token))
                continue

            ans = operations[token](nums.pop(), nums.pop())
            nums.append(ans)

        return nums[0]
