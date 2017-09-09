#383. Ransom Note
class Solution(object):
    def canConstruct(self, ransomNote, magazine):
        """
        :type ransomNote: str
        :type magazine: str
        :rtype: bool
        """
        cnt = collections.Counter(magazine)
        for letter in ransomNote:
            cnt[letter] -= 1
            if cnt[letter] <0: return False
        return True
