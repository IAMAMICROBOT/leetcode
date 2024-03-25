class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        c=0
        l=0
        dic={0:-1}
        for i in range(len(nums)):
            if nums[i]==0:
                c-=1
            else:
                c+=1
            if c in dic:
                l=max(l,i-dic[c])
            else:
                dic[c]=i
        return l
        
            
