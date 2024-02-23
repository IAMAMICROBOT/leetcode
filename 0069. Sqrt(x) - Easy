class Solution:
    def mySqrt(self, x: int) -> int:
        
        i = 0
        j = x
        res = i
        while(i<=j):
            mid = i+(j-i)//2
            if mid**2 == x:
                return mid
            if mid**2 < x:
                res = mid
                i = mid+1
            else:
                j = mid-1
        return res
