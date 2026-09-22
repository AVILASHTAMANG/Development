# Implement the Least Recently Used (LRU) cache class LRUCache. The class should support the following operations
#
# LRUCache(int capacity) Initialize the LRU cache of size capacity.
# int get(int key) Return the value corresponding to the key if the key exists, otherwise return -1.
# void put(int key, int value) Update the value of the key if the key exists. Otherwise, add the key-value pair to the cache. If the introduction of the new pair causes the cache to exceed its capacity, remove the least recently used key.
# A key is considered used if a get or a put operation is called on it.
#
# Ensure that get and put each run in O(1) average time complexity.

class doubleListNode:
    def __init__(self, key=None, val=0):
        self.key = key
        self.val = val
        self.next = None
        self.prev = None

#########  [head] <---> [MRU node] <---> ... <---> [LRU node] <---> [tail] #################

class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.hash_map = {} # gives lookups for cache keys by mapping every cache key directly mapping every cache key directly to the memory address (or reference) of its corresponding node in the linked list.
        self.head = doubleListNode() # It maintains the exact sequence of usage, from the most recently used item (near the front/head).
        self.tail = doubleListNode() # It maintains the exact sequence of usage, from the most recently used item (near the front/head).
        # Connecting head and tail together to represent empty list
        self.head.next = self.tail # will always point to the Most Recently Used (MRU) node.
        self.tail.prev = self.head # will always point to the Least Recently Used (LRU) node.

    # Helper 1: Cuts a node out of its current position in the linked list
    def _remove(self, node):
        prev_node = node.prev
        next_node = node.next
        prev_node.next  = next_node
        next_node.prev = prev_node

    # Helper 2: Inserts a node right at the front (right after self.head)
    def _add_to_front(self, node):
        node.prev = self.head
        node.next = self.head.next
        self.head.next.prev = node
        self.head.next = node

    def get(self, key: int) -> int:
        if key in self.hash_map:
            node = self.hash_map[key]
            # 1. Remove it from it's current spot
            self._remove(node)
            # 2. Move it to the front to mark it as most recently used
            self._add_to_front(node)
            # 3. Return it's value
            return node.val
        return -1

    def put(self, key: int, value: int) -> None:
        if key in self.hash_map:
            # 1. If it exists, update its value and refresh it to the front
            node = self.hash_map[key]
            node.val = value
            self._remove(node)
            self._add_to_front(node)
        else:
            # 2. If it's new, create a new node
            new_node = doubleListNode(key, value)
            self.hash_map[key] = new_node
            self._add_to_front(new_node)

            # 3. Check if we exceeded capacity; if so, evict the LRU item
            if len(self.hash_map) > self.capacity:
                # The LRU node is always sitting right before the tail
                lru = self.tail.prev
                self._remove(lru)
                del self.hash_map[lru.key]


if __name__ == "__main__":
    # Initialize LRUCache with capacity 2
    lru_cache = LRUCache(2)

    lru_cache.put(1, 1)  # cache is {1=1}
    lru_cache.put(2, 2)  # cache is {1=1, 2=2}

    print(lru_cache.get(1))  # returns 1 (key 1 is now most recently used)

    lru_cache.put(3, 3)  # evicts key 2 because capacity is 2, cache is now {1=1, 3=3}

    print(lru_cache.get(2))  # returns -1 (not found / was evicted)

    lru_cache.put(4, 4)  # evicts key 1, cache is now {3=3, 4=4}

    print(lru_cache.get(1))  # returns -1 (not found / was evicted)
    print(lru_cache.get(3))  # returns 3
    print(lru_cache.get(4))  # returns 4


