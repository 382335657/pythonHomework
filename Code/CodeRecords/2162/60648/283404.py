from decimal import Decimal
class Solution(object):
    def myPow(self, x, n):
        """
        :type x: float
        :type n: int
        :rtype: float
        """
        def func(x, n):
            if n == 0:
                return 1
            if x == 0:
                return 0
            temp = func(x, n >> 1)
            if n & 1: # n为奇数
                return temp * temp * x
            else: # n为偶数
                return temp * temp
        if n >= 0:
            res = func(x, n)
        else:
            res = 1 / func(x, -n) 
        return res

    def myPow_2(self, x, n):
        """
        :type x: float
        :type n: int
        :rtype: float
        """
        def func(x, n):
            product = 1
            for _ in range(n):
                product *= x
            return product
        if n >= 0:
            res = func(x, n)
        else:
            res = 1 / func(x, -n)
        return res


if __name__=="__main__":
    x=Decimal(input())
    n=int(input())
    r=Solution().myPow(x,n)
    print(r)