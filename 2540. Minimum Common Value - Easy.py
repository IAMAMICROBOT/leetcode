class Solution:
    def getCommon(self, nums1: List[int], nums2: List[int]) -> int:
        nums1[:len(nums1)+len(nums2)]=list(set(nums1))+list(set(nums2))
        nums1.sort()
        for i in range(len(nums1)):
            if i+1<len(nums1) and nums1[i]==nums1[i+1]:
                return(nums1[i])
        return -1
