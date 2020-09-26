class Solution:
    def longestSubstring(self, s: str, k: int) -> int:
        if not s or len(s) == 0:
            return 0

        char_stat = {}
        for curr_char in s:
            if curr_char not in char_stat:
                char_stat[curr_char] = 0
            char_stat[curr_char] += 1
        res = 0
        for curr_char in s:
            if char_stat[curr_char] < k:
                return max(self.longestSubstring(temp_str, k) for temp_str in s.split(curr_char))
        
        return len(s)