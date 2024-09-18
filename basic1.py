from Data.variables import sales_transactions

products = set()
for transaction in sales_transactions:
    products.add(transaction["product_id"])

# product_id -> quantity and price of product
def get_product_properties(product_id: str) -> (int, int):
    quantity = 0
    for transaction in sales_transactions:
        unit_price = transaction["unit_price"]
        if transaction["product_id"] == product_id:
            quantity += transaction["quantity"]
    return (quantity, unit_price)


# product_id -> total sales in money
def get_total_sales(product_id: str) -> int:
    properties = get_product_properties(product_id)
    return properties[0] * properties[1]


# making dictionary of {product, total sales}
sales_dictionary: dict[str, float] = {}
for product in products:
    sales_dictionary[product] = get_total_sales(product)

# prints first output of question
print(sales_dictionary)

# gets the list of products in descending order on the basis of sales
product_cost_pairs = []
for (key, value) in sales_dictionary.items():
    product_cost_pairs.append(tuple([key, value]))

descending_products_sales = []
for product in sorted(product_cost_pairs, key=lambda x: x[1], reverse=True):
    descending_products_sales.append(product[0]) # adding product ID to list

# prints second output of question
print(descending_products_sales)
