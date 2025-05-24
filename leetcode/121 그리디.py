class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_price = 1e9
        max_profit = 0

        for price in prices:
            if price < min_price:
                min_price = price  # 최소값 갱신
            else:
                profit = price - min_price
                if profit > max_profit:
                    max_profit = profit  # 최대 이익 갱신

        return max_profit
    
