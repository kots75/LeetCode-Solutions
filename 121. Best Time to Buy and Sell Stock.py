#sol from long video
def maxProfit(prices):
    l, r = 0,1
    maxProfit = 0

    while r < len(prices):
      if prices[l] < prices[r]:
        profit = prices[r] - prices[l]
        maxProfit = max(profit, maxProfit)
      else:
        l = r
      r += 1
    return maxProfit

#optimized sol from short
# def maxProfit(prices):
#     profit = 0
#     buy = prices[0]
    
#     for p in prices:
#       buy = min(buy, p)
#       profit = max(profit, p - buy)
#     return profit


prices = [7,1,5,3,6,4]
print(maxProfit(prices))