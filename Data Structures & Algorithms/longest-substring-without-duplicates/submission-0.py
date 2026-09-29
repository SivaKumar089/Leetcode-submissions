class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left = 0
        char_set = set()
        longest = 0
        for right, ch in enumerate(s):

            while ch in char_set:
                char_set.remove(s[left])
                left +=1
            char_set.add(s[right])
            longest = max(longest ,right - left + 1)
        return longest
