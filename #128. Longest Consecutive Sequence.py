#128. Longest Consecutive Sequence
class Solution(object):
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        s = set(nums)
        res = 0
        for elem in s:
            if elem-1 not in s:
                nextElem = elem+1
                while (nextElem in s):
                    nextElem += 1
                res = max(res, nextElem-elem)
        return res

class Solution(object):
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        dict = {x: False for x in nums} # False means not visited
        maxLen = 0
        for i in dict:
            if dict[i] == False:
                curr = i+1; lenright = 0
                while curr in dict:
                    lenright += 1; dict[curr] = True; curr += 1
                curr = i-1; lenleft = 0
                while curr in dict:
                    lenleft += 1; dict[curr] = True; curr -= 1
                maxLen = max(maxLen, lenleft+1+lenright)
        return maxLen        