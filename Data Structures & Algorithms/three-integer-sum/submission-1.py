class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        n = len(nums)
        res = []

        for i in range(n - 1):
            if i == 0 or nums[i] != nums[i - 1]:
                low = i + 1
                high = n - 1
                target = -nums[i]

                while low < high:
                    curr_sum = nums[low] + nums[high]

                    if curr_sum == target:
                        res.append([nums[i], nums[low], nums[high]])

                        while low < high and nums[low] == nums[low + 1]:
                            low +=1   

                        while low < high and nums[high] == nums[high - 1]:
                            high -=1   

                        low +=1
                        high -=1
                    elif curr_sum < target:
                        low +=1
                    else:
                        high -=1
        return res
                