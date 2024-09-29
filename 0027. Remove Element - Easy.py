class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        for j in range(nums.count(val)):
            nums.remove(val)
