'''
Determine whether an integer is a palindrome. Do this without extra space.
'''

class Solution(object):
    def isPalindrome(self, x):
        if x>0:
            flag = 1
        else:
            flag = -1
        x_0 = x
        x=x*flag
        result = 0
        while x:
            result = result*10+x%10
            x=x/10
        if x_0 == result:
            return True
        else:
            return False
            
        """
        :type x: int
        :rtype: bool
        """
