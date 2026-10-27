class Solution:
    def partition(self, s: str) -> List[List[str]]:
        res = []
        temp = []

        def dfs(i):
            if i >= len(s):
                res.append(temp[:])
            
            for j in range(i, len(s)):
                if self.isPalidrome(s, i, j):
                    temp.append(s[i: j + 1])
                    dfs(j + 1)
                    temp.pop()
        
        dfs(0)
        return res

    def isPalidrome(self, s, left, right):
        while left < right:
            if s[left] != s[right]:
                return False
            left +=1
            right -=1
        return True
