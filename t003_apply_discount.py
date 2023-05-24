def apply_discount(price):
  if price >= 300:
    discount = 0.3
  elif price >= 200:
    discount = 0.2
  elif price >= 100:
    discount = 0.1
  elif price < 0:
    discount = 0
  else:
    discount = 0.05

  discounted_price = price - (price * discount)
  return discounted_price


price = 350
discounted_price = apply_discount(price)
print("Discounted Price:", discounted_price)
