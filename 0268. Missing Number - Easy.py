class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        array_sum=0
        n=len(nums)
        total_sum=n*(n+1)//2
        for i in nums:
            array_sum+=i
        return total_sum-array_sum
