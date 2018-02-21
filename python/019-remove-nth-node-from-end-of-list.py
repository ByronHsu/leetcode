# Definition for singly-linked list.
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
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        length = 0
        now = head
        L = [now]
        while now != None:
          length += 1
          now = now.next
          L.append(now)
        index = length - n
        if index == 0:
          return L[1]
        elif index == length - 1:
          L[index - 1].next = None
        else:
          L[index - 1].next = L[index + 1]
        return head

def construct(L):
  head = ListNode(L[0])
  now = head
  for i in range(1, len(L)):
    now.next = ListNode(L[i])
    now = now.next
  return head

def test(head, n):
  print('ans: {}'.format(Solution().removeNthFromEnd(head, n)))

if __name__ == '__main__':
  test(construct([1, 2, 3, 4, 5]), 1)