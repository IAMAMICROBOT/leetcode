class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        for i in range(21):
            if n==3**i:
                return True
        return False
