# 3. Mastering Tuple Packing and Unpacking in Python

# Task 1: Customer Order Processing Refine your skills in tuple unpacking by managing customer orders.
def output_orders(orders):
    for order in orders:
        customer, product, quantity = order
        print(f"{customer} ordered {quantity} unit(s) of {product}.")
    #end for
    return None
#end function

orders = orders = [
    ("Alice", "Laptop", 1),
    ("Bob", "Camera", 2),
    ("Charlie", "Phone", 3)
]
output_orders(orders)