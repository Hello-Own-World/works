#Cofee Machine v. 1.0
#Hello_Own_World 28.08.19

import time
dict_of_coffe = {
    "espresso" :{
        "water" : 50,
        "coffe" : 12,
        "sugar" : 10,
        "milk" : 0,
        "cup" : 1,
        "money" : 15
    } ,
    "latte" : {
        "water" : 250,
        "coffe" : 15,
        "sugar" : 20,
        "milk" : 100,
        "cup" : 1,
        "money" : 28
    },
    "americano" : {
        "water" : 150,
        "coffe" : 12,
        "sugar" : 10,
        "milk" : 0,
        "cup" : 1,
        "money" : 17
    },
    "cappuccino" :{
        "water" : 125,
        "coffe" : 12,
        "sugar" : 10,
        "milk" : 80,
        "cup" : 1,
        "money" : 24
    }
}
ingredients = {
    "water" : 4000,
    "coffe" : 2000,
    "sugar" : 2000,
    "milk" : 2000,
    "cup" : 1000,
    "money" : 0
}

coffe_machine = {
    "menu": dict_of_coffe ,
    "ingredients": ingredients
}

def add_money (value_of_money) :
    if value_of_money >= 0 :
        coffe_machine["ingredients"]["money"] += value_of_money
        return True
    print("WRONG VALUE !!! ")
    return False
def check_if_in_machine_is_enough_ingredients (choise):
    for ingr in coffe_machine["menu"][choise]:
        if coffe_machine["ingredients"][ingr] - coffe_machine["menu"][choise][ingr] >= 0:
            print("Enough :" , ingr)
            time.sleep(0.3)
        else:
            print ("Not enough" , ingr)
            return False

def making_coffe (choise) :
    if check_if_in_machine_is_enough_ingredients(choise) != False :
        for ingr in coffe_machine["menu"][choise]:
                coffe_machine["ingredients"][ingr] -= coffe_machine["menu"][choise][ingr]
        print("Coffe is making ...")
        time.sleep(2)
        print("Take your cup ")
        time.sleep(1)


menu = str(coffe_machine["menu"].keys())

while True:
    print("-"*20)
    print("""
Welcome !
I am Coffe machine v. 1.0
If you want drink a cup of coffe , you are in right place.
So , what would you prefer?
Here is my assortment :""" , menu[11:len(menu)-2] )

    order = input("Enter name of coffe :")
    if order in coffe_machine["menu"] :
        print("Price of {} = {} grn".format(order,coffe_machine["menu"][order]["money"]))
    else:
        print("Sorry , but we haven`t this type of coffe )=")
        time.sleep(2)
        continue
    cash = int(input("Please enter money : "))
    add_money(cash)
    making_coffe(order)
    if cash > coffe_machine["menu"][order]["money"]:
        rest = cash - coffe_machine["menu"][order]["money"]
        coffe_machine["ingredients"]["money"] -=  rest
        print("Here is your rest" ,rest,"grn")
    time.sleep(3)

