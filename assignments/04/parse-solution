import re
from collections import Counter

def main():
    
    # Read the CSV file with the product orders
    with open('orders.csv') as f_in:
        text = f_in.read()

    # Extract all order numbers (assuming they are in the format "Order #1234")
    order_numbers = re.findall(r'Order #(\d+)', text)
    print("Order Numbers:", order_numbers)

    # Extract all product names (assuming product names are single words with a capitalized first letter)
    product_names = re.findall(r'\b[A-Z][a-zA-Z]+\b', text)
    print("Product Names:", product_names)

    # Extract all prices (assuming prices are in the format "$123.45")
    prices = re.findall(r'\$\d+\.\d{2}', text)
    print("Prices:", prices)

    # Extract all order dates (assuming dates are in format YYYY-MM-DD)
    dates = re.findall(r'\b\d{4}-\d{2}-\d{2}\b', text)
    print("Order Dates:", dates)

    # Find orders for products priced over $500
    expensive_orders = [price for price in prices if float(price[1:]) > 500]
    print("Expensive Orders (over $500):", expensive_orders)

    # Change the date format to DD/MM/YYYY
    formatted_dates = [re.sub(r'(\d{4})-(\d{2})-(\d{2})', r'\3/\2/\1', date) for date in dates]
    print("Formatted Dates (DD/MM/YYYY):", formatted_dates)

    # Extract product names that have more than 6 characters
    long_product_names = [name for name in product_names if len(name) > 6]
    print("Product Names with more than 6 characters:", long_product_names)

    # Count the occurrence of each product in the text
    product_counts = Counter(product_names)
    print("Product Counts:", product_counts)

    # Extract orders with prices ending in .99
    prices_ending_in_99 = [price for price in prices if price.endswith('.99')]
    print("Prices ending in .99:", prices_ending_in_99)

    # Find the cheapest product
    cheapest_price = min([float(price[1:]) for price in prices])
    print("Cheapest Product Price:", f"${cheapest_price:.2f}")

if __name__ == '__main__':
    main()
