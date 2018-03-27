class FenwickTree:
    def __init__(self, size):
        self.node = [0]*(size + 1) # 從1開始編號
        self.size = size
    def query(self, i):
        Sum = 0
        while i != 0:
            Sum += self.node[i]
            i -= self.lowbit(i)
        return Sum
    def update(self, i, load):
        while i <= self.size:
            self.node[i] += load
            i += self.lowbit(i)
    def lowbit(self, x):
        return x & (-x)

class Solution(object):
    def countSmaller(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        sort = sorted(nums)
        rank = {}
        count = 1
        # create map from num to rank
        for i in range(len(sort)):
            if i > 0 and sort[i] != sort[i-1]:
                count += 1
            rank[sort[i]] = count # count from one

        f = FenwickTree(len(nums))
        ans = []
        for i in reversed(range(len(sort))):
            r = rank[sort[i]]
            f.update(r, 1)
            ans.append(f.query(r))
        return list(reversed(ans))