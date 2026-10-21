class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        num_set = set(nums)

        longest = 0

        for num in num_set:

            if num - 1 not in num_set:
                temp = []
                curr = num

                while curr in num_set:
                    temp.append(curr)
                    curr +=1
                
                longest = max(longest, len(temp))
        return longest