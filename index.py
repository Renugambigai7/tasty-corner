import final_bill 

def display_menu(menu_choice):
    if menu_choice == "veg":
        return {"veg biriyani": 80, "parotta": 25, "fried rice": 50, "meals": 60, "dosa": 30}
    elif menu_choice == "non_veg":
        return {"chicken biriyani": 100, "chicken fry": 60, "fish fry": 60, "mutton biriyani": 120}
    else:
        print("Invalid menu choice. Please choose either 'veg' or 'non_veg'.")
        return None

def place_order(menu):
    order_details = [] 
    total_price = 0  

    while True:  
        print(f"\nMenu: {menu}")  
        order = input("Choose your order: ")

        if order in menu:
            while True:
                try:
                    plates = int(input(f"How many plates of {order} would you like? "))
                    if plates <= 0:
                        print("Please enter a valid number of plates.")
                        continue
                    break  
                except ValueError:
                    print("Invalid input! Please enter a number.")
            
            total_price += menu[order] * plates
            order_details.append((order, plates, menu[order] * plates)) 
        else:
            print("Invalid choice, please select from the menu.")

        order_more = input("Do you want to order more? (yes or no): ")
        if order_more != "yes":
            break

    return order_details, total_price

def apply_delivery_charge(total_price):
    while True:
        delivery = input("Do you want delivery? (yes or no): ")
        if delivery == "yes":
            total_price += 30  
            break
        elif delivery == "no":
            break
        else:
            print("Invalid input! Please enter 'yes' or 'no'.")
    return total_price

def main():
    print("***** Welcome to Tasty Corner *****")
    menu_choice = input("Choose your menu type (veg or non_veg): ")
    menu = display_menu(menu_choice)

    if menu:
        order_details, total_price = place_order(menu)
        total_price = apply_delivery_charge(total_price)  
    
        with open("bill_data.txt", "w") as f:
            for item, plates, price in order_details:
                f.write(f"{item},{plates},{price}\n")  
            f.write(str(total_price) + "\n")  
       
        final_bill.display_final_bill()  
if __name__ == "__main__":
    main()
