#49 group anagrams/242ms/53.37%
class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        map = {}
        for i, v in enumerate(strs):
            target = "".join(sorted(v))
            if target not in map:
                map[target]=[v]
            else:
                map[target].append(v)

        result = []
        for value in map.values():
            result += [sorted(value)]
        return result