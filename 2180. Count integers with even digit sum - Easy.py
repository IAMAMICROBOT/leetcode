class Solution:
    def countEven(self, num: int) -> int:
        def ds(i):
            r=0
            for j in str(i):
                r+=(int(j))
            return r
        c=0
        for i in range(num,0,-1):
                if ds(i)%2==0: 
                    c+=1
        return c
        
