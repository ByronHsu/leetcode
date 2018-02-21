# Merge two sorted linked lists and return it as a new list. The new list should be made by splicing together the nodes of the first two lists.

# Example:

# Input: 1->2->4, 1->3->4
# Output: 1->1->2->3->4->4
class ListNode(object):
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


class Solution(object):
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        L1, L2, L = [], [], []
        now1, now2 = l1, l2
        while now1 != None:
          L1.append(now1.val)
          now1 = now1.next
        while now2 != None:
          L2.append(now2.val)
          now2 = now2.next
        p1, p2 = 0, 0
        

        while p1 < len(L1) or p2 < len(L2):
          T1, T2 = list(range(len(L1))), list(range(len(L2)))
          
          if p1 in T1 and p2 in T2:
            if L1[p1] < L2[p2]:
              L.append(L1[p1])
              p1 += 1
            else:
              L.append(L2[p2])
              p2 += 1
          else:
            if p1 not in T1 and p2 not in T2:
              break
            elif p1 not in T1:
              L.append(L2[p2])
              p2 += 1
            elif p2 not in T2:
              L.append(L1[p1])
              p1 += 1

        def constructList(L):
            if len(L):
              head = ListNode(L[0])
            else:
              head = None
            now = head
            for i in range(1, len(L)):
              now.next = ListNode(L[i])
              now = now.next
            return head
            
        return constructList(L)

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

def test(l1, l2):
  print('ans: {}'.format(Solution().mergeTwoLists(l1, l2).printList()))

if __name__ == '__main__':
  # test(construct([1, 2, 4]), construct([1, 3, 4]))
  test(construct([]), construct([0]))
  test(construct([1]), construct([2]))