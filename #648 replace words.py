#648 replace words
#fastest version
class Solution(object):
    def replaceWords(self, dict, sentence):
        """
        :type dict: List[str]
        :type sentence: str
        :rtype: str
        """
        dict2 = {}
        for item in dict:
            if len(item) == 1:
                dict2[item] = True
            else:
                if item[:2] not in dict2:
                    dict2[item[:2]] = set([item])
                else:
                    dict2[item[:2]].add(item)
        result = []
        inputSen = sentence.split(" ")
        for item in inputSen:
            if item[0] in dict2 or len(item) == 1:
                result.append(item[0])
            else:
                if item[:2] not in dict2:
                    result.append(item)
                else:
                    candidate = ""
                    l = float('inf')
                    for thing in dict2[item[:2]]:
                        if len(thing) < l and thing == item[:len(thing)]:
                            candidate = thing
                            l = len(thing)
                    if candidate == "":
                        result.append(item)
                    else:
                        result.append(candidate)
        return " ".join(result)

#my version
class TrieNode:
    def __init__(self):
        self.children = dict()
        self.isWord = False

class Trie:

    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        node = self.root
        for letter in word:
            child = node.children.get(letter)
            if child is None:
                child = TrieNode()
                node.children[letter] = child
            node = child
        node.isWord = True

    def search(self, word):
        ans = ''
        node = self.root
        for letter in word:
            node = node.children.get(letter)
            if node is None: break
            ans += letter
            if node.isWord: return ans
        return word

class Solution(object):
    def replaceWords(self, dict, sentence):
        """
        :type dict: List[str]
        :type sentence: str
        :rtype: str
        """
        trie = Trie()
        for word in dict: trie.insert(word)
        ans = []
        for word in sentence.split():
            ans.append(trie.search(word))
        return ' '.join(ans)