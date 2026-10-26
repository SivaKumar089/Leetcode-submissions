class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        res = []
        self.backtrack(res, candidates, 0, [], target)
        return res
    
    def backtrack(self, res, nums, pos, temp, target):

        
        if target == 0:
            res.append(temp[:])
            return

        for i in range(pos, len(nums)):
            if target < nums[i]:
                return
            if i > pos and nums[i] == nums[i-1]:
                continue
            temp.append(nums[i])
            self.backtrack(res, nums, i + 1, temp, target - nums[i])
            temp.pop()