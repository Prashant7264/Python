#bill Mangement System

#create an empty list to store items.

items = []

#welcome Message
x="Welcome to The Shop"
print(x)
#number of items

num_items = int(input("Enter the number of items:"))

for i in range(num_items):
    print(f"\nEnter details for Item {i + 1}:")
    name = input("Item Name:")
    quantity = int(input("Quantity:"))
    unit_price = float(input("Unit price:"))

#add items in the list use append for adding
    items.append({"name": name, "quantity": quantity, "unit_price": unit_price})
    print(items)


total_amount = 0

#Calculate the total cost for each item and total amount of items.

for item in items:
    item_total = item["quantity"]* item["unit_price"]
    total_amount += item_total
    print((f'{item["name"]}: {item["quantity"]} * {item["unit_price"]:.2f} = {item_total:.2f}'))
#

remove_item = input("Do you want to remove an item? (yes/no): ")
if remove_item == "yes":
    item_to_remove = input("Enter the name of the item to remove: ")
    items = [item for item in items if item["name"]!= item_to_remove]
if remove_item == "no":
    pass
#discount
discount = float(input("Enter discount percentage:"))
if discount>0:
    discount_amount = total_amount * (discount / 100)
    total_amount -= discount_amount
    print(f'Discount Applied: {discount}% = -{discount_amount:.2f}')

# Add a unique invoice number
import uuid
invoice_number = str(uuid.uuid4())
print(f'\nInvoice Number: {invoice_number}')


#Grand Total
print(f'\n Total AMount: {total_amount:.2f}')


#print the bill/invoice for payment
from datetime import datetime

class Bill:
    def __init__(self, invoice_number, total_amount):
        self.invoice_number = invoice_number
        self.total_amount = total_amount
        self.print_receipt()
    def print_receipt(self):
        print(f'\nReceipt for Invoice Number: {self.invoice_number}')
        print(f'Date: {datetime.now()}')
        print('------------------------')
        print(f'Total Amount: {self.total_amount:.2f}')
        print(f'Thank you!! visit Again..!')

bill=Bill(invoice_number, total_amount)


