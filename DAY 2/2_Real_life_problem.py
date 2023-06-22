'''Program checks you are hungry or not. if you are hungry then a fastfood menu will display and you have to pick the item from the menue.
When You order the item then show you a message that "Your order has been placed successfully'''

def menu():
    print('''
    Your Options Are:
            Press 1 to order "Pizza"
            Press 2 to order "Burger"
            Press 3 to order "Shawarma"
            Press 4 to order "Fries"
            Please Enter any other number to Exit.
    ''')
    order = input("Which food would you like to order? ")
    fast_food = ["Pizza","Burger","Shawarma","Fries"]
    try:
        order = int(order)
        if order == 1:
            print(f"Thanks for ordering {fast_food[0]}!")
        elif order == 2:
            print(f"Thanks for ordering {fast_food[1]}!")
        elif order == 3:
            print(f"Thanks for ordering {fast_food[2]}!")
        elif order == 4:
            print(f"Thanks for ordering {fast_food[3]}!")
        else:
            print("Thanks for visiting our menu!")
    except ValueError:
        print("Please Enter a valid food number!")
        menu()
    
            

while True:
    status = input("If you are hungry Enter 'Yes' otherwise Enter 'No':")
    if status.lower() == "yes":
        menu()
        break
    elif status.lower() == "no":
        print("Thanks for visiting us. You can place an order when you are hungry!")
        break
