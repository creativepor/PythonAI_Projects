# You are building a checkout system. Given a store inventory with stock levels and prices, 
# calculate the total cost for a customer's cart and update the inventory stock.tory

inventory = {
    "apple": {"price": 20, "stock": 30},
    "banana": {"price": 40, "stock": 60},
    "orange": {"price": 80, "stock": 120},
    "kiwi": {"price": 60, "stock": 50},
    "grapes": {"price": 100, "stock": 80},
    "dragon fruit": {"price": 200, "stock": 20}
}

# Add the cart items with quantities
cart = {"apple": 2, "banana": 5, "kiwi": 3, "grapes": 1} 

total_bill = 0.0

for item in cart:
    if item in inventory:
        item_price = inventory[item]["price"]
        item_quantity = cart[item]
        sub_total = item_price * item_quantity
        total_bill += sub_total
        inventory[item]["stock"] -= item_quantity

        print(f"Item: {item}, Price: {item_price}, Quantity: {item_quantity}, Subtotal: {item_price * item_quantity}")
    else:
        print(f"Item {item} is not available in the inventory")

print(f"Total Bill: {total_bill}")
print(f"Updated Inventory: {inventory}")    




