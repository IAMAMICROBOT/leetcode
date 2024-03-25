class Solution:
    def frequencySort(self, s: str) -> str:
        res = ""
        dic = {}
        
        for i in s:
            if i in dic:
                dic[i] += 1
            else:
                dic[i] = 1
        sor_d = sorted(dic.items(), key=lambda x: x[1],reverse=True)
        for i in sor_d:
            res += i[0] * i[1]
        return res
