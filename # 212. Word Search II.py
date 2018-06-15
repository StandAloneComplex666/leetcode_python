class TrieNode():
    def __init__(self):
        self.children = {}
        self.string = ''

class Solution:
    def findWords(self, board, words):
        """
        :type board: List[List[str]]
        :type words: List[str]
        :rtype: List[str]
        """
        root = TrieNode()
        for word in words:
            node = root
            for s in word:
                if s not in node.children:
                    node.children[s] = TrieNode()
                node = node.children[s]
            node.string = word
        
        def dfs(i,j, node):
            if board[i][j] not in node.children:
                return
            node = node.children[board[i][j]]
            if node.string:
                ans.append(node.string)
                node.string = ''
            tmp = board[i][j]
            board[i][j] = '#'
            for a, b in [(i-1, j),(i+1, j),(i,j-1),(i, j+1)]:
                if 0 <= a < len(board) and 0 <= b < len(board[0]) and board[a][b] in node.children:
                    dfs(a, b, node)
            board[i][j] = tmp
            return 
        
        ans = []
        for i in range (len(board)):
            for j in range (len(board[0])):
                dfs(i,j, root)
        return ans