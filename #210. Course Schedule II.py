#210. Course Schedule II
class Solution(object):
    def findOrder(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: List[int]
        """
        matrix = [[] for _ in xrange(numCourses)]
        indegree = [0 for _ in xrange(numCourses)]
        que = collections.deque()
        res = []
        
        for course, pre in prerequisites:
            indegree[course] += 1
            matrix[pre].append(course)
        
        for i in xrange(numCourses):
            if indegree[i] == 0:
                que.appendleft(i)
        count = 0
        while que:
            temp = que.pop()
            res.append(temp)
            count += 1
            for course in matrix[temp]:
                indegree[course] -= 1
                if indegree[course] == 0:
                    que.appendleft(course)
        return res if count == numCourses else []  