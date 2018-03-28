class Solution(object):
    def reverseStr(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: str
        """
	    s = list(s)
	    for i in xrange(0, len(s), 2*k):
	        s[i:i+k] = reversed(s[i:i+k])
	    return "".join(s)

class Solution(object):
    def reverseStr(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: str
        """
        start = 0
        s =list(s)
        while start+2*k <= len(s):
            for i in range(int(k/2)):
                s[start+i], s[start+k-1-i] = s[start+k-1-i], s[start+i]
            start = start + 2*k
        if start + k <= len(s):
            for i in range(int(k/2)):
                s[start+i], s[start+k-1-i] = s[start+k-1-i], s[start+i]
        if start + k > len(s):
            for i in range(int((len(s)-start)/2)):
                s[start+i], s[len(s)-1-i] = s[len(s)-1-i], s[start+i]
        return ''.join(s)