class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        freq = {}

        for num in nums:
            freq[num] = freq.get(num, 0) + 1
        res =[]
        for num, key in freq.items():
            if key > len(nums) // 3:
                res.append(num)
        return res