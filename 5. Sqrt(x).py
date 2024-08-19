"""
Given a non-negative integer x, return the square root of x rounded down to the nearest integer. The returned integer should be non-negative as well.

You must not use any built-in exponent function or operator.

"""

class Solution(object):
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """
        l, r = 0, x
        result = 0

        while l <= r:
            m = (l + r) // 2
            if m * m > x:
                r = m - 1
            elif m * m < x:
                l = m + 1
                result = m
            else:
                return m
        
        return result
