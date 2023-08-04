# https://leetcode.com/problems/daily-temperatures/

#! brute force -> timeout!!!
class Solution1:
    def dailyTemperatures(self, temperatures: list[int]) -> list[int]:

        res = []
        for i, t1 in enumerate(temperatures):
            days = 0
            for j, t2 in enumerate(temperatures[i:]):
                if t2 > t1:
                    days = j
                    break
            res.append(days)
        return res


class Solution2:
    def dailyTemperatures(self, temperatures: list[int]) -> list[int]:

        res = [0] * len(temperatures)
        stack = []  # pair: [temp, index]

        for i, t in enumerate(temperatures):
            while stack and t > stack[-1][0]:
                stackT, stackInd = stack.pop()
                res[stackInd] = i - stackInd
            stack.append((t, i))
        return res

Solution2().dailyTemperatures([73,74,75,71,69,72,76,73])