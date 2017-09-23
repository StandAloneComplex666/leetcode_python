# -*- coding: utf-8 -*-
"""
Created on Fri Jun 16 19:14:52 2017

@author: hp
"""
class twosum(object):
    def sumoftwo(self, num ,target):
        hash ={}
        for i in range(len(num)):
            if target - num[i] in hash:
                return [hash[target-num[i]], i]
            hash[num[i]] = i
        return [-1,-1]

if __name__ == "__main__":
    num =[2,7,11,15]
    target = 9
    ts = twosum()
    output = ts.sumoftwo(num,target)
    
    