from queue import Queue
class Solution:
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        L = []
        for c in s:
          if c != ')' and c != '(':
            continue
          if len(L) and c == ')' and L[-1] == '(':
            L.pop()
          else:
            L.append(c)
        if len(L): return False
        else: return True
        
    def removeInvalidParentheses(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        q = Queue()
        q.put((s, 0))
        mdepth, ans, dic = None, [], {}
        while not q.empty():
            fs, fd = q.get()
            if self.isValid(fs):
                if not mdepth:
                    mdepth = fd
                if mdepth != None and mdepth == fd:
                    ans.append(fs) 
                continue
            if mdepth:
                continue
            for i in range(len(fs)):
                if fs[i] == '(' or fs[i] == ')':
                    ns = fs[:i] + fs[i+1:]
                    if ns not in dic:
                        q.put((ns, fd + 1))
                        dic[ns] = True
        return ans