class Solution:
    def asteroidsDestroyed(self, mass: int, asteroids: List[int]) -> bool:
        flag=1
        asteroids.sort()
        for i in asteroids:
            if(i<=mass) :
                mass+=i
            else:
                flag=0
        if flag==0:
            return False
        else: 
            return True

