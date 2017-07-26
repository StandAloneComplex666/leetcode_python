#58 length of last word
class Solution:  
    # @param s, a string  
    # @return an integer  
    def lengthOfLastWord(self, s):  
        i = len(s) - 1  
          
        while i >= 0 and s[i] == ' ':  
            i -= 1  
          
        length = 0  
        while i >= 0 and s[i] != ' ':  
            length += 1  
            i -= 1  
          
        return length  