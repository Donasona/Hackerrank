
# ✅ *Final Question (Clean & Clear English Version)*

# Aleena buys Tata Motors shares and wants to calculate her profit or loss. She keeps track of the stock price every day.

# You are given an array prices where prices[k] represents the price of a single share on the *k-th day*.

# Your task is to find the *maximum profit* she can earn by:

# * choosing *one day to buy* a share, and
# * choosing *another future day to sell* that share.

# *Important rule:* You must *buy before you sell* (i < j).

# Return the *maximum profit* possible from this single transaction.
# If it is *not possible to make any profit, return **0*.



### *Example*

# *Input:*
# prices = [109, 103, 101, 102, 106, 104, 108, 105]

# *Output:*
# 7

# *Explanation:*
# Buy on day 3 (price = 101),
# Sell on day 7 (price = 108),
# Profit = 108 − 101 = *7*.

def maxProfit(prices):
    if not prices:
        return 0

    min_price = prices[0]
    max_profit = 0

    for price in prices[1:]:
        if price < min_price:
            min_price = price  # Update minimum price seen so far
        else:
            profit = price - min_price
            if profit > max_profit:
                max_profit = profit

    return max_profit


# Example usage
prices = [109, 103, 101, 102, 106, 104, 108, 105]
print("Maximum Profit:", maxProfit(prices))
