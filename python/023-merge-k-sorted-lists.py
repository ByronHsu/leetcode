# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

from queue import PriorityQueue

class Element:
    def __init__(self, node, val):
        self.node = node
        self.val = val
    def __lt__(self, other):
        return self.val < other.val

class Solution:
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        pq = PriorityQueue()
        for l in lists:
            if l: pq.put(Element(l, l.val))

        dummy = cur = ListNode(0)

        while not pq.empty():
            top = pq.queue[0]
            cur.next = pq.get()
            if top.next: pq.put(Element(top.next, top.next.val))
            cur = cur.next
        return dummy.next