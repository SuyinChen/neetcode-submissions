class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = ''.join(filter(str.isalnum, s))
        s = s.lower()
        print(s)
        for i in range(len(s)):
            if s[i] != s[-1-i]:
                return False
            else:
                i += 1
        return True