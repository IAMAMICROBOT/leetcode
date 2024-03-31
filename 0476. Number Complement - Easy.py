class Solution:
    def findComplement(self, num: int) -> int:
        res=bin(num)[2:]
        res1=""
        for i in range(len(res)):
            if res[i]=='0':
                res1+='1'
            else:
                res1+='0'
        return int(res1,2)
