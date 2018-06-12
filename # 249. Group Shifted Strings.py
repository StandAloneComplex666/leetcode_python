class Solution:
    def groupStrings(self, strings):
        """
        :type strings: List[str]
        :rtype: List[List[str]]
        """
        dic = {}
        for string in strings:
            key = tuple((ord(char) - ord(string[0])) % 26 for char in string)
            print(key)
            if key in dic:
                dic[key].append(string)
            else:
                dic[key] = [string]
        return [value for _, value in dic.items()]