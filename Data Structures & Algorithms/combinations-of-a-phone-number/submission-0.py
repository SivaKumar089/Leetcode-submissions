class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        res = []

        if digits == "":
            return res
        maps = ["", "", "abc", "def", "ghi", "jkl", "mno", "pqrs", "tuv", "wxyz"]

        self.backtrack(res, digits, maps, "")
        return res
    def backtrack(self, res, digits, maps, pair):

        if len(pair) == len(digits):
            res.append(pair)
            return

        for ch in maps[int(digits[len(pair)])]:
            self.backtrack(res, digits, maps, pair + ch)
         