class Solution:
    def reverseWords(self, s: str) -> str:
        l=s.split()
        res=""
        for i in range(len(l)-1,-1,-1):
            res+=l[i]+" "
        return res.rstrip()
