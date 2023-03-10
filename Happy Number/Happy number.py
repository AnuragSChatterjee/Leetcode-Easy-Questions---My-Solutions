class Solution(object):
    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """
        if n<10:
            if n==1 or n==7:
                return True
            else:
                return False
        total = 0
        while n>10:
            remainder = n%10
            total += pow(remainder, 2)
            n/=10
        return isHappy(total)
            

