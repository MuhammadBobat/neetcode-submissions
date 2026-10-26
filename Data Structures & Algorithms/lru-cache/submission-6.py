class Node:

    def __init__(self, key=0, val=0):
        self.val = val
        self.key = key
        self.next = None
        self.prev = None
        

class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = {}

        self.start = Node()
        self.end = Node()
        self.start.next = self.end
        self.end.prev = self.start

    def _insert_to_front(self, node):
        node.next = self.start.next
        node.next.prev = node 
        node.prev = self.start
        self.start.next = node 
    
    def _remove(self, node):
        prev_node = node.prev
        prev_node.next = node.next
        node.prev = None
        node.next.prev = prev_node
        node.next = None


    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1
        else:
            node = self.cache[key]
            # Since key already exists, we remove it and re-add to front
            self._remove(node)
            self._insert_to_front(node)

            return node.val

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self._remove(self.cache[key])
            self.cache[key] = Node(key, value)
            node = self.cache[key]
            # Remove old linked list entry, append to front
            self._insert_to_front(node)
        
        else:
            # Check capacity first
            if len(self.cache) == self.capacity:
                del self.cache[self.end.prev.key]
                self._remove(self.end.prev)

            self.cache[key] = Node(key, value)

            #Append to front of linked list
            self._insert_to_front(self.cache[key])


