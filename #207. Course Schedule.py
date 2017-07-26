# 207. Course Schedule
# fastest version:
class Solution(object):
    def canFinish(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: bool
        """
        graph=[[] for _ in range(numCourses)]
        visited=[0 for _ in range(numCourses)]
        for x,y in prerequisites:
            graph[x].append(y)
        for i in range(numCourses):
            if not self.DF(i,graph,visited):
                return False
        return True
    
    def DF(self,i,graph,visited):
        if visited[i]==1:       #visited
            return True
        elif visited[i]==-1:    #be visiting
            return False        #closed loop
        else:
            visited[i]=-1
            for j in graph[i]:
                if not self.DF(j,graph,visited):
                    return False
            visited[i]=1
            return True
# my version: very slow .still thinking about why it is so slow
class Solution:
    # @param {integer} numCourses
    # @param {integer[][]} prerequisites
    # @return {boolean}
    def canFinish(self, numCourses, prerequisites):
        if numCourses<2 or len(prerequisites)<2:
            return True
        #prerequisites.sort()
        while True:
            count=0
            mark = [True]*numCourses
            for pre in prerequisites:
                mark[pre[0]] = False
            for pre in prerequisites:
                if mark[pre[1]]:
                    count+=1
                    prerequisites.remove(pre)
            if prerequisites==[]:
                return True
            elif count==0:
                return False
