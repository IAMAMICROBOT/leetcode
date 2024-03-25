class Solution:
    def firstUniqChar(self, s: str) -> int:
        f=defaultdict(int)
        for i in s:
                f[i]+=1
        for i, char in enumerate(s):
            if f[char] == 1:
                return i
        return -1
