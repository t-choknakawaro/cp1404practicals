total_price = 0
number_of_items = int(input('Number of items: '))
for i in range(number_of_items):
    price_of_item = float(input('Price of item: '))
    total_price += price_of_item
if total_price > 100:
    discount = total_price * 0.10
    total_price = total_price - discount
else:
    pass
print('Total price for {} items is ${:.2f}'.format(number_of_items, total_price))