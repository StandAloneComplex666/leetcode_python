#401 binary watch
#version1 /42ms /62.84%
class Solution(object):
    def readBinaryWatch(self, num):
        """
        :type num: int
        :rtype: List[str]
        """
        ans = []
        for i in range(12):
            for j in range(60):
                if (bin(i)+bin(j)).count('1') == num:
                    ans.append('%d:%02d' % (i, j))
        return ans

#version2 32ms /fastest so far
class Solution(object):
    
    
        
    def readBinaryWatch(self, num):
        """
        :type num: int
        :rtype: List[str]
        """
        def popcount(x):
            return bin(x).count("1")
        
        if num == 0:
            return ["0:00"]
        
        hour_list = [[] for i in range(4)]
        min_list = [[] for i in range(6)]
        
        
        for hour in range(12):
            hour_list[popcount(hour)].append(hour) 
        
        for minute in range(60):
            min_list[popcount(minute)].append(minute)
        
        #print min_list[5]
        result = []
        for h_bits in range(min(num+1,4)):
            
            m_bits = num - h_bits
            
            if m_bits < 6:    
                hours = hour_list[h_bits] 
                mins = min_list[m_bits]
                for hour in hours:
                    for minute in mins:
                        result.append(str(hour) + ":" + format(minute,'02d'))
                        
        return result