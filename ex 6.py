#ex 6
shopping_cart = []

def additems():
    for x in range(3):
        item= input("what do you want to add? ")
        shopping_cart.append(item)
        print(shopping_cart)

additems()
print("Intial: ", shopping_cart)

shopping_cart.extend(['butter', 'cheese'])
print("Final: ", shopping_cart)




