class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        if x == 0:
            return True
        if x > 0:
            string = str(x)
            text = r'[a-zA-Z0-9]'
            string1 = ''.join(re.findall(text, string))
        else:
            return None
        return string1.lower() == string1[::-1].lower()
        
        
