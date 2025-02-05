import datetime  \

def display_final_bill():
    try:
        with open("bill_data.txt", "r") as f:
            order_details = []
            lines = f.readlines()
            total_price = int(lines[-1].strip()) 
            
            for line in lines[:-1]:  
                parts = line.strip().split(",") 
                item = parts[0] 
                plates = int(parts[1])  
                price = int(parts[2])  
                order_details.append((item, plates, price))

        print("\n***** FINAL BILL *****")
        print("Order Time:", datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
        print("------------------------------")
        
        for item, plates, price in order_details:
            print(f"{item}: {plates} plate(s) x ₹{price // plates} = ₹{price}")
        
        print("\nTotal Price (including delivery if applicable): ₹", total_price)
        print("------------------------------")
        print("Thank you for ordering from Tasty Corner!")

    except FileNotFoundError:
        print("Error: No bill found. Please place an order first.")
    except Exception as e:
        print("An error occurred while reading the bill:", str(e))

if __name__ == "__main__":
    display_final_bill() 
