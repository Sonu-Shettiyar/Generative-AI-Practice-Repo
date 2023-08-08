inventory = []
sales_records = []

while True:
    print("Canteen Management System")
    print("1. Add a snack")
    print("2. Remove a snack")
    print("3. Update snack availability")
    print("4. Make a sale")
    print("5. Show inventory")
    print("6. Show sales records")
    print("7. Exit")
    
    choice = input("Enter your choice: ")
    
    if choice == '1':
        # Add a snack
        snack = {}
        snack['id'] = input("Enter snack ID: ")
        snack['name'] = input("Enter snack name: ")
        snack['price'] = float(input("Enter snack price: "))
        snack['availability'] = input("Is the snack available? (yes/no): ")
        inventory.append(snack)
        print("Snack added to inventory.")
        
    elif choice == '2':
        # Remove a snack
        snack_id = input("Enter snack ID to remove: ")
        for snack in inventory:
            if snack['id'] == snack_id:
                inventory.remove(snack)
                print("Snack removed from inventory.")
                break
        else:
            print("Snack not found in inventory.")
        
    elif choice == '3':
        # Update snack availability
        snack_id = input("Enter snack ID to update availability: ")
        for snack in inventory:
            if snack['id'] == snack_id:
                new_availability = input("Update availability (yes/no): ")
                snack['availability'] = new_availability
                print("Availability updated.")
                break
        else:
            print("Snack not found in inventory.")
        
    elif choice == '4':
        # Record a sale
        snack_id = input("Enter snack ID sold: ")
        for snack in inventory:
            if snack['id'] == snack_id:
                if snack['availability'] == 'yes':
                    snack['availability'] = 'no'
                    sales_records.append(snack)
                    print("Sale recorded.")
                else:
                    print("Snack is not available for sale.")
                break
        else:
            print("Snack not found in inventory.")
        
    elif choice == '5':
        # Display inventory
        print("Current Inventory:")
        for snack in inventory:
            print(f"ID: {snack['id']}, Name: {snack['name']}, Price: {snack['price']}, Availability: {snack['availability']}")
        
    elif choice == '6':
        # Display sales records
        print("Sales Records:")
        for sale in sales_records:
            print(f"ID: {sale['id']}, Name: {sale['name']}, Price: {sale['price']}")
        
    elif choice == '7':
        print("Exiting the application.")
        break
        
    else:
        print("Invalid choice. Please select a valid option.")
