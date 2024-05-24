class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        f=0
        l=len(letters)-1
        res=-1
        while f<=l:
            mid=(f+l)//2
            if letters[mid] <= target:
                f=mid+1
            else:
                res=mid
                l=mid-1
        if res==-1:
            return letters[0]
        else:
            return letters[res]
        
