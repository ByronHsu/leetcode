class Solution:
    def minWindow(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        dic = {}
        for i in range(len(t)):
            if t[i] not in dic:
                dic[t[i]] = [1, 0, []]
            else:
                dic[t[i]][0] += 1

        ran = []
        rest = len(t)

        for i in range(len(s)):
            if s[i] in dic:
                dic[s[i]][2].append(i)
                if dic[s[i]][0] > 0:
                    dic[s[i]][0] -= 1
                    rest -= 1
                else:
                    dic[s[i]][1] += 1
            if rest == 0:
                l, r = 2**32, i
                for key in dic:
                    lidx = dic[key][1]
                    l = min(l, dic[key][2][lidx])

                if len(ran) == 0:
                    ran = [l, r]
                elif r - l < ran[1] - ran[0]:
                    ran[0], ran[1] = l, r

        if len(ran) == 0:
            return ""
        else:
            return s[ran[0]:ran[1]+1]
                

if __name__ == '__main__':
    print(Solution().minWindow('acbbaca', 'aba'))
