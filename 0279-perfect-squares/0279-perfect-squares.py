class Solution:
    def numSquares(self, n: int) -> int:
        if int(math.isqrt(n))**2==n:
            return 1
        for i in range (1,int(math.sqrt(n))+1):
            if int(math.isqrt(n-i*i))**2==n-i*i:
                return 2
        while n%4==0:
            n//=4
        if n%8==7:
            return 4
        return 3
        