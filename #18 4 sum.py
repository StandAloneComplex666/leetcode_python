#18 4 sum  my version/202ms /75.06%
class Solution:
    # @return a list of lists of length 4, [[val1,val2,val3,val4]]
    def fourSum(self, num, target):
        numLen, res, dict = len(num), set(), {}
        if numLen < 4: return []
        num.sort()
        for p in range(numLen):
            for q in range(p+1, numLen): 
                if num[p]+num[q] not in dict:
                    dict[num[p]+num[q]] = [(p,q)]
                else:
                    dict[num[p]+num[q]].append((p,q))
        for i in range(numLen):
            for j in range(i+1, numLen-2):
                T = target-num[i]-num[j]
                if T in dict:
                    for k in dict[T]:
                        if k[0] > j: res.add((num[i],num[j],num[k[0]],num[k[1]]))
        return [list(i) for i in res]
#other's version 88ms
class Solution(object):
    def fourSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        nums.sort()
        ret = []
        n = len(nums)
        i = 0
        while i < n-3:
            if i>0 and nums[i] == nums[i-1]:
                i+=1
                continue
            if nums[i]+nums[i+1]+nums[i+2]+nums[i+3]>target:
                break
            if nums[i]+nums[n-3]+nums[n-2]+nums[n-1]<target:
                i+=1
                continue;
            l = i+1
            while l < n-2:
                if l>i+1 and nums[l]==nums[l-1]:
                    l+=1
                    continue
                if nums[i]+nums[l]+nums[l+1]+nums[l+2]>target:
                    break;
                if nums[i]+nums[l]+nums[n-2]+nums[n-1]<target:
                    l+=1
                    continue;
                dif = target - nums[i] - nums[l]
                j = l+1
                k = n-1
                while j < k:
                    s = nums[j]+nums[k]
                    if s == dif:
                        ret.append([nums[i],nums[l],nums[j],nums[k]]) 
                        j+=1
                        k-=1
                        while j < k and nums[j] == nums[j-1]:
                            j+=1
                        while j<k and nums[k] == nums[k+1]:
                            k-=1
                    elif s > dif:
                        k-=1
                    else:
                        j+=1
                
                l+=1
            
            i+=1
        return ret