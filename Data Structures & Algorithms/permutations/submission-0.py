class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        self.backtrack(res, nums, [False] * len(nums), [])
        return res

    def backtrack(self, res, nums, used, temp):
        if len(nums) == len(temp):
            res.append(temp[:])
            return 
        

        for i in range(len(nums)):
            
            if not used[i]:
                used[i] = True
                temp.append(nums[i])
                self.backtrack(res, nums, used, temp)

                temp.pop()
                used[i] =  False
            