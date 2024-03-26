class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        s=set(nums)
        for i in range(1,len(s)+1):
            if i not in s:
                return i
        return len(s) + 1
