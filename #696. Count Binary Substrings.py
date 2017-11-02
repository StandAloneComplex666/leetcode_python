class Solution:
    def countBinarySubstrings(self, s):
        """
        :type s: str
        :rtype: int
        """
        pre_len = 0 
        cur_len = 1
        res = 0
        for i in range(1,len(s)):
            if s[i] == s[i-1]:
                cur_len+=1
            else:
                pre_len = cur_len
                cur_len = 1
            if pre_len >= cur_len:
                res+=1
        return res