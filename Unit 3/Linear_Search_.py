def linear_search_product(products, target_product):
    indices = []
    for i in range(len(products)):
        if products[i] == target_product:
            indices.append(i)
    return indices

# Example Usage:
product_list = ["Airdopes", "Bracelet", "SmartWatch", "Bracelet", "Laptop", "Calculator"]
target = "Bracelet"
result = linear_search_product(product_list, target)
print(result)

