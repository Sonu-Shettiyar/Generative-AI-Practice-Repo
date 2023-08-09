import json

arr = {"items": [], "orders": [], "totalSales": 0}

try:
    with open('item.json', 'r') as json_content:
        arr = json.load(json_content)
except FileNotFoundError:
    print('File not Found')

def updateJsonFile():
    try:
        with open('item.json', 'w') as json_content:
            json.dump(arr, json_content, indent=4)
        return True
    except:
        return False

def displayMenu():
    print('==================\n')
    print('MENU')

    for i in range(len(arr['items'])):
        print(f'{arr["items"][i]["id"]}: {arr["items"][i]["name"]} Rs.{arr["items"][i]["price"]}')
    
    print('\n===================================')

def addItem():
    itemDict = {}
    name = input('Enter a name for the Item: ')
    price = int(input('Enter a price for the Item: '))
    qty = int(input('Enter the quantity: '))
    itemDict['name'] = name
    itemDict['price'] = price
    itemDict['qty'] = qty
    itemDict['id'] = hash(name)
    arr['items'].append(itemDict)
    check = updateJsonFile()
    if check:
        print('Snack Added Successfully')
        print('\n---------------------\n')
    else:
        print('\n----------------------\n')
        print('Something went wrong while adding a new item in the menu')
        print('\n------------------\n')


def addOrder():
    cus = input("Enter a customer's name: ")
    itemId = None
    try:
        itemId = list(map(int, input("Enter Item Id [use ',' to separate multiple ids]: ").split(', ')))
    except ValueError:
        print('Please enter valid Ids')
        return addOrder()
    
    totalPrice = 0
    itemEl = []
    count = 0
    
    for i in range(len(arr["items"])):
        for j in itemId:
            if j == arr["items"][i]["id"]:
                count += 1
                if arr["items"][i]["qty"] == 0:

                    print(f'Item with id: {j} is not Available right now.')
                    print('\n------------------\n')
                    return
                
                arr["items"][i]["qty"] = arr["items"][i]["qty"] - 1
                itemEl.append(arr["items"][i]["name"])
                totalPrice += arr["items"][i]["price"]
    
    if count == 0:
        print('Wrong Ids provided.')
        return
    
    orderDict = {}
    orderDict["customer"] = cus
    orderDict["orderId"] = hash(cus)  
    orderDict["items"] = itemEl
    orderDict["totalPrice"] = totalPrice
    orderDict["status"] = 'received'
    
    arr["orders"].append(orderDict)
    arr["totalSales"] = arr["totalSales"] + totalPrice
    check = updateJsonFile()
    
    if check:
        print('\n+__________________________________________=______\n')
        print('Order Confirmed.')
        print('\n#################\n')
        print('Order Details: ')
        for i in orderDict:
            if i == 'totalPrice':
                print(f"{i}: Rs.{orderDict[i]}")
                continue
            elif i == 'items':
                print(f"{i}: {', '.join(orderDict[i])}")
                continue
            print(f"{i}: {orderDict[i]}")
        print('\n###################')
        print('\n+________________________________________________\n')
    else:
        print('\n+=________________________________________________\n')
        print('Something went wrong while taking your order.')
        print('\n+____________+__________________________________________\n')

def displaySales():
    print('\n+____________________________________\n')
    print(f'Total Sales: Rs.{arr["totalSales"]}')
    print('\n+______+____________________________________\n')

def removeItem():
    _id = int(input('Enter the id of the element which has to be removed: '))
    index = None
    for i in range(len(arr["items"])):
        if arr["items"][i]["id"] == _id:
            index = i
            break
    if index is not None:
        arr["items"].pop(index)
        check = updateJsonFile()
        if check:
            print('\n+____________=__________________\n')
            print('Item Removed from the Menu')
            print('\n+________________________\n')
        else:
            print('\n+=__________________\n')
            print('Something went wrong while updating the new Menu')
            print('\n+________________________\n')
    else:
        print('No Product Found')


def updateAvailability(): 
    _id = int(input('Enter the id of the product whose availability has to be changed: '));
    newQty = int(input('Enter quantity: '));
    for i in range(len(arr["items"])):
        if _id == arr["items"][i]["id"]:
            arr["items"][i]["qty"] = newQty;
            check = updateJsonFile();
            if check:
                print('\n+____________+____________________________________\n');
                print("Availability changed");
                print('\n+__________________________________________\n');
            else:
                print('\n+________________________________________________\n');
                print('Something went wrong while updating the new Menu');
                print('\n+____________+______________________________\n');
            return;
    print('\n+______=__________________\n');
    print('No Product Found');
    print('\n+________________________\n');


def updateOrder():
    _id = int(input('Enter Order Id: '));
    status = input('Enter status of the order: ');
    for i in range(len(arr['orders'])):
        if arr["orders"][i]['orderId'] == _id:
            arr["orders"][i]["status"] = status;
            check = updateJsonFile();
            if check:
                print('\n+________________________+________________________\n');
                print("Status changed");
                print('\n+______________________________________________________\n');
            else:
                print('\n+____________+________________________________________________\n');
                print('Something went wrong while updating the status of an order');
                print('\n+__________________________________________\n');
            return;
    print('\n+____________________________________________________________\n');
    print('No Product Found');
    print('\n+_________________________________\n');

def displayAllOrders(): 
    print('\n+____________________________________\n');
    for j in arr['orders']:
        print('\n####################\n');
        for i in j:
            if i=='totalPrice':
                print(f"{i}: Rs.{j[i]}");
                continue;
            elif i=='items':
                print(f"{i}: {', '.join(j[i])}");
                continue;
            print(f"{i}: {j[i]}");
        print('\n###################\n');
    print('\n+__________________________________________\n');

def main():
    while True:
        print('=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=')
        print('1. To See the Menu')
        print('2. To Add a Snack')
        print('3. To Add an Order')
        print('4. To Remove a Snack from the Menu')
        print('5. To Update availability of an Item')
        print('6. To Display Total Sales')
        print('7. To Update an order')
        print('8. To Display all Orders')
        print('9. To Close the application')
        print('=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=')

        choice = input('Enter a valid option between 1-9: ')

        if choice == '1':
            displayMenu()
        elif choice == '2':
            addItem()
        elif choice == '3':
            addOrder()
        elif choice == '4':
            removeItem()
        elif choice == '5':
            updateAvailability()
        elif choice == '6':
            displaySales()
        elif choice == '7':
            updateOrder()
        elif choice == '8':
            displayAllOrders()
        elif choice == '9':
            print('Thank you for coming to Zesty Zomato.')
            break
        else:
            print('Please Enter a valid option')

if __name__ == "__main__":
    print('Welcome to Zesty Zomato')
    main()
