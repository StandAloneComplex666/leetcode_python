#922 ms / 38.76%
import collections
class Solution:
    # @param start, a string
    # @param end, a string
    # @param dict, a set of string
    # @return an integer
    def ladderLength(self, start, end, wordList):
        wordSet = set([])
        for word in wordList:
            wordSet.add(word)

        wordLen = len(start)
        queue = collections.deque([(start, 1)])
        while queue:
            currWord, currLen = queue.popleft()
            if currWord == end:
                return currLen
            for i in xrange(wordLen):
                part1 = currWord[:i]
                part2 = currWord[i+1:]
                for j in 'abcdefghijklmnopqrstuvwxyz':
                    if currWord[i] != j:
                        nextWord = part1 + j + part2
                        if nextWord in wordSet:
                            queue.append((nextWord, currLen + 1))
                            wordSet.remove(nextWord)
        return 0
