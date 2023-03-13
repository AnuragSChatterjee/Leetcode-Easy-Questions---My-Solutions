class Solution(object):
    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: int
        """
        for i in range(len(s)):
            if s[i] not in s[i+1]:
                return s.index(s[i])
            else:
                return -1
        
