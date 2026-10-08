class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(s) < len(t) or not t:
            return ""

        t_freq = {}
        for ch in t:
            t_freq[ch] = t_freq.get(ch, 0) + 1

        window_freq = {}
        have, need = 0, len(t_freq)
        res_len = float("inf")
        res_range = (-1, -1)
        left = 0

        for right in range(len(s)):
            ch = s[right]
            window_freq[ch] = window_freq.get(ch, 0) + 1

            if ch in t_freq and window_freq[ch] == t_freq[ch]:
                have += 1

            while have == need:
                curr_len = right - left + 1
                if curr_len < res_len:
                    res_len = curr_len
                    res_range = (left, right)

                left_ch = s[left]
                window_freq[left_ch] -= 1
                if left_ch in t_freq and window_freq[left_ch] < t_freq[left_ch]:
                    have -= 1

                left += 1

        start, end = res_range
        return s[start : end + 1] if res_len != float("inf") else ""