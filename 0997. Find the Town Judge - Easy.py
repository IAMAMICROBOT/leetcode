class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        if n==1:
            return n
        trustworthy=[0]*(n+1)
        for p,j in trust:
            trustworthy[p]-=1
            trustworthy[j]+=1
        for i in range(len(trustworthy)):
            if trustworthy[i]==n-1:
                return i
        return -1
