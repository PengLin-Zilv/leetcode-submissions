class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        # check if s2 includes s1
        # if s2 contains consecutive letters in s1, then return True

        if len(s2) < len(s1):
            return False

        s1_counts = [0] * 26
        s2_window_counts = [0] *26

        for char in s1:
            s1_counts[ord(char) - ord("a")] += 1
        for char in s2[:len(s1)]:
            # initialize the first window
            s2_window_counts[ord(char) - ord("a")] += 1

        for i in range(len(s2) - len(s1) + 1):
            if s1_counts == s2_window_counts:
                return True
            # if doesn't match, window goes to the right, the windows leftest count -= 1 (drops the ith letter count)
            if i < len(s2) - len(s1):
                s2_window_counts[ord(s2[i]) - ord("a")] -= 1
                # the window adds a count for the new right coming one
                s2_window_counts[ord(s2[i + len(s1)]) - ord("a")] += 1
        return False
