'''
    First get the key of a string by transfering it
     to the relative position of its first character.
    Then the strings who belongs to the same group will have the same key.
    Use hashmap to store them and then output.
'''
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