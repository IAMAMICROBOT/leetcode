class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        nums3=[]
        for i in range(m):
            nums3.append(nums1[i])
        for i in range(n):
            nums3.append(nums2[i])
        nums3.sort()
        for i in range(len(nums3)):
            nums1[i]=nums3[i]
