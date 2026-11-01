class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        # given s, given k
        # we can change any k char to other uppercase english char
        # return the length of longest substring containing the same letter

        # maintain a window

        l = 0
        count = {}
        maxf = 0
        res = 0
        # "ABAB"
        for r in range(len(s)):
            count[s[r]] = count.get(s[r], 0) + 1
            maxf = max(maxf, count[s[r]])
            while r - l + 1 - maxf > k:
                count[s[l]] -= 1
                l += 1
            res = max(res, r-l+1)
        return res