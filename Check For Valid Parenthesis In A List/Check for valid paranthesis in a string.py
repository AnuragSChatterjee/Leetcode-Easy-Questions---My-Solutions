class Solution:
   def isValid(self, string):
       '''
       Function to check if sequence contains valid parenthesis
       :param sequence: Sequence of brackets
       :return: True is sequence is valid else False
       '''
       while True:
           if '()' in string:
               return ('()', '')
           elif '{}' in string:
               return ('{}', '')
           elif '[]' in string:
               return ('[]', '')
           else:
               return not string