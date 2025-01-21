class Solution:
    def myPow(self, x: float, n: int) -> float:
        #iterative solution

        if x == 0:
            return 0
        if n == 0:
            return 1

        power = n

        if n<0:
            n = -n

        res = 1

        while n!=0:
            if n%2 != 0: #n is odd
                res = res*x
            x = x*x
            n = n//2

        return res if power>0 else 1/res

