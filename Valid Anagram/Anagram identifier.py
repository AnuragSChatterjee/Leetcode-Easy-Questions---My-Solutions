class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        string1 = s.lower()
        string2 = t.lower()

        sortedstring1 = sorted(string1)
        sortedstring2 = sorted(string2)

        if sortedstring1 == sortedstring2:
            return True
        else:
            return False
        