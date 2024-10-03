for num in range(0,6):
    print('DRINKS')
    print("Water        Free!")
    print("Coca Cola    $1.50")
    print("Sprite       $1.50")
    print("Ginger Ale   $1.50")
    
    print('FOODS')
    print("Pizza               Free!")
    print("Hamburger           $2.15")
    print("Fried Chicken       $2.15")
    print("Pho                 $2.15")
    print("Tacos               Free!")

    food_items = ["pizza","hamburger","fried chicken","pho","tacos"]
    drink_items = ["water","ginger ale","coca cola","sprite"]
    order_list = [] #amount of items ordered
    amount_list = [] #
    price = 0


    item_input = input("["+str(num)+"] What do you want to order? > ").lower().strip("!?, %$")

    if item_input == "":
        break
    
    if item_input in food_items or item_input in drink_items:
        item_amt = input("How many would you like? ").lower().strip("!?, %$")
        item_amt = int(item_amt)
        if(item_amt < 1):
            print("Changing negative amount to 1.")
            item_amt = 1
        if(item_amt > 99):
             print("You cannot order more than 99 items at a time!")
             item_amt = 99
        try:
                order_list.append(item_input)
                
        except ValueError:
            print("please enter a valid number for the amount.")     
    else:
        print("I'm sorry, I don't think we sell that.")
    

print("RECEIPT")





    
    
    



