# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        now = head
        while now != None:
            if hasattr(now, 'v') and now.v == True:
                return True
            now.v = True
            now = now.next
        return False