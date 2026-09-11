class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        hash_map = [0] * 128

        for ch in s:
            hash_map[ord(ch)] +=1

        for ch in t:
            hash_map[ord(ch)] -=1

        for count in hash_map:
            if count != 0:
                return False
        
        return True

