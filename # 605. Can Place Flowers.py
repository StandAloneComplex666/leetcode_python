class Solution(object):
    def canPlaceFlowers(self, flowerbed, n):
        """
        :type flowerbed: List[int]
        :type n: int
        :rtype: bool
        """
        count = 0
        count_zero = 0
        flowerbed_temp =[0]+flowerbed+[0]
        #print(flowerbed_temp)
        for i in xrange(0,len(flowerbed_temp)):
            if flowerbed_temp[i] == 0:
                count_zero += 1
            elif count_zero != 0 and flowerbed_temp[i] == 1:
                #print(count_zero)
                count += int(0.5*(count_zero - 1))
                count_zero = 0
            else:
                continue
        count += int(0.5*(count_zero-1))
        return count >= n