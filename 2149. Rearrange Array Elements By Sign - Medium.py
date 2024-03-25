class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:    
        p=[]
        n=[]
        res=[]
        for i in nums:
            if i<0:
                n.append(i)
            else:
                p.append(i)
        for i in range(int(len(nums)/2)):
            res.append(p[i])
            res.append(n[i])

        return res
