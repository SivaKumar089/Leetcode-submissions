class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        
        n = len(word1)
        m = len(word2)
        i = j = 0
        dirc = True
        res = []
        while i < n and j < m:
            
    
            res.append(word1[i])
            res.append(word2[j])

            i +=1
            j +=1
      

        res.append(word1[i:])
        res.append(word2[j:])

        return "".join(res)
            

