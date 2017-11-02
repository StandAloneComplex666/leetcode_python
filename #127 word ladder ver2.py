class Solution:
    # @param {string} beginWord
    # @param {string} endWord
    # @param {set<string>} wordDict
    # @return {integer}
    def ladderLength(self, beginWord, endWord, wordDict):
        from collections import defaultdict, deque
        qf = deque( [ [beginWord, 0] ] )
        qe = deque( [ [endWord, 0] ] )
        sf = { }
        se = { }
        neighbors = defaultdict(list)
        for word in wordDict:
            if endWord not in wordDict:
                return 0
        for word in wordDict:
            for x in range(len(word)):
                token = word[:x] + '_' + word[x+1:]
                neighbors[token] += word,
        while qf or qe:
            if qf:
                word, length = qf.popleft()
                if word in se :
                    return length + se[word] + 1
                for x in range(len(word)):
                    token = word[:x] + '_' + word[x+1:]
                    for ladder in neighbors[token]:
                        if ladder not in sf:
                            sf[ladder] = length + 1
                            qf += [ladder, length + 1],
            if qe:
                word, length = qe.popleft()
                if word in sf :
                    return length + sf[word] + 1
                for x in range(len(word)):
                    token = word[:x] + '_' + word[x+1:]
                    for ladder in neighbors[token]:
                        if ladder not in se:
                            se[ladder] = length + 1
                            qe += [ladder, length + 1],
        return 0
