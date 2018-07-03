class Solution(object):
    def wordPattern(self, pattern, str):
        """
        :type pattern: str
        :type str: str
        :rtype: bool
        """
        s = pattern
        t = str.split(' ')
        if len(s) != len(t):
            return False
        s_t_dict, t_s_dict = {}, {}
        for i in xrange(0, len(s)):
            if s[i] not in s_t_dict:
                if t[i] in t_s_dict:
                    return False
                s_t_dict[s[i]] = t[i]
                t_s_dict[t[i]] = s[i]
            else:
                if s_t_dict[s[i]] != t[i]:
                    return False
        return True 