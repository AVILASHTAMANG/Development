# Design a time-based key-value data structure that can store multiple values for the same key at different time stamps and retrieve the key's value at a certain timestamp.
# Implement the TimeMap class:
# TimeMap() Initializes the object of the data structure.
# void set(String key, String value, int timestamp) Stores the key key with the value value at the given time timestamp.
# String get(String key, int timestamp) Returns a value such that set was called previously, with timestamp_prev <= timestamp.
# If there are multiple such values, it returns the value associated with the largest timestamp_prev. If there are no values, it returns "".

from collections import defaultdict
class TimeMap:

    def __init__(self):
        self.store = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.store[key].append((timestamp,value))

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.store:
            return ""
        arr = self.store[key]
        left, right = 0, len(arr) - 1
        ans = ""
        while left<=right:
            mid = (left+right)//2
            if arr[mid][0]==timestamp:
                return arr[mid][1]
            elif arr[mid][0]<timestamp:
                ans = arr[mid][1]
                left = mid + 1
            else:
                right = mid - 1
        return ans

if __name__=='__main__':
    operations = ["TimeMap", "set", "get", "get", "set", "get"]

    arguments = [
        [],
        ["alice", "happy", 1],
        ["alice", 1],
        ["alice", 2],
        ["alice", "sad", 3],
        ["alice", 3]
    ]
    tm = TimeMap()

    print(tm.set("alice", "happy", 1))  # None
    print(tm.get("alice", 1))  # happy
    print(tm.get("alice", 2))  # happy
    print(tm.set("alice", "sad", 3))  # None
    print(tm.get("alice", 3))  # sad