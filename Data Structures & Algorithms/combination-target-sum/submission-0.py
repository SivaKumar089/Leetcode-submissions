class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
        self.backtrack(res, nums, 0, [], target)
        return res
    
    def backtrack(self, res, nums, pos, temp, target):
        if target  < 0: 
            return 
        
        if target == 0:
            res.append(temp[:])

        for i in range(pos, len(nums)):
            temp.append(nums[i])
            self.backtrack(res, nums, i, temp, target - nums[i])
            temp.pop()
        