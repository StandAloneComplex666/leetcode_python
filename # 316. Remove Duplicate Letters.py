class Solution(object):
    def removeDuplicateLetters(self, s):
        """
        :type s: str
        :rtype: str
        """
        vis, cnt = [False] * 26, [0] * 26
        ans = []
        for c in s:
            cnt[ord(c) - 97] += 1  # ord(a) =97
        for c in s:
            index = ord(c) - 97
            cnt[index] -= 1
            if vis[index]: continue
            while ans and ans[-1] > c and cnt[ord(ans[-1]) - 97]:
                vis[ord(ans.pop()) - 97] = False
            ans.append(c)
            vis[index] = True
 
        return ''.join(ans)


class Solution(object):
    def removeDuplicateLetters(self, s):
        if not s: return ''
        last_pos = {}
        for i, c in enumerate(s):
            last_pos[c] = i
 
        last_pos = collections.OrderedDict(sorted(last_pos.items(), key=lambda x: x[1]))
        start, end = 0, last_pos.items()[0][1]
        ans = []
        for i in xrange(len(last_pos)):
            min_c = 'z'
            for k in xrange(start, end + 1):
                if min_c > s[k] and s[k] in last_pos:
                    min_c = s[k]
                    start = k + 1
            ans += [min_c]
 
            del last_pos[min_c]
            if not last_pos:  break
            end = last_pos.items()[0][1]
 
        return ''.join(ans)

Python

class Solution(object):
    def removeDuplicateLetters(self, s):
        """
        :type s: str
        :rtype: str
        """
        ans = ''
        while s:
            cnt = collections.Counter(s)
            min_c, index = s[0], 0
            for i, c in enumerate(s):
                if min_c > c:
                    min_c, index = c, i
                cnt[c] -= 1
                if not cnt[c]: break
            ans += min_c
            s = s[index + 1:].replace(min_c,'')
        return ans

class Solution(object):
    def removeDuplicateLetters(self, s):
        """
        :type s: str
        :rtype: str
        """
        ans = ''
        while s:
            cnt = collections.Counter(s)
            min_c, index = s[0], 0
            for i, c in enumerate(s):
                if min_c > c:
                    min_c, index = c, i
                cnt[c] -= 1
                if not cnt[c]: break
            ans += min_c
            s = s[index + 1:].replace(min_c,'')
        return ans