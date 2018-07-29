class Solution:
    def maxProfit(self, prices, fee):
        """
        :type prices: List[int]
        :type fee: int
        :rtype: int
        """
        dpBuy = [0 for i in range(len(prices))]
        dpSell = [0 for i in range(len(prices))]
        
        dpBuy[0], dpSell[0] = -prices[0], 0
        
        for i in range(1,len(prices)):
            dpBuy[i] = max(dpBuy[i-1], dpSell[i-1] - prices[i])
            dpSell[i] = max(dpSell[i-1], dpBuy[i-1] + prices[i] - fee)
        return dpSell[-1]