def find_min_price(prices):
    min_price = prices[0]
    for price in prices:
        if price < min_price:
            min_price = price
    return min_price
