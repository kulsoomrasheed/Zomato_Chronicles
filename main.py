arr = []

def addSnack(id,name, price, availability,qty):
    obj = {}
    obj['id'] = id
    obj['Snack_name'] = name
    obj['price'] = price
    obj['availability'] = availability
    obj['qty'] = qty
    arr.append(obj)
   

addSnack(1,'pizza', 90, True,50)
addSnack(2,'samosa', 8, True,50)
addSnack(3,'aloo tikki', 40, True,50)
addSnack(4,'patties', 10, True,50)

def removeSnack(id):
    snack_found = False  # Flag to track if the snack with the given ID is found
    for i in arr:
        if i['id'] == id:
            arr.remove(i)
            print(f"Snack with ID {id} has been removed from the inventory.")
            snack_found = True  # Set the flag to True if the snack is found

    if not snack_found:
        print("The snack was not found, please try with a different id")

# Test the removeSnack function
b=removeSnack(5)  # This will remove the snack with ID 1 if it exists
 # This will display an error message as ID 5 doesn't exist in the inventory

print(b,'----------------')

def updateSnackAvailability(id, availability):
    # Loop through each snack dictionary in the inventory (arr)
    for snack in arr:
        # Check if the 'id' of the snack matches the provided 'id'
        if snack.get('id') == id:
            # Update the 'availability' attribute based on the provided 'availability' parameter
            snack['availability'] = availability
            print(f"Snack with ID {id} has been updated as {'available' if availability else 'unavailable'}.")
            return

    # If the loop finishes without finding a matching ID, display an error message
    print(f"Snack with ID {id} was not found in the inventory.")

updateSnackAvailability(1,False)
print(arr)


sales_records = []

def recordSale(id, quantity):
    # Loop through each snack dictionary in the inventory (arr)
    for snack in arr:
        # Check if the 'id' of the snack matches the provided 'id'
        if snack.get('id') == id:
            # Check if the snack is available before recording the sale
            if snack['availability']:
                # Update the quantity in the inventory to reflect the sale
                snack['qty'] -= quantity

                # Create a sales record entry with snack ID and quantity sold
                sales_record = {
                    'snack_id': id,
                    'quantity_sold': quantity
                }

                # Append the sales record to the sales records list
                sales_records.append(sales_record)

                print(f"Sale recorded: {quantity} of snack with ID {id} sold.")
                return
            else:
                print(f"Snack with ID {id} is unavailable for sale.")
                return

    # If the loop finishes without finding a matching ID, display an error message
    print(f"Snack with ID {id} was not found in the inventory.")


recordSale(3,1)

