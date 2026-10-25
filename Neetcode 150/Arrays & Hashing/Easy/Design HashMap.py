# Design a HashMap without using any built-in hash table libraries.
#
# Implement the MyHashMap class:
#
# MyHashMap() initializes the object with an empty map.
# void put(int key, int value) inserts a (key, value) pair into the HashMap. If the key already exists in the map,
# update the corresponding value.
# int get(int key) returns the value to which the specified key is mapped, or -1 if this map contains no mapping
# for the key.
# void remove(key) removes the key and its corresponding value if the map contains the mapping for the key.

class MyHashMap:

    def __init__(self):
        self.hashmap = []

    def put(self, key: int, value: int) -> None:
        for pair in self.hashmap:
            if pair[0] == key:
                pair[1] = value
                return
        self.hashmap.append([key, value])

    def get(self, key: int) -> int:
        for pair in self.hashmap:
            if pair[0] == key:
                return pair[1]
        return -1

    def remove(self, key: int) -> None:
        for i, pair in enumerate(self.hashmap):
            if pair[0] == key:
                self.hashmap.pop(i)
                return


# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)

operations = ["MyHashMap", "put", "put", "get", "get", "put", "get", "remove", "get"]
arguments = [[], [1, 1], [2, 2], [1], [3], [2, 1], [2], [2], [2]]

obj = None
output = []

for ops, args in zip(operations, arguments):
    if ops == 'MyHashMap':
        obj = MyHashMap()
        output.append(None)
    if ops == 'put':
        obj.put(*args)
        output.append(None)
    if ops == 'get':
        output.append(obj.get(*args))
    if ops == 'remove':
        obj.remove(*args)
        output.append(None)

print(output)