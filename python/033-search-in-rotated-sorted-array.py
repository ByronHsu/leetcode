import math
class Solution:
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        l, r = 0, len(nums)-1
        while l < r:
          mid = math.floor((l+r)/2)
          if nums[l] <= nums[mid]: # [l, mid] sorted
            if target >= nums[l] and target <= nums[mid]:
              r = mid
            else:
              l = mid+1
          elif nums[mid] <= nums[r]: # [mid, r] sorted
            if target >= nums[mid] and target <= nums[r]:
              l = mid
            else:
              r = mid-1
        if not len(nums) or nums[l] != target:
          return -1
        else:
          return l

def test(L, t):
  print(Solution().search(L,t))

if __name__ == '__main__':
  test([4, 5, 6, 7, 0, 1, 2], 0)
  test([], 5)