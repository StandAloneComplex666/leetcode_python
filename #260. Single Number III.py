class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        if not nums:
            return [0,0]
        res = []
        res_record = {}
        for i in nums:
            if i not in res_record:
                res_record[i] =-1
            else:
                res_record[i]*=-1
        print(res_record)
        for i in nums:
            if res_record[i] < 0:
                res.append(i)
        if len(res) == 1:
            res.append(0)
        if len(res) == 0:
            res=[0,0]
        return res