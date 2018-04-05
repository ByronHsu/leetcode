# Definition for singly-linked list.
# class ListNode:
    # def __init__(self, x):
    #     self.val = x
    #     self.next = None

def printList(node):
    now = node
    while now:
        if now.val: print('({})->'.format(now.val), end='')
        now = now.next
    print()

class Solution:
    def sortList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        # count length
        L = 0
        end = head
        while end and end.next != None:
            end = end.next
            L += 1
        return self.mergeSort(head, end, L)
    def mergeSort(self, head, end, length):
        if length == 0: return head
        count = length // 2
        mid = head
        while count != 0:
            mid = mid.next
            count -= 1
        nxt = mid.next
        mid.next = None
        end.next = None
        L = self.mergeSort(head, mid, length//2)
        R = self.mergeSort(nxt, end, length - length//2 - 1)
        return self.mergeTwoLists(L, R)
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        dummy = cur = ListNode(0)
        while l1 and l2:
            if l1.val < l2.val:
                cur.next = l1
                l1 = l1.next
            else:
                cur.next = l2
                l2 = l2.next
            cur = cur.next
        cur.next = l1 or l2
        return dummy.next
        