#30. Substring with Concatenation of All Words
class Solution:
    # @param S, a string
    # @param L, a list of string
    # @return a list of integer
    def findSubstring(self, S, L):
        words={}
        wordNum=len(L)
        for i in L:
            if i not in words:
                words[i]=1
            else:
                words[i]+=1
        wordLen=len(L[0])
        res=[]
        for i in range(len(S)+1-wordLen*wordNum):
            curr={}; j=0
            while j<wordNum:
                word=S[i+j*wordLen:i+j*wordLen+wordLen]
                if word not in words: 
                    break
                if word not in curr: 
                    curr[word]=1
                else:
                    curr[word]+=1
                if curr[word]>words[word]: break
                j+=1
            if j==wordNum: res.append(i)
        return res

#fastest version:
class Solution(object):
    def findSubstring(self, s, words):
        """
        :type s: str
        :type words: List[str]
        :rtype: List[int]
        """
        from collections import deque
        result = []
        if len(words) == 0:
            return result
        wordLen = len(words[0])
        wordDict = dict()
        for word in words:
            wordDict[word] = wordDict.get(word, 0) + 1    
    
        for i in range(wordLen):        
            start = i
            current = start
            wordUsed = deque(maxlen=len(words))
            while current <= len(s)-(len(words)-len(wordUsed))*wordLen:
                currentWord = s[current:current+wordLen]
                if currentWord not in wordDict:
                    while wordUsed:
                        wordDict[wordUsed.popleft()] += 1
                    start = current + wordLen
                    current = start
                elif wordDict[currentWord] == 0:
                    while wordUsed[0] != currentWord:
                        wordDict[wordUsed.popleft()] += 1
                        start += wordLen
                    wordUsed.popleft()
                    wordUsed.append(currentWord)
                    start += wordLen
                    current += wordLen
                else:                
                    wordUsed.append(currentWord)
                    wordDict[currentWord] -= 1
                    current += wordLen
                    if len(wordUsed) == len(words):
                        result.append(start)
                        wordDict[wordUsed.popleft()] += 1
                        start += wordLen
            while wordUsed:
                wordDict[wordUsed.popleft()] += 1
        return sorted(result)