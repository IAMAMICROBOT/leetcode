class Solution:
    def addBinary(self, a: str, b: str) -> str:
        A,B=0,0
        for i in range(len(a)):
            if a[::-1][i]=='1':
                A=A+(2**i)
        for j in range(len(b)):
            if b[::-1][j]=='1':
                B=B+(2**j)
        return(bin(A+B)[2:])
