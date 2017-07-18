#447. Number of Boomerangs 1055ms/88.04%
class Solution(object):  
  
    def numberOfBoomerangs(self, points):  
        p = points  
  
        res = 0  
        for i in xrange(len(p)):  
            dic = {}  
            for j in xrange(len(p)):  
  
                dist = (p[j][1] - p[i][1])**2 +  (p[j][0] - p[i][0])**2  
                dic[dist] = dic.get(dist,0) +1  
  
            #print dic  
            for i in dic.values():  
                if i > 1:  
                    res += i*(i-1)  
  
  
        return res  