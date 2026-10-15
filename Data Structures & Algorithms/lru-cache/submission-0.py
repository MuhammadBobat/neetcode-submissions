class Node:

    def __init__(self, val=None, key=None, next=None, prev=None):
        self.val = val
        self.prev = prev
        self.next = next
        self.key = key

class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = {}
        self.head = Node()
        self.tail = Node()
        self.head.next = self.tail
        self.tail.prev = self.head

    def _add_to_front(self, node):
        node.prev = self.head
        new_next = self.head.next
        self.head.next = node
        node.next = new_next
        new_next.prev = node

    def _remove(self, node):
        prev_node = node.prev
        next_node = node.next
        prev_node.next = node.next
        next_node.prev = prev_node
    

    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1

        # Update new pointers
        node = self.cache[key]
        self._remove(node)

        # Bring accessed node to the front - updates recency
        self._add_to_front(node)

        return node.val
        

    def put(self, key: int, value: int) -> None:
        # For existing nodes, update value and move to front
        if key in self.cache:
            node = self.cache[key]
            node.val = value
            
            # Call functions to move 'updated' node to the front
            self._remove(node)
            self._add_to_front(node)

        # For new nodes, initialise them and add to front
        else:
            self.cache[key] = Node(val=value, key=key)
            self._add_to_front(self.cache[key])

        # Release old entries at the back of the Linked List
        if len(self.cache) > self.capacity:
            # Remove end node (LRU)
            remove = self.tail.prev
            del self.cache[remove.key]
            self._remove(remove)
            

        
