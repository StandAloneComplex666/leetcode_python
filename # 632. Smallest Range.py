# 632. Smallest Range
class Solution(object):
    def smallestRange(self, nums):
        """
        :type nums: List[List[int]]
        :rtype: List[int]
        """
        pq = [(row[0], i, 0) for i, row in enumerate(nums)]
        heapq.heapify(pq)

        ans = -1e9, 1e9
        right = max(row[0] for row in nums)
        while pq:
            left, i, j = heapq.heappop(pq)
            if right - left < ans[1] - ans[0]:
                ans = left, right
            if j + 1 == len(nums[i]):
                return ans
            v = nums[i][j+1]
            right = max(right, v)
            heapq.heappush(pq, (v, i, j+1))  

class Solution(object):
    def smallestRange(self, nums):
        """
        :type nums: List[List[int]]
        :rtype: List[int]
        """
        dmap = collections.defaultdict(set)
        cover = collections.defaultdict(set)
        nsize = len(nums)
        
        for idx, nlist in enumerate(nums):
            for num in nlist:
                dmap[num].add(idx)
        snum = sorted(set(n for nlist in nums for n in nlist))
        ssize = len(snum)

        start = end = 0
        ans = [snum[0], snum[-1]]
        gap = 0x7FFFFFFF
        while start < ssize and end < ssize:
            while end < ssize and len(cover) < nsize:
                for idx in dmap[snum[end]]:
                    cover[idx].add(snum[end])
                end += 1
            while start < ssize and len(cover) == nsize:
                if len(cover) == nsize and snum[end - 1] - snum[start] < gap:
                    gap = snum[end - 1] - snum[start]
                    ans = [snum[start], snum[end - 1]]
                for idx in dmap[snum[start]]:
                    cover[idx].remove(snum[start])
                    if not cover[idx]: del cover[idx]
                start += 1
        return ans