prices = [1000, 2500, 5000, 800, 12000]
discounted_prices = []
discount_percent = 20

for price in prices:
    new_price = price * (1 - discount_percent / 100)
    discounted_prices.append(int(new_price))

print(f"Հին գներ. {prices}")
print(f"Զեղչված գներ (20%). {discounted_prices}")
