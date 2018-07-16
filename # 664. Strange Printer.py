'''
Let dp(i, j) be the number of turns needed to print S[i:j+1].

Note that whichever turn creates the final print of S[i], might as well be the first turn, and also there might as well only be one print, since any later prints on interval [i, k] could just be on [i+1, k].

So suppose our first print was on [i, k]. We only need to consider prints where S[i] == S[k], because we could instead take our first turn by printing up to the last printed index where S[k] == S[i] to get the same result.

Then, when trying to complete the printing of interval [i, k] (with S[i] == S[k]), the job will take the same number of turns as painting [i, k-1]. This is because it is always at least as good to print [i, k] first in one turn rather than separately.

Also, we would need to complete [k+1, j]. So in total, our candidate answer is dp(i, k-1) + dp(k+1, j). Of course, when k == i, our candidate is 1 + dp(i+1, j): we paint S[i] in one turn, then paint the rest in dp(i+1, j) turns.
'''

def strangePrinter(self, S):
    memo = {}
    def dp(i, j):
        if i > j: return 0
        if (i, j) not in memo:
            ans = dp(i+1, j) + 1
            for k in xrange(i+1, j+1):
                if S[k] == S[i]:
                    ans = min(ans, dp(i, k-1) + dp(k+1, j))
            memo[i, j] = ans
        return memo[i, j]

    return dp(0, len(S) - 1)