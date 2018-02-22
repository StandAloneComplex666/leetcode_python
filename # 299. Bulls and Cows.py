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
#those two below are others' answer which express more clear
def getHint(self, secret, guess):
"""
:type secret: str
:type guess: str
:rtype: str
"""
secret_map, guess_map = {}, {}
bull_count, cow_count = 0, 0
for i in range(len(secret)):
    if secret[i] == guess[i]:
        bull_count += 1
    else:
        if secret[i] in secret_map:
            secret_map[secret[i]] += 1
        else:
            secret_map[secret[i]] = 1
        if guess[i] in guess_map:
            guess_map[guess[i]] += 1
        else:
            guess_map[guess[i]] = 1
for i in guess_map:
    if i in secret_map:
        cow_count += min(secret_map[i], guess_map[i])
return '%sA%sB' % (bull_count, cow_count)

def getHint(self, secret, guess):
"""
:type secret: str
:type guess: str
:rtype: str
"""
    s, g = Counter(secret), Counter(guess)
    a = sum(i == j for i, j in zip(secret, guess))
    return '%sA%sB' % (a, sum((s & g).values()) - a)