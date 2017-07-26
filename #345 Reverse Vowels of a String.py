#345. Reverse Vowels of a String
class Solution(object):
    def reverseVowels(self, s):
        """
        :type s: str
        :rtype: str
        """
        if s == None:
            return ""
        
        left = 0
        right = len(s) - 1
        vowels = {'a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', "U"}
        aString = list(s)
        
        while left < right:
            while aString[left] not in vowels:
                left += 1
                if left >= right:
                    return ''.join(aString)
                
            while aString[right] not in vowels:
                right -= 1
                if right <= left:
                    return ''.join(aString)
                
            temp = aString[left]
            aString[left] = aString[right]
            aString[right] = temp
            left += 1
            right -= 1
            
        return ''.join(aString)