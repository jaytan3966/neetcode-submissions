class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = ''.join(letter.lower() for letter in s if letter.isalnum())
        return s == s[::-1]