class ListNode:
    def __init__(self, key = None, val = None):
        self.key = key
        self.val = val
        self.next, self.prev = None, None
    def printList(self):
        now = self
        while now:
            if now == self: print('head->', end='')
            if now.val: print('({},{})->'.format(now.key, now.val), end='')
            now = now.next
        print()
class LRUCache:
    def __init__(self, capacity):
        """
        :type capacity: int
        """
        self.size = capacity
        self.start, self.end = ListNode(), ListNode()
        self.hashTable = {}
        self.start.next = self.end
        self.end.prev = self.start
    # utils function
    def removeNode(self, key):
        node = self.hashTable[key]
        L, R = node.prev, node.next
        L.next, R.prev = node.next, node.prev
    def insertNodeEnd(self, key):
        node = self.hashTable[key]
        L, R = self.end.prev, self.end
        L.next, node.prev = node, L
        R.prev, node.next = node, R
    def insertHash(self, key, value):
        self.hashTable[key] = ListNode(key, value)
    def removeHash(self, key):
        del self.hashTable[key]
    def get(self, key):
        """
        :type key: int
        :rtype: int
        """
        if not (key in self.hashTable): return -1
        self.removeNode(key)
        self.insertNodeEnd(key)
        return self.hashTable[key].val
    def put(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: void
        """
        if key in self.hashTable:
            self.hashTable[key].val = value
            self.removeNode(key)
        else:
            self.insertHash(key, value)
        self.insertNodeEnd(key)  
        keyToBeRemoved = self.start.next.key
        if len(self.hashTable) > self.size:
            self.removeNode(keyToBeRemoved)
            self.removeHash(keyToBeRemoved)
        return