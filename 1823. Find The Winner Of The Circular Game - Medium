class Solution:
    def findTheWinner(self, n: int, k: int) -> int:
        def win(n,k):
            res=0
            for i in range(2,n+1):
                res=(res+k)%i
            return(res)
        return(win(n,k)+1)
        
