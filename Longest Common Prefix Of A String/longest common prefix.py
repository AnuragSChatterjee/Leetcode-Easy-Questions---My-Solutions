class Solution(object):
   def longestCommonPrefix(self, strs):
        if len(strs) == 0:
           return ""
        if len(strs) == 1:
           return strs

        current_value = strs[0]
        for i in range(len(strs)):
            output = ""
            if len(current_value) == 0:
                return ""
            for j in range(len(strs)):
                if j < len(current_value) and current_value[j] == strs[i][j]:
                    output+=current_value[j]
                else:
                    break
            current_value = output
        return current_value