import re
from collections import Counter

def main():
    
    # Read the CSV file with the product orders
    with open('orders.csv') as f_in:
        text = f_in.read()

    # 1. Extract all order numbers from the text.
    order_numbers = re.findall(r'Order #(\d+)', text)
    print("Order Numbers:", order_numbers)

    # 2. Extract all product names.
    product_names = re.findall(r'\b[A-Z][a-zA-Z]+\b', text)
    print("Product Names:", product_names)

    # 3. Extract all prices.
    prices = re.findall(r'\$\d+\.\d{2}', text)
    print("Prices:", prices)

    # 4. Extract all order dates.
    dates = re.findall(r'\b\d{4}-\d{2}-\d{2}\b', text)
    print("Order Dates:", dates)

    # 5. Find all orders for products priced over $500. (You are allowed to use Python to filter the list.)
    expensive_orders = [price for price in prices if float(price[1:]) > 500]
    print("Expensive Orders (over $500):", expensive_orders)

    # 6. Change the date format to DD/MM/YYYY. (Note the re.sub() method)
    formatted_dates = [re.sub(r'(\d{4})-(\d{2})-(\d{2})', r'\3/\2/\1', date) for date in dates]
    print("Formatted Dates (DD/MM/YYYY):", formatted_dates)

    # 7. Extract product names that have more than 6 characters.
    long_product_names = [name for name in product_names if len(name) > 6]
    print("Product Names with more than 6 characters:", long_product_names)

    # 8. Count the occurrence of each product in the text. (You may want to use the Counter class from the collections package.)
    product_counts = Counter(product_names)
    print("Product Counts:", product_counts)

    # 9. Extract the orders with prices ending in .99.
    prices_ending_in_99 = [price for price in prices if price.endswith('.99')]
    print("Prices ending in .99:", prices_ending_in_99)

    # 10. Find the cheapest product. (You may want to use Python's min() method.)
    cheapest_price = min([float(price[1:]) for price in prices])
    print("Cheapest Product Price:", f"${cheapest_price:.2f}")

if __name__ == '__main__':
    main()
