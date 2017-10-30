'''
Reverse digits of an integer.

Example1: x = 123, return 321
Example2: x = -123, return -321
'''
class Solution(object):
    def reverse(self, x):
        if x>0:
            flag = 1
        else:
            flag = -1
        x = x*flag
        result = 0
        while x:
            result = result*10+x%10
            x = x/10
        if result > 2147483647:
            return 0
        else:
            return result*flag
'''
        :type x: int
        :rtype: int
'''    
