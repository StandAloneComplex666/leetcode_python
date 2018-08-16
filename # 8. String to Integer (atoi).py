class Solution:
    def myAtoi(self, str):
        """
        :type str: str
        :rtype: int
        """
        str=str.lstrip()
        if len(str)==0: return 0
        res=''
        digits=set(['1','2','3','4','5','6','7','8','9','0'])
        signs=['+','-']
        for i in range(len(str)):
            if i==0: 
                if(str[i]  in digits or str[i] in signs):
                    res=str[i]
                else:
                    return 0
            else:
                if str[i] in digits:
                    res=res+str[i]
                else:
                    break
        if len(res)==1 and res in signs: return 0
        res=int(res)
        if res>(2**31-1):
            return 2**31-1
        elif res<-2**31:
            return -2**31
        else:
            return res