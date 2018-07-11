class Solution:
    def repeatedStringMatch(self, A, B):
        count = 1
        tmp = A
        max_count = (len(B) / len(A)) + 1
        while not(B in tmp):
            tmp = tmp + A
            if (count > max_count):
                count = -1
                break
            count = count + 1

        return count