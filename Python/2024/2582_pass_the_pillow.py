class Solution:
    def passThePillow(self, n: int, time: int) -> int:
        
        if n > time:
             return time+1
        
        numOfRun = time % (n-1)

####
sol = Solution()

print((9/4).is_integer())
print((9%4))
