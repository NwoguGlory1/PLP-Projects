def calculate_discount(price, discount_percent):
    """calculates  the final price after applying a discount. """
    final_price =   price - (discount_percent * price)

    if discount_percent >= 0.2:
        calculate_discount()
    else:
        return price