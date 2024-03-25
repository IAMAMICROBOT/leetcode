class Solution:
    def findLeastNumOfUniqueInts(self, arr: List[int], k: int) -> int:
        dict=collections.Counter(arr)
        sortd = sorted(dict.values(),reverse=True)
        while k>0:
            p=sortd.pop()
            if k-p>=0:
                k-=p
            else:
                sortd.append(p)
                break
        return len(sortd)
