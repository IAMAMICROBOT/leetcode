class Solution:
    def furthestBuilding(self, height: List[int], bricks: int, ladders: int) -> int:
        ldiff=[]
        for i in range(len(height)):
            if i+1<len(height) and height[i+1]-height[i]>0:
                heapq.heappush(ldiff,height[i+1]-height[i])
                if len(ldiff)>ladders:
                    bricks-=heapq.heappop(ldiff)
                if bricks<0:
                    return(i)
            else:
                continue
        return(len(height)-1)
