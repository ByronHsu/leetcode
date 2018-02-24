from collections import deque
class Solution:
    def minWindow(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        dic = {}
        for i in t:
            if i not in dic:
                dic[i] = [1, deque()]
            else:
                dic[i][0] += 1
        # print(dic)
        ran = []
        for i in range(len(s)):
            if s[i] in dic:
                if dic[s[i]][0] > 0:
                    dic[s[i]][0] -= 1
                    dic[s[i]][1].append(i)
                else:
                    dic[s[i]][1].popleft()
                    dic[s[i]][1].append(i)
            # print(dic)
            for key in dic:
                if dic[key][0] != 0:
                    break
            else:
                l, r = 2**32, -2**32
                for key in dic:
                    l = min(l, dic[key][1][0])
                    r = max(r, dic[key][1][-1])
                if len(ran) == 0:
                    ran = [l, r]
                elif r - l < ran[1] - ran[0]:
                    ran[0], ran[1] = l, r
                # print(dic)
                # print(l, r)
                # print(ran)

        # print(ran)
        if len(ran) == 0:
            return ""
        else:
            return s[ran[0]:ran[1]+1]
                