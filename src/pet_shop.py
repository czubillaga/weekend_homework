# WRITE YOUR FUNCTIONS HERE
def get_pet_shop_name(shop):
    return shop["name"]

def get_total_cash(shop):
    return shop["admin"]["total_cash"]

def add_or_remove_cash(shop, cash):
    shop["admin"]["total_cash"] += cash

def get_pets_sold(shop):
    return shop["admin"]["pets_sold"]

def increase_pets_sold(shop, increase):
    shop["admin"]["pets_sold"] += increase

def get_stock_count(shop):
    return len(shop["pets"])

def get_pets_by_breed(shop, breed):
    pet_list = []
    for pet in shop["pets"]:
        if pet["breed"] == breed:
            pet_list.append(pet)

    return pet_list

def find_pet_by_name(shop, name):
    for pet in shop["pets"]:
        if pet["name"] == name:
            return pet
    return None
    

def remove_pet_by_name(shop, name):
    for pet in shop["pets"]:
        if pet["name"] == name:
            shop["pets"].pop(shop["pets"].index(pet))

def add_pet_to_stock(shop, new_pet):
    shop["pets"].append(new_pet)

def get_customer_cash(customer):
    return customer["cash"]

def remove_customer_cash(customer, cash):
    customer["cash"] -= cash

def get_customer_pet_count(customer):
    return len(customer["pets"])

def add_pet_to_customer(customer, new_pet):
    customer["pets"].append(new_pet)

def customer_can_afford_pet(customer, pet):
    if customer["cash"] >= pet["price"]:
        return True
    else:
        return False

def sell_pet_to_customer(shop, pet, customer):
    if pet == None:
        return
    if customer_can_afford_pet(customer,pet):
        remove_customer_cash(customer, pet["price"])
        add_or_remove_cash(shop, pet["price"])
        add_pet_to_customer(customer, pet)
        remove_pet_by_name(shop, pet["name"])
        increase_pets_sold(shop, 1)