#4 Median of Two Sorted Arrays / 88ms/ 95.29%
class Solution:
    # @return a float
     
    def getMedian(self, A, B, k):
        # return kth smallest number of arrays A and B, assume len(A) <= len(B)
        lenA = len(A); lenB = len(B)
        if lenA > lenB: return self.getMedian(B, A, k)
        if lenA == 0: return B[k-1]
        if k == 1: return min(A[0], B[0])
        pa = min(k/2, lenA); pb = k - pa
        return self.getMedian(A[pa:], B, k - pa) if A[pa - 1] <= B[pb - 1] else self.getMedian(A, B[pb:], k - pb)
     
    def findMedianSortedArrays(self, A, B):
        lenA = len(A); lenB = len(B)
        if (lenA + lenB) % 2 == 1: 
            return self.getMedian(A, B, (lenA + lenB) / 2 + 1)
        else:
            return 0.5 * ( self.getMedian(A, B, (lenA + lenB) / 2) + self.getMedian(A, B, (lenA + lenB) / 2 + 1) )