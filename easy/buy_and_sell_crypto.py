class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit = 0

        # Loop through each price from the list in order
        for i in range(len(prices)): 
            # Check if any subsequent prices are >
            for j in range(len(prices)): 
                if i >= j or prices[i] > prices[j]: 
                    continue
                else: 
                    # If a price is found to be greater, calculate the max profit and assign
                    if (prices[j] - prices[i]) > max_profit: 
                        max_profit = prices[j] - prices[i]

        return max_profit
