#6 zigzag conversion/132ms/44.02%
#version 1
class Solution(object):
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        if numRows == 1 or numRows > len(s):
            return s
        count = 0
        n=numRows  
        size=2*n-2  
        result=[]  
        for i in range(n):  
            j=i  
            while j<len(s):  
                result.append(s[j])  
                if i!=0 and i!=n-1 and j+size-2*i<len(s):  
                    result.append(s[j+size-2*i])  
                j+=size         
        return "".join(result)

#version 2
class Solution(object):
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        if numRows == 1:
            return s
        l = [""] * numRows
        index, step = 0 , 1
        for x in s:
            l[index] += x
            if index == 0:
                step = 1
            if index == numRows - 1:
                step = -1
            index += step
        return "".join(l)