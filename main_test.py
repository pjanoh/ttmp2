from main import find_min_price

def test():
    prices = [200, 150, 118, 211, 108, 560]
    actual = find_min_price(prices)
    expected = 108
    assert expected == actual