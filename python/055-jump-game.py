# 重點: 如果i+k可以走到, [0, i+k]全部都可以走到
# 為什麼可以iterate一次就好, 不會有"後面東西更新後前面的的就變成能走"的情況嗎?
# 不會, 因為如果前面走不到, 後面就一定走不到, 會直接return False
# 作法: 維護[0, r](可走的點), 他必定為連續的
class Solution:
    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        r = 0
        for i in range(len(nums)):
            if i <= r:
                if i == len(nums)-1:
                    return True
                r = max(nums[i]+i, r)
            else:
                return False
        
        return False