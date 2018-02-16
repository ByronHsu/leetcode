from queue import PriorityQueue

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None
    def printList(self):
        now = self
        print(now.val, end='')
        now = now.next
        while now != None:
          print('->{}'.format(now.val), end='')
          now = now.next
        print()

class Solution:
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        dummy = ListNode(None)
        curr = dummy
        pq = PriorityQueue()
        for i, e in enumerate(lists):
          # print(e.val)
          if e:
            pq.put((e.val, i, e))
        
        while pq.qsize() > 0:
          pop = pq.get()
          curr.next, li = pop[2], pop[1]
          curr = curr.next
          if curr.next: pq.put((curr.next.val, li, curr.next))
        return dummy.next

def construct(L):
  if len(L):
    head = ListNode(L[0])
  else:
    head = None
  now = head
  for i in range(1, len(L)):
    now.next = ListNode(L[i])
    now = now.next
  return head

def test(L):
  print('ans: {}'.format(Solution().mergeKLists(L).printList()))

if __name__ == '__main__':
  test([construct([2, 2, 4]), construct([1, 3, 4]), construct([1, 3, 4]), construct([1, 3, 4]), construct([1, 3, 4])])
