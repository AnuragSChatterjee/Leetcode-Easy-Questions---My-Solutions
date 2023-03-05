class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n==1:
            return n

        if n==2:
            return n

        most_previous_value = 1
        previous_value = 1
        current_value = 0

        for i in range(2,n+1):
            current_value = previous_value + most_previous_value 
            most_previous_value = previous_value
            previous_value = current_value
        return current_value



