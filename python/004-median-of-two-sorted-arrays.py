
# There are two sorted arrays nums1 and nums2 of size m and n respectively.

# Find the median of the two sorted arrays. The overall run time complexity should be O(log (m+n)).

# Example 1:
# nums1 = [1, 3]
# nums2 = [2]

# The median is 2.0
# Example 2:
# nums1 = [1, 2]
# nums2 = [3, 4]

# The median is (2 + 3)/2 = 2.5
import math

class Solution:
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        l1, l2 = len(nums1), len(nums2)
        ls = l1 + l2
        # k: 以pivot為基準, 前面共有k個
        # 若為偶數則中位數即為pivot的左右兩邊平均, 若為奇數則中位數為pivot左方
        if(ls % 2 == 0): # 偶數
          k = ls / 2
        else:
          k = math.floor(ls / 2)
        # 在兩端包dummy node 避免掉很煩的code ex: a[-1]不存在...
        nums1.append(2**32-1)
        nums2.append(2**32-1)
        nums1.insert(0, -2**32+1)
        nums2.insert(0, -2**32+1)
        # [1, l1+1]
        l, r = 1, l1+1
        # 以l1為準二分搜
        while(l <= r):
          mid = math.floor((l + r) / 2)
          idx1 = mid
          idx2 = int(k - mid + 2)
          # 若idx2超出範圍 l2:[d,x,x,x,d] l2範圍亦為[1, l2+1]
          if(idx2 > l2 + 1):
            l = mid + 1
          # 若idx2超出範圍
          elif(idx2 < 1):
            r = mid - 1
          else:
            # 共有三種情況
            # 若a1<b2&&b1<a2則他即是我們要的pivot!直接break掉
            a1, a2 = nums1[idx1 - 1], nums1[idx1]
            b1, b2 = nums2[idx2 - 1], nums2[idx2]
            if(a2 < b1):
              l = mid + 1
            elif(b2 < a1):
              r = mid - 1
            else:
              break

        m1 = max(nums1[idx1 - 1], nums2[idx2 - 1])
        m2 = min(nums1[idx1], nums2[idx2])
        
        if(ls % 2 == 0):
          return (m1 + m2) / 2
        else:
          return m2


def test(l1, l2):
  print('input: l1:{} l2:{}'.format(l1,l2))
  print(Solution().findMedianSortedArrays(l1,l2))

if __name__ == '__main__':
  test([2], [])
  test([1,2,3],[4,5,6])
  test([1,2],[3,4,5])
  test([1,2],[3,4,5,6])
  test([1,2],[3,4,5,6,7])
  test([2,4],[1,3,5])
  test([9,10],[2,4,6])
  test([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22],[0,6])