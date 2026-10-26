class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        self.backtrack(res, nums, 0, [])
        return res
    def backtrack(self, res, nums, pos, temp):
        res.append(temp[:])

        for i in range(pos, len(nums)):
            temp.append(nums[i])
            self.backtrack(res, nums, i + 1, temp)
            temp.pop()


