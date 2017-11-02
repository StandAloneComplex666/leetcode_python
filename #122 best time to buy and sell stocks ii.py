class Solution:  
    # @param prices, a list of integer  
    # @return an integer  
    def maxProfit(self, prices):  
        profit = 0  
        length = len(prices)  
        for i in range(0,length-1):  
            if prices[i+1] > prices[i]:  
                profit += prices[i+1] - prices[i]  
        return profit  
