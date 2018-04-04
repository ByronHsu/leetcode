# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        now, L = head, 1
        while now.next != None:
            now = now.next
            L += 1
        tar, count = L - n, 0 # 0 1 2 3 4 ...
        prev, now = None, head
        while count != tar:
            prev, now = now, now.next
            count += 1
        if not prev: head = now.next
        else: prev.next = now.next
        return head
            