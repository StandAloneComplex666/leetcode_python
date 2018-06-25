class vertex(object):
    def __init__(self, name):
        self.name = name
        self.adjs = []
        self.visited = set()

class Solution(object):
    def findItinerary(self, tickets):
        """
        :type tickets: List[List[str]]
        :rtype: List[str]
        """
        ver_dict = {}
        for ticket in tickets:
                src, dst = ticket[0], ticket[1]
                if src not in ver_dict:
                    ver_dict[src] = vertex(src)
                if dst not in ver_dict:
                    ver_dict[dst] = vertex(dst)
                ver_dict[src].adjs.append(ver_dict[dst])

        for ver in ver_dict.values():
            ver.adjs.sort(key=lambda x: x.name)

        trip_len = len(tickets) + 1
        trip_path = []

        self.dfs(ver_dict['JFK'], ver_dict, trip_len, trip_path)

        return trip_path

    def dfs(self, ver_src, ver_dict, trip_len, trip_path):
        trip_path.append(ver_src.name)
        
        if len(trip_path) == trip_len:
            return True

        neighbers = ver_src.adjs
        for idx, nei in enumerate(neighbers):
            if idx not in ver_src.visited:
                ver_src.visited.add(idx)
                if self.dfs(nei, ver_dict, trip_len, trip_path):
                    return True
                ver_src.visited.remove(idx)

        trip_path.pop()