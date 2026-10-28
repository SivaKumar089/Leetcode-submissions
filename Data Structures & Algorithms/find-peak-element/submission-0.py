class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        def binary_search(l, r):
            if l == r:
                return l
            m = l + (r - l) // 2
            if nums[m] > nums[m + 1]:
                return binary_search(l, m)
            return binary_search(m + 1, r)

        return binary_search(0, len(nums) - 1)