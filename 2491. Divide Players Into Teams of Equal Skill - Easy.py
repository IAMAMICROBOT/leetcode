class Solution:
    def dividePlayers(self, skill: List[int]) -> int:
        skill.sort()
        res=[]
        sums=[]
        j=len(skill)-1
        for i in range(len(skill)//2):
            res.append([skill[i],skill[j]])
            sums.append(skill[i]+skill[j])
            j-=1
        if len(set(sums))==1:
            for i in range(len(res)):
                res[i]=res[i][0]*res[i][1]
            return sum(res)
        return -1
