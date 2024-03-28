class Solution:
    def maxSubarrayLength(self, nums: List[int], k: int) -> int:
        freq=defaultdict(int)
        n=len(nums)
        res=1
        i=j=0
        while i<n and j<n:
            freq[nums[j]]+=1
            while freq[nums[j]]>k:
                freq[nums[i]]-=1
                i+=1
            res=max(res,j-i+1)
            j+=1
        return res
