class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        left = 0
        freq = {}
        max_freq = 0
        max_window = 0

        for right, ch in enumerate(s):
            freq[ch] = freq.get(ch, 0)  + 1

            max_freq = max(max_freq, freq[ch])
            window_length = right - left + 1
            change_char = window_length - max_freq

            if change_char > k:
                left_char = s[left]
                freq[left_char] -=1
                left +=1
            
            max_window = max(max_window, right - left + 1)
        return max_window