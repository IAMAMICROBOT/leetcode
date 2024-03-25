class Solution:
    def trailingZeroes(self, n: int) -> int:
        res=1
        while n>0:
            res*=n
            n-=1
        c=0
        while res%10==0:
            c+=1
            res//=10
        return c

