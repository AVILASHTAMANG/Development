# Design a HashSet without using any built-in hash table libraries.
#
# Implement MyHashSet class:
#
# void add(key) Inserts the value key into the HashSet.
# bool contains(key) Returns whether the value key exists in the HashSet or not.
# void remove(key) Removes the value key in the HashSet. If key does not exist in the HashSet, do nothing.

class MyHashSet:

    def __init__(self):
        self.hashset = []

    def add(self, key: int) -> None:
        if key not in self.hashset:
            self.hashset.append(key)

    def remove(self, key: int) -> None:
        if key in self.hashset:
            self.hashset.remove(key)

    def contains(self, key: int) -> bool:
       return key in self.hashset

# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)

operations = [
    "MyHashSet", "add", "add", "contains", "contains",
    "add", "contains", "remove", "contains"
]

arguments = [
    [], [1], [2], [1], [3], [2], [2], [2], [2]
]

obj = None
output = []

for operations, args in zip(operations, arguments):
    if operations == "MyHashSet":
        obj = MyHashSet()
        output.append(None)
    elif operations == "add":
        obj.add(*args)
        output.append(None)
    elif operations == "remove":
        obj.remove(*args)
        output.append(None)
    elif operations == "contains":
        output.append(obj.contains(*args))
print(output)