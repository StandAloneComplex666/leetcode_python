class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        data, res, pq = {}, [], []
        for i in nums:
            data[i] = data[i] + 1 if i in data else 1
        for key in data:
            heapq.heappush(pq, (-data[key], key))
        for i in xrange(k):
            res.append(heapq.heappop(pq)[1])
        return res