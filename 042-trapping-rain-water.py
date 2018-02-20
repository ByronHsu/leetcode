# 思路:
#     窪地存在的條件為左右兩邊必然有東西比他高, 我們稱兩旁的東西為bar
#     第一個步驟: 先把bar找出來
#     創建一個stack 只要他比左右兩邊小 就把他擠掉
#     第二個步驟: 根據bar stack去計算水量

class Solution:
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        s = []
        for i in range(len(height)):
            while len(s) >= 2 and s[-1][1] <= s[-2][1] and s[-1][1] <= height[i]: 
                # 當他比前一個與後一個小時 把它擠掉
                s.pop()
            s.append((i, height[i]))

        ans = 0
        for i in range(1, len(s)):
            cum = 0
            h = min(s[i-1][1], s[i][1])
            for j in range(s[i-1][0]+1, s[i][0]-1+1):
                cum += h-height[j]
            ans += cum
        return ans

def test(L):
    print(Solution().trap(L))

if __name__ == '__main__':
    test([0,1,0,2,1,0,1,3,2,1,2,1])
    test([])

