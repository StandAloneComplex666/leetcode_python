class Solution:
    def topKFrequent(self, words, k):
        """
        :type words: List[str]
        :type k: int
        :rtype: List[str]
        """
        dic = collections.Counter(words)
        min_heap = [(-dic[x], x) for x in dic]
        heapq.heapify(min_heap)
        ans = []
        for _ in range(k):
            ans.append(heapq.heappop(min_heap)[1])
        return ans