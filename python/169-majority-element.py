# Boyer Moore 算法(https://blog.csdn.net/kimixuchen/article/details/52787307)
# 用途: 找出數組中出現超過一半次數的數
# 原理: 當count減為0時相當於整個數組reset, 只要找右邊出現最多次的數即可
class Solution(object):
    def majorityElement(self, nums):
        major, count = nums[0], 1
        for n in nums:
            if n == major:
                count += 1
            elif count == 0:
                major = n
                count = 1
            else:
                count -= 1
        return major
