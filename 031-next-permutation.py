# Implement next permutation, which rearranges numbers into the lexicographically next greater permutation of numbers.

# If such arrangement is not possible, it must rearrange it as the lowest possible order (ie, sorted in ascending order).

# The replacement must be in-place, do not allocate extra memory.

# Here are some examples. Inputs are in the left-hand column and its corresponding outputs are in the right-hand column.
# 1,2,3 → 1,3,2
# 3,2,1 → 1,2,3
# 1,1,5 → 1,5,1
# 思路:
#   先找從右邊看回來第一個往下落的地方[i-1, i], 同時[i, n-1]會是一個reverse sorted的list
#   要如何找到[i-1, n-1]下一個值呢? 第一步理所當然的是先把i-1用[i, n-1]中第一個比i-1大的數換掉
#   但這樣還不是下一個比他大的值, 我們必須讓[i, n-1]變得最小, 如何讓它變得最小呢?
#   因為他在我們替換完之後仍然是reverse sorted的, 所以我們只有將它反地sort回來就ok了 
class Solution:
    def nextPermutation(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        for i in reversed(range(1, len(nums))):
          if nums[i-1] < nums[i]:
            for j in reversed(range(i, len(nums))):
              if nums[j] > nums[i-1]:
                nums[i-1], nums[j] = nums[j], nums[i-1]
                break
            nums[i:] = sorted(nums[i:])
            return
        nums.sort()
        return

def test(L):
  print('ans:', Solution().nextPermutation(L))

if __name__ == '__main__':
  # test([5,4,6,2,3,4,2,1])
  test([1,2,3])