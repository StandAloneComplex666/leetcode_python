#640 equation/32ms/81.14%
class Solution(object):
    def solveEquation(self, equation):
        """
        :type equation: str
        :rtype: str
        """
        s1,s2=equation.split('=')
        #print s1,s2
        if s1[0]!='-':s1='+'+s1
        if s2[0]!='-':s2='+'+s2
        countL,countLX=self.defcount(s1)
        countR,countRX=self.defcount(s2)
        #print countL,countLX
        #print countR,countRX
        if countLX==countRX:
            if countL==countR:
                return 'Infinite solutions'
            else:
                return 'No solution'
        return 'x='+str((countR-countL)/(countLX-countRX))
        
        
    def defcount(self,s):
        count=0
        countX=0
        num=''
        
        for i in xrange(len(s)):
            if s[i]=='+':
                if num!='':
                    count+=sign*int(num)
                    num=''
                sign=1
                continue
            if s[i]=='-':
                if num!='':
                    count+=sign*int(num)
                    num=''
                sign=-1
                continue
            if s[i]=='x':
                #print num
                if num!='':
                    countX+=sign*int(num)
                    num=''
                else:
                    countX+=sign
                continue
            num+=s[i]
        if num!='':count+=sign*int(num)    
        
        return [count,countX]