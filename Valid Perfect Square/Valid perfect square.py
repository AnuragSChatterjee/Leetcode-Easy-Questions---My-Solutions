from math import sqrt
class Solution(object):
    def isPerfectSquare(self, num):
        """
        :type num: int
        :rtype: bool
        """
        if num > 0:
            squareroot = int(sqrt(num))
            return squareroot * squareroot == num
        else:
            return False
            
