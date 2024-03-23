class Solution:
    def printVertically(self, s: str) -> List[str]:
        l=s.split()
        Max=max(len(w) for w in l)
        res=['']*Max
        for w in l:
            for i in range(Max):
                if i<len(w):
                    res[i]+=w[i]
                else:
                    res[i]+=' '
        for i in range(len(res)):
            res[i]=res[i].rstrip()
            
        return res
        
