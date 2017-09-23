#305ms/31.88%
class Solution:
    # @param word1 & word2: Two string.
    # @return: The minimum number of steps.
    def minDistance(self, word1, word2):
        # write your code here
        len1 = len(word1)
        len2 = len(word2)
        f = [[0] * (len2 + 1) for i in range(len1 + 1)]
        for i in range(len1 + 1):
            f[i][0] = i
        for j in range(len2 + 1):
            f[0][j] = j

        for i in range(1, len1 + 1):
            for j in range(1, len2 + 1):
                if word2[j - 1] == word1[i - 1]:
                    f[i][j] = f[i - 1][j - 1]
                else:
                    f[i][j] = min(f[i - 1][j - 1], f[i - 1][j], f[i][j - 1]) + 1

        return f[len1][len2]
