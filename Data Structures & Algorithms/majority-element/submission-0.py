class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        count = 0
        curr = nums[0]

        for num in nums:

            if count == 0:
                curr = num
            
            if curr == num:
                count +=1
            else:
                count -=1
        return curr