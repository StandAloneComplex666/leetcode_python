#5. Longest Palindromic Substring 
#version 1: someelse's very fast /about 150ms
class Solution(object):
    
    def longestPalindrome(self,s):
        if len(s) < 2:
            return s
        s = '#' + '#'.join(s) + '#'
        p = []
        #记录比较过程中右边能到达的最远地方 以及到达最远地方时的中心点
        rightMax,mid = 0,0
        maxPval = 0
        maxPidx = 0
        for i in range(len(s)):
            # 比较过的最右边大于当前比较索引时才有可能减少比较次数
            if rightMax > i:
                # i关于mid的对称点
                i2 = 2*mid-i
                if p[i2] < rightMax-i:
                    # 可以直接根据对称点的p值得到  跳出循环
                    p.append(p[i2])
                    continue
                else:
                    # 从没有遍历到的地方开始遍历 不用从左边第一个开始比较
                    start = 2*i - rightMax - 1
            else:
                # 这种情况只能从左边第一个开始比较  回文串只记录左边索引  左右索引关系 ：end - i = i - start
                start = i - 1
            while start >= 0 and 2 * i - start < len(s) and s[start] == s[2 * i - start]:

                if 2*i - start > rightMax:
                    rightMax = 2*i - start
                    mid = i
                start -= 1
            # 记录p中最大值
            if maxPval<i-start-1:
                maxPval = i-start-1
                maxPidx = i
            p.append(i - start - 1)
        begin,end = maxPidx-maxPval,maxPidx+maxPval
        result = s[begin:end+1]
        return result.replace('#','')

#version 2: my version very slow like 1300ms
class Solution:
    # @return a string
    def ispalindrome(self, s, l, r):
        while l >= 0 and r < len(s) and s[l] == s[r]:
            l -= 1; r += 1
        return s[l+1 : r]
    def longestPalindrome(self, s):
        palindrome = ''
        for i in range(len(s)):
            # palindrome centered like aba
            strp = self.ispalindrome(s, i-1, i+1)
            len1 = len(strp)
            if len1 > len(palindrome): palindrome = strp
            # palindrome centered like aa
            strp2 = self.ispalindrome(s, i, i + 1)
            len2 = len(strp2)
            if len2 > len(palindrome): palindrome = strp2
        return palindrome