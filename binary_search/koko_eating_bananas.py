class Solution:  
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        res = max(piles)
        l, r = 1, max(piles)

        while l <= r:
            k = (l + r) // 2
            
            total_hours = 0
            for pile in piles:
                total_hours += math.ceil(pile / k)
            
            if total_hours <= h:
                res = min(res, k)
                r = k - 1
            else:
                l = k + 1

        return res