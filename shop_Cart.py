def display_cart(cart):
    if not cart:
        print("\nYour cart is empty")
    else:
        print("\nShopping cart:")
    total_price = 0
    for item in cart:
        print(f"{item['name']}: ${item['price']}")
        total_price+=item['price']
    print("--------------------------")
    print(f"Total: ${total_price:.2f}")
    
def main():
    cart = []
    while True:
        print("\nShopping Cart Application")
        print("1. Add Item to Cart")
        print("2. View Cart")
        print("3. Remove Item from Cart")
        print("4. Exit")
        
        choice = input("\nEnter your choice: ")
        if choice == '1':
            item_name = input("\nEnter item name: ")
            item_price = float(input("Enter item price: "))
            item = {"name": item_name, "price": item_price}
            cart.append(item)
            print('\nItem added to cart!')
        elif choice == '2':
            display_cart(cart)
        elif choice == '3':
            if not cart:
                print("Your Cart is Empty")
            else:
                display_cart(cart)
                item_index = int(input("\nEnter the item number to remove: ")) - 1
                if 0 <= item_index < len(cart):
                    removed_item = cart.pop(item_index)
                    print(f"\nRemoved item: {removed_item['name']}")
                else:
                    print("Invalid item number.")
        elif choice == '4':
            print("Exit the application")
            break
        else:
            print("Invalid choice. Please select a valid option")
if _name_ == "_main_":
    main()