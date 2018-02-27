class Solution:
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        dic = {}
        ans = 0
        for n in nums:
            if n in dic:
                continue
            l, r = n-1 in dic, n+1 in dic
            if l and r:
                llen, rlen = dic[n-1], dic[n+1]
                dic[n-llen] = llen+rlen+1
                dic[n+rlen] = llen+rlen+1
                dic[n] = 1
                ans = max(llen+rlen+1, ans)
            elif l:
                llen = dic[n-1]
                dic[n] = llen+1
                dic[n-llen] = llen+1
                ans = max(llen+1, ans)
            elif r:
                rlen = dic[n+1]
                dic[n] = rlen+1
                dic[n+rlen] = rlen+1
                ans = max(rlen+1, ans)
            else:
                dic[n] = 1
                ans = max(1, ans)

        print(ans)
        return ans
if __name__ == '__main__':
    Solution().longestConsecutive([4,0,-4,-2,2,5,2,0,-8,-8,-8,-8,-1,7,4,5,5,-4,6,6,-3])

