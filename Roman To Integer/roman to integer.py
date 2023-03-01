def romantointeger(S):
    if S == "I":
        return 1
    if S == "V":
        return 5
    if S == "X":
        return 10
    if S == "L":
        return 50
    if S == "C":
        return 100
    if S == "D":
        return 500
    if S == "M":
        return 1000
    return -1

class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
    output_result = 0
    for i in range(len(s)):
        current_value = romantointeger(S[i])
        for j in range(i+1, len(s)):
            next_value = romantointeger(S[i+1])
            if current_value >= next_value:
                output_result += current_value
		    i += 1 
            if current_value < next_value:
                output_result += next_value - current_value
                i += 1
            else:
                output_result += current_value
    return output_value


