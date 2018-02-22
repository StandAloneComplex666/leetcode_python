class Solution(object):
    def getHint(self, secret, guess):
        """
        :type secret: str
        :type guess: str
        :rtype: str
        """
        l = len(guess)
        bull = 0
        cow = 0
        letter_bull = {}.fromkeys(set(secret),0)
        letter_cow_guess = {}.fromkeys(set(secret),0)
        letter_cow_secret = {}.fromkeys(set(secret),0)
        for i in range(l):
            if secret[i] == guess[i]:
                bull += 1
                letter_bull[secret[i]] += 1
            if guess[i] in secret:
                letter_cow_guess[guess[i]] += 1
            letter_cow_secret[secret[i]] += 1
        for key in letter_bull:
            temp = min(letter_cow_secret[key], letter_cow_guess[key]) - letter_bull[key]
            if temp >= 0:
                cow += temp
        res = str(bull) + "A" + str(cow) + "B"
        return res