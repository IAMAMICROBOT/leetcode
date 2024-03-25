class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        c=0
        for i in nums:
            if i==0:
                c+=1
        for i in range(c):
            nums.remove(0)
            nums.append(0)

        
