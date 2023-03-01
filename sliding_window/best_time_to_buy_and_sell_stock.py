class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit = 0

        current_price = None
        for price in prices:
            if current_price == None:
                current_price = price
            elif current_price < price:
                max_profit = max(max_profit, price - current_price)
            else:
                current_price = price
        
        return max_profit