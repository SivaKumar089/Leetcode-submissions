class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []
        self.backtrack(res, nums, 0, [] )
        return res
    def backtrack(self, res, nums, i, temp):
        res.append(temp[:])

        for j in range(i, len(nums)):

            if j > i and nums[j] == nums[j - 1]:
                continue
            
            temp.append(nums[j])
            self.backtrack(res, nums, j + 1, temp)
            temp.pop()
        
