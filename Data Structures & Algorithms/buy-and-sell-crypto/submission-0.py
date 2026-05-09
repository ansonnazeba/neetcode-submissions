class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if len(prices) == 1:
            return 0

        min_price = prices[0]
        max_diff = 0

        for i in range(1, len(prices)):
            if prices[i] > min_price:
                max_diff = max(prices[i] - min_price, max_diff)
            else:
                min_price = min(prices[i], min_price)
            

        return max_diff

            

        