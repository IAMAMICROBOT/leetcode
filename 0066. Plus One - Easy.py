class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        res=''
        resl=[]
        for i in digits:
            res+=str(i)
        res=int(res)
        res+=1
        while res>0:
            resl.append(res%10)
            res//=10
        return resl[::-1]
