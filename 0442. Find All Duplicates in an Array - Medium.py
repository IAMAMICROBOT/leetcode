class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        res=[]
        temp=set()
        for i in nums:
            if i in temp:
                res.append(i)
            else:
                temp.add(i)
        return res
