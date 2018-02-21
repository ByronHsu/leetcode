# Given n non-negative integers a1, a2, ..., an, where each represents a point at coordinate (i, ai). n vertical lines are drawn such that the two endpoints of line i is at (i, ai) and (i, 0). Find two lines, which together with x-axis forms a container, such that the container contains the most water.

# Note: You may not slant the container and n is at least 2.

# 思路:
#   使用two pointers
#   key point: 
#   當a[i] < a[j]時 不管怎麼往內移動j都不可能讓面積更大
#   因此將i往內
class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        ans = -2**32 + 1
        l, r = 0, len(height) - 1
        while(l < r):
          ans = max(ans, min(height[l], height[r])*(r-l))
          if height[l] < height[r]:
            l += 1
          else:
            r -= 1
      
        return ans

def test(L):
  print('ans: {}'.format(Solution().maxArea(L)))

if __name__ == '__main__':
  test([6, 3, 7, 2, 4, 3])