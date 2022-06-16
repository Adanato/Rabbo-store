# I want this to act as a location.
# actions possible are buying, looking for items, 
# and talking to rabbo

# List items
shopping_cart = []
ShoppingItems = ["Carrots", "Lettuce", "Tomatoes"]

DinerMenuItems = ["Carrot Stew" , "Carrots and Beef", "Rat Soup"]

### Functions to enter store

#Main function
def rabbo_store_main(): 
    print("Hello! Welcome to Rabbo\'s store. \nDo you want to enter? \nYes or No")
    enter_store()
    store_actions()



def enter_store():
    UserAnswer = input()
    match UserAnswer.lower():
        case "yes":
            print("Awesome huhu")
        case "no":
            print("ok bye")
            #leave function
        case _:
            print("Yes or No")
            enter_store() 

def store_actions():
    print("\"You walk into rabbo's amazing store, and start to look around.\"")
    print("what do you want to do? \n Shop, Eat, or Talk?")

def choose_store_actions():
    UserAnswer = input()
    match UserAnswer.lower():
        case "shop":
            print("Awesome huhu")
        case "eat":
            print("ok bye")
        case "talk":
            print("I don't want to talk with you lol \n Choose something else.")
            choose_store_actions()
        case _:
            print("Shop, Eat, or Talk?")
            choose_store_actions()

### shopping functions

def items_in_stock():
    print("Let's see what I have in stock")
    stock = "I have "
    for i in ShoppingItems:
        if i != ShoppingItems[len(ShoppingItems) - 1]:
            stock = stock + i +", "
        else:    
            stock = stock + "and " + i 
    print( stock + " in stock.")


def buy_items(): 
    print("What do you want to buy?")
    UserAnswer = input()
    for i in ShoppingItems:
        if i.lower() == UserAnswer.lower():
            shopping_cart.append(i)
            break        
    if shopping_cart == []:
        print("We don't have that try again.")
        buy_items()       

def checkout():
    31
### dining functions

def menu_in_stock():
    stock = "We have "
    for i in DinerMenuItems:
        if i != DinerMenuItems[len(DinerMenuItems) - 1]:
            stock = stock + i +", "
        else:    
            stock = stock + "and " + i 
    print( stock + " on our menu.")

def eat_at_diner():
    print("What do you want to eat?")

    UserAnswer = input()

    match UserAnswer.lower():
        case "carrot stew": 
            print("'It was really fresh and tasty'")
        case "carrots and beef":
            print("Vegetarians are wary of you.")
        case "rat soup": 
            print("The Big Rat hates you")
        case _:
            print("We don't have that on our menu.")
            eat_at_diner()

eat_at_diner()

#rabbo_store_main()