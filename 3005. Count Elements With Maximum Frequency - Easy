class Solution:
    def maxFrequencyElements(self, nums: List[int]) -> int:
        dic={}
        for i in nums:
            if i in dic:
                dic[i]+=1
            else:
                dic[i]=1
        h_f=0
        max_f=1
        for f in dic.values():
            if max_f<f:
                h_f=0
            if f>1 and f==max_f:
                h_f+=f
            max_f=max(max_f,f)
        if max_f==1:
            return len(nums)
        if h_f%max_f==0:
            return max_f+h_f
        return max_f
