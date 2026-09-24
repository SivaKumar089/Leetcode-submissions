class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs:
            return ""
        
        prefix = strs[0]
        n = len(strs)

        for i in range(1, n):
            while not strs[i].startswith(prefix):
                prefix = prefix[:-1]
        return prefix