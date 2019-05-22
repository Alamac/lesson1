my_price = 200
my_discount = 5



def discounted(price, discount, max_discount=50):
    price = abs(float(price))
    discount = abs(float(discount))
    max_discount = abs(float(max_discount))
    if max_discount > 99:
        raise ValueError('Discount can\'t be more than 99%')
    if discount >= max_discount:
        price_with_discount = price
    else:
        price_with_discount = price - price * discount / 100
    return(price_with_discount)


product = {
    'name': 'Iphone XS',
    'stock': 22,
    'price': 65000,
    'phones': ['iphone', 'samsung', 'oneplus'],
    'discount': 120
}

product['price_with_discount'] = discounted(product['price'], product['discount'], max_discount=120)

print(product)