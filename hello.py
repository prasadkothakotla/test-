def calculate_discount(price, discount):
    if discount < 0 or discount > 100:
        raise ValueError("Invalid discount")

    return price * (1 - discount / 100)


price = 100
discount = 20

print(calculate_discount(price, discount))

print(price/0)
