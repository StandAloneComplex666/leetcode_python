class Solution(object):
    def validTree(self, n, edges):
        """
        :type n: int
        :type edges: List[List[int]]
        :rtype: bool
        """
        # BFS solution 
        dic = {}
        if len(edges) == 0:
            if n > 1:
                return False 
            else:
                return True
        
        # create adjacency list 
        for edge in edges:
            if edge[0] in dic:
                dic[edge[0]].append(edge[1])
            else:
                dic[edge[0]] = [edge[1]]
        
            if edge[1] in dic:
                dic[edge[1]].append(edge[0])
            else:
                dic[edge[1]] = [edge[0]]
        
        # store visited vertex as key and its parent as value
        visited = {}
        def dfs(vertex, parent):
            visited[vertex] = parent
            for adjvertex in dic[vertex]:
						    ## if found any adjvertex which is already seen before and that vertex is not a parent of 
								##current vertex, then this is s a cycle
                if adjvertex in visited and adjvertex != parent:
                    return False
                else:
                    if adjvertex != parent:
                        dfs(adjvertex, vertex)      
            return True
        
        if not dfs(edges[0][0], edges[0][0]):
            return False
            
        for i in range(n):
            if i not in visited:
                #print("not connected vertex {}".format(i))
                return False
            
        return True