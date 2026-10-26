class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []
        self.backtrack(res, 0, 0, "", n)
        return res
    def backtrack(self, res, open_count, close_count, pair, n):

        if len(pair) == 2 * n:
            res.append(pair)
            return
        
        if open_count < n:
            self.backtrack(res, open_count + 1, close_count, pair + '(', n)
        if open_count > close_count:
            self.backtrack(res, open_count, close_count + 1, pair + ')', n)
