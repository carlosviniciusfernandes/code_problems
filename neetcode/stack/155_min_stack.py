# https://leetcode.com/problems/min-stack/

#* Worked on first try, but perfomance is very poor
class MinStack1:

    def __init__(self):
        self.stack = []

    def push(self, val: int) -> None:
        self.stack.append(val)

    def pop(self) -> None:
        if not self.stack:
            return None

        return self.stack.pop()

    def top(self) -> int:
        if not self.stack:
            return None

        return self.stack[-1]


    def getMin(self) -> int:
        if not self.stack:
            return None

        return min(self.stack)

#! Perfomance is greatly increased running the test cases if a dedicated stack is used for the min value, preventing the usage of the *min()* func
class MinStack2:
    def __init__(self):
        self.stack = []
        self.minStack = []

    def push(self, val: int) -> None:
        self.stack.append(val)
        val = min(val, self.minStack[-1] if self.minStack else val)
        self.minStack.append(val)

    def pop(self) -> None:
        self.stack.pop()
        self.minStack.pop() #! not very memory efficient

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.minStack[-1]

#* Extremelly good solution both memory and perfomance wise
class MinStack3:
    def __init__(self):
        self.stack = []
        self.stackSize = 0
        self.minIndexesStack = []

    def push(self, val: int) -> None:
        self.stack.append(val)
        self.stackSize += 1
        if not self.minIndexesStack or val < self.stack[self.minIndexesStack[-1]]:
            self.minIndexesStack.append(self.stackSize - 1)

    def pop(self) -> None:
        if self.stackSize == 0:
            return

        lastIndex = self.stackSize - 1
        if lastIndex == self.minIndexesStack[-1]:
            self.minIndexesStack.pop()

        self.stackSize -= 1
        self.stack.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        minIndex = self.minIndexesStack[-1]
        return self.stack[minIndex]
