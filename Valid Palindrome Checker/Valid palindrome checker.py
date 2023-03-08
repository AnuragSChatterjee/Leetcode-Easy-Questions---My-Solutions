import re
class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        text = r'[a-zA-Z0-9]'
        s = ''.join(re.findall(text, s))
        return s.lower() == s[::-1].lower()