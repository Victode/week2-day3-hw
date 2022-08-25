def print_name(name):
    print(f"Hello {name}, we've been expecting you")

def adder(num1, num2):
    return num1 + num2


    from IPython.display import clear_output

# Ask the user four bits of input: Do you want to : Show/Add/Delete or Quit?
shopping_cart = {
    'apple': 'quantity'
#         ,
#     {
#          'banana':
#         {
#             'price':0.64
#         }
#     },
#     {
#         'orange':
#         {
#             'price':0.54
#         }
#     }
}
def quantity(item):
    for value in shopping_cart.values():
        shopping_cart.append(value)
        return shopping_cart

def add(added):
    for key in shopping_cart.keys():
        shopping_cart.append(key)
        quant = input("How many are you buying?")
        quantity(quant)

    return shopping_cart

def gone(delete):
    shopping_cart.remove(delete)
    return shopping_cart

def cart():
    while True:
        nav = input("Would you like to (show) (add) (delete) or (quit)?")
        if nav == "show":
                print(shopping_cart)
                
        elif nav == "add":
            added = input("What would you like to add to your cart?")
            add(added)
        
        elif nav == 'delete':
            delete = input("What would yuou like to remove?")
            gone(delete)
            
        elif nav == 'quit':
                break
cart()
                