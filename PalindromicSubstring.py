class PalindromicSubstring:
    def isPalindrome(self,s):
        if s == s[::-1] :
            return True
        else :
            return False
        
    def longestPalindrome(self, s):
        if len(s) == 0 : return ""
        returnS = ""
        if self.isPalindrome(s): return s
        for i in range(len(s)):
            x = len(s)
            while x > 0:
                if self.isPalindrome(s[i:x]) and len(s[i:x]) > len(returnS):
                    returnS = s[i:x]
                x -= 1
        return returnS
