class Solution:
    def shiftingLetters(self, S, shifts):
        """
        :type S: str
        :type shifts: List[int]
        :rtype: str
        """
        shifted_letters = [None for _ in S]
        current_sum = 0
        for i in range(len(shifts)-1, -1, -1):
            current_sum += shifts[i]
            shifted_letters[i] = Solution.shift_char(S[i], current_sum)
        return ''.join(shifted_letters)

    @staticmethod
    def shift_char(char, distance):
        distance %= 26
        new_ord = ord(char) + distance
        if new_ord > ord('z'):
            new_ord -= 26
        return chr(new_ord)