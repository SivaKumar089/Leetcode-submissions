class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        i = j = 0
        res = []

        while i < len(nums1) and j < len(nums2):
            if nums1[i] < nums2[j]:
                res.append(nums1[i])
                i+=1
            else:
                res.append(nums2[j])
                j+=1
        
        res.extend(nums1[i:])
        res.extend(nums2[j:])

        mid = (len(res) - 1) // 2

        if len(res) % 2 == 0:
            return (res[mid] + res[mid + 1]) / 2
        return res[mid]