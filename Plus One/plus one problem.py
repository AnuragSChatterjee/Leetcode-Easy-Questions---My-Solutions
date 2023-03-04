class Solution(object):
    def plusOne(self, digits):
        intermediary_string = ''.join(map(str,digits))
        i = int(intermediary_string) + 1
        return list(map(int, str(i)))



      