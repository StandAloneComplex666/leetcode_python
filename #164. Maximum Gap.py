# 164. Maximum Gap
class Solution(object):
    def maximumGap(self, num):
        if len(num) <2:
            return 0

        # Application of Pigeonhole Principle
        max_val = max(num)
        min_val = min(num)

        # Initialize buckets
        n = len(num)
        buckets = [[] for i in range(n-1)]
        bucket_size = (max_val-min_val)/float( (n-1) )

        # Construct buckets for (n-2) numbers
        for number in num:
            if number == max_val or number == min_val:
                continue
            k = int( math.floor( (number - min_val)/bucket_size) )
            buckets[k].append(number)

        L = [] # non-empty buckets
        for b in buckets:
            if b!=[]:
                L.append( b ) 

        # According to Pigeon Principle, at least 1 bucket is empty
        # The maximum gap should be gap between 2 elements from 2 successive bucket
        # Initial max gap should be gap either between min-val and first non-empty bucket (minimum) or between max_val and last non-empty bucket
        if L==[]:
            return max_val - min_val
        max_gap = max(min(L[0])-min_val, max_val-max(L[-1]) )
        for i in range(1, len(L)):
            gap = min(L[i]) - max( L[i-1] )
            max_gap = max(max_gap, gap)
                
        return max_gap