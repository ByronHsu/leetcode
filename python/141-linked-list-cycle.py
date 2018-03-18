# 如果有限状态机、迭代函数或者链表上存在环，
# 那么在某个环上以不同速度前进的2个指针必定会在某个时刻相遇。
# 同时显然地，如果从同一个起点(即使这个起点不在某个环上)
# 同时开始以不同速度前进的2个指针最终相遇，
# 那么可以判定存在一个环，
# 且可以求出2者相遇处所在的环的起点与长度。

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
        slow, fast = head, head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                return True
        return False
    