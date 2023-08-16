# https://leetcode.com/problems/time-based-key-value-store/

from collections import defaultdict

#! failed test cases
class TimeMap1:

    def __init__(self):
        self.store = defaultdict(dict)


    def set(self, key: str, value: str, timestamp: int) -> None:
        self.store[key][timestamp] = value


    def get(self, key: str, timestamp: int) -> str:
        timestamps = self.store.get(key,{})

        if not timestamps:
            return ''

        value = timestamps.get(timestamp)
        if value:
            return value

        return self.get_prev_timestamp(timestamps, timestamp)

    def get_prev_timestamp(self, timestamps: dict[int], target: int):
        timestamps_sorted = sorted(list(timestamps.keys()))

        l,r = 0, len(timestamps_sorted) - 1
        i = (l + r) // 2
        while l <= r:
            i = (l + r) // 2
            if timestamps_sorted[i] > target:
                r -= 1
            else: # it is not gonna be equal
                l += 1
        prev_timestamp = timestamps_sorted[i]
        return timestamps.get(prev_timestamp)


class TimeMap2:

    def __init__(self):
        self.store = defaultdict(list)


    def set(self, key: str, value: str, timestamp: int) -> None:
        self.store[key].append([value, timestamp])


    def get(self, key: str, timestamp: int) -> str:
        result = ""
        valuePairs =  self.store.get(key, [])

        l , r = 0, len(valuePairs) - 1
        while l<=r:
            i = (l+r) // 2
            if valuePairs[i][1] <= timestamp:
                result = valuePairs[i][0]
                l = i + 1
            else:
                r = i -1
        return result