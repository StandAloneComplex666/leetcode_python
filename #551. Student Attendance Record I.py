#551. Student Attendance Record I/39ms/66.42%
class Solution(object):
    def checkRecord(self, s):
        """
        :type s: str
        :rtype: bool
        """
        a = 0
        l = 0
        for i in range(len(s)):
            if s[i] == 'A':
                a = a + 1
            if s[i] == 'L':
                if i<=len(s)-3:
                    if s[i+1] == 'L' and s[i+2] == 'L':
                        return False                    
            if a > 1:
                return False
        return True