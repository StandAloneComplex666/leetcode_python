#187. Repeated DNA Sequences
class Solution:
    # @param s, a string
    # @return a list of strings
    def findRepeatedDnaSequences(self, s):
        dict={}
        for i in range(len(s)-9):
            key=s[i:i+10]
            if key not in dict:
                dict[key]=1
            else:
                dict[key]+=1
        res=[]
        for elem in dict:
            if dict[elem]>1:
                res.append(elem)
        return res

class Solution(object):
    def findRepeatedDnaSequences(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        appear_dict = {}
        result_set = set()
        
        
        for i in xrange(len(s)-9):
            substr = s[i:i+10]            
            if substr in appear_dict:
                result_set.add(substr)
            else:
                appear_dict[substr] = 1
                
        return list(result_set)