class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        from collections import defaultdict
        graph = defaultdict(set)
        weight = defaultdict()
        lookup = {}
        # 建图
        for idx, equ in enumerate(equations):
            graph[equ[0]].add(equ[1])
            graph[equ[1]].add(equ[0])
            weight[tuple(equ)] = values[idx]
            weight[(equ[1], equ[0])] = float(1 / values[idx])

        # 深度遍历(DFS)
        def dfs(start, end, vistied):
            # 当图中有此边,直接输出
            if (start, end) in weight:
                return weight[(start, end)]
            # 图中没有这个点
            if start not in graph or end not in graph:
                return 0
            # 已经访问过
            if start in vistied:
                return 0
            vistied.add(start)
            res = 0
            for tmp in graph[start]:
                res = (dfs(tmp, end, vistied) * weight[(start, tmp)])
                # 只要遍历到有一个不是0的解就跳出
                if res != 0:
                    # 添加此边,以后访问节省时间
                    weight[(start, end)] = res
                    break
            vistied.remove(start)
            return res

        res = []
        for que in queries:
            # 用集合记录是否已经访问节点
            tmp = dfs(que[0], que[1], set())
            if tmp == 0:
                tmp = -1.0
            res.append(tmp)
        return res