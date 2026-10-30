class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        already_in = set()
        length = 0

        # we keep a set to lookup is char in s is already in the set
        # if so, means repeated, delete s[l] from the set, and l+=1 until c is not in the already_in 
        # if not, add into the list

        # initialize a window
        l = 0
        
        for r in range(len(s)):
            while s[r] in already_in: 
                # if repeat, remove s[l] until no more repeat
                already_in.remove(s[l])
                l += 1
            already_in.add(s[r])
            length = max(r-l+1, length)
        return length


