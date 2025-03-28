# 121. Best Time to Buy and Sell Stock

# You are given an array pricesList where prices[i] is the price of a given stock on the ith day.
# You want to maximize your profit by choosing a single day to buy one stock and choosing a different day in the future to sell that stock.
# Return the maximum profit you can achieve from this transaction. If you cannot achieve any profit, return 0.

prices1 = [7,1,5,3,6,4] #Output: 5
prices2 = [7,6,4,3,1] #Output: 0

def maxProfit(pricesList):
    # profit = buy - sell
    bought = pricesList[0] # buys on the first day
    maxProfit = 0

    for price in pricesList:
        curProfit = 0
        if price < bought: # checks if current price is smaller than previously bought, so we could buy at better price
            bought = price
            print("updates bought to:", bought)
            continue # continues the loop since we can`t buy and sell on the same day

        if price - bought > 0:
            curProfit = price - bought
            print(f"curProfit:{curProfit}, maxProfit:{maxProfit}")
            maxProfit = max(maxProfit,curProfit)

    return maxProfit


print(maxProfit(prices2))