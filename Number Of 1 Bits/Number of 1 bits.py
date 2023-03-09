class Solution(object):
    def hammingWeight(self, n):
        """
        :type n: int
        :rtype: int
        """
        binary_converter = bin(n)
        string_converter = str(binary_converter)
        return sum(map(lambda x: 1 if "1" in x else 0, string_converter))