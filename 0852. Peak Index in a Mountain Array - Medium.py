class Solution:
    def peakIndexInMountainArray(self, nums: List[int]) -> int:
        f=0
        l=len(nums)-1

        while f<=l:
            mid=(f+l)//2
            if nums[mid] < nums[mid+1]:
                f=mid+1
            else:
                res=mid
                l=mid-1
        return res
