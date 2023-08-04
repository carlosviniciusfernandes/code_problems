# https://leetcode.com/problems/car-fleet/

class Solution:
    def carFleet(self, target: int, position: list[int], speed: list[int]) -> int:

        pair = [(p, s) for p, s in zip(position, speed)]
        pair.sort(reverse=True) #* sorts py reverse p -> from the closest to the target to the furthest
        stack = []
        for p, s in pair:
            time_units_to_target = (target - p) / s
            stack.append(time_units_to_target)
            if len(stack) >= 2 and stack[-1] <= stack[-2]: #! if faster then the previous (less time_units), pop from the stack
                stack.pop()
        return len(stack) #* each fleet will take a different amount of time_units to reach the target

assert 3 == Solution().carFleet(target = 12, position = [10,8,0,5,3], speed = [2,4,1,1,3])
assert 1 == Solution().carFleet(target = 10, position = [3], speed = [3])
assert 1 == Solution().carFleet(target = 100, position = [0,2,4], speed = [4,2,1])