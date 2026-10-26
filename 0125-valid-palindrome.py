class Solution:
    def isPalindrome(self, s: str) -> bool:
        # s is a palindrome if it reads same forward and backward
        # after:
        # 1)converting all uppercase letters into lowercase letters 
        # 2)and removing all non-alphanumeric characters

        # given s, return true if it is palindrome
        # return False otherwise

        # we want to use two pointers, compare s[l] and s[r], each time narrow l+=1, r-=1 if same
        # they should skip non alphanumeric characters

        # not valid palindrome if l and r are not same:
        # but skip the non alphanumeric chars

        l = 0
        r = len(s) - 1
        # "A man, a plan, a canal: Panama"

        while l < r:
            if not s[l].isalnum():
                l += 1
                continue
            if not s[r].isalnum():
                r -= 1
                continue
            if s[l].lower() != s[r].lower():
                return False
            l += 1
            r -= 1
        return True

            
