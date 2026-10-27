from math import ceil
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        # Checks if our current k works given h
        def k_works(k):
            hours = 0
            for pile in piles:
                hours += (ceil(pile / k))
            if hours > h:
                return False
            else:
                return True

        # Slowest speed is k = 1
        # Fastest speed is k = largest of all piles[i]; happens when h = len(piles)      
        l = 1
        r = 0
        for i in range(len(piles)):
            r = max(r, piles[i])
        
        while l < r:
            k = (l + r) // 2
            if k_works(k):
                r = k
            else:
                l = k + 1
        
        return l
        

        