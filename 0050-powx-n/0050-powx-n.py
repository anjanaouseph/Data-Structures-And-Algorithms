class Solution:
    def myPow(self, x: float, n: int) -> float:
        def power(x,n):
            #base cases
            if x == 0:
                return 0
            if n == 0:
                return 1

            #now call recursive function
            res = power(x, n//2)
            res = res * res if n%2==0 else res * res * x
            return res

        return power(x,n) if n >=0 else 1/(power(x,-n)) #if positive n call function directly if n is negative make n positive and call the function.