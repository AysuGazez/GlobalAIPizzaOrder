import csv
import datetime

# üst pizza sınıfı
class Pizza:
    def __init__(self):
        self.description = ""
        self.cost = 0.0

    def get_description(self):
        return self.__class__.__name__

    def get_cost(self):
        return self.__class__.cost

# alt pizza sınıfları
class ClassicPizza(Pizza):
    cost = 70.0
    2
    def __init__(self):
        self.description = "Classic Pizza's ingredients: Cheese, Tomato Sauce, Sausage, Olives "
        print(self.description)

class MargaritaPizza(Pizza):
    cost = 80.0

    def __init__(self):
        self.description = "Margarita Pizza's ingredients: Mozzarella, Tomato Sauce, Basil "
        print(self.description)

class TurkishPizza(Pizza):
    cost = 90.0

    def __init__(self):
        self.description = "Turkish Pizza's ingredients: Cheese, Tomato Sauce, Ground Beef, Olives "
        print(self.description)

class QuattroFormaggiPizza(Pizza):
    cost = 100.0

    def __init__(self):
        self.description = "Quattro Formaggi Pizza's ingredients: Mozzarella, Cheddar, Blue Cheese , Parmesan Cheese "
        print(self.description)

class VegetarianPizza(Pizza):
    cost = 85.0

    def __init__(self):
        self.description = "Vegetarian Pizza's ingredients: Mozzarella, Tomato Sauce, Mushroom, Olives, Corn, Onion  "
        print(self.description)

# decorator sınıfı

class Decorator(Pizza):
    def __init__(self, component):
        self.component = component
        self.cost = 0.0
        self.description = ""

    def get_cost(self):
        return self.cost + \
               Pizza.get_cost(self)

    def get_description(self):
        return self.get_description() + \
               Pizza.get_description(self)

class Olive(Decorator):
    cost = 7.5

    def __init__(self, component):
        super().__init__(component)
        self.description = "Olives"
        self.component = component

class Mushroom(Decorator):
    cost = 9.5

    def __init__(self, component):
        super().__init__(component)
        self.description = "Mushrooms"
        self.component = component

class Mozzarella(Decorator):
    cost = 12.0

    def __init__(self, component):
        super().__init__(component)
        self.description = "Mozzarella"
        self.component = component

class Beef(Decorator):
    cost = 25.0

    def __init__(self, component):
        super().__init__(component)
        self.description = "Beef"
        self.component = component

class Onion(Decorator):
    cost = 5.0

    def __init__(self, component):
        super().__init__(component)
        self.description = "Onions"
        self.component = component

class Corn(Decorator):
    cost = 6.0

    def __init__(self, component):
        super().__init__(component)
        self.description = "Sweet Corn"
        self.component = component

def main():
    with open("Menu.txt", "r") as menu:
        for i in menu:
            print(i, end="")

    menu_dict= {
        1: ClassicPizza,
        2: MargaritaPizza,
        3: TurkishPizza,
        4: QuattroFormaggiPizza,
        5: VegetarianPizza,
        11: Olive,
        12: Mushroom,
        13: Mozzarella,
        14: Beef,
        15: Onion,
        16: Corn
    }

    total_cost = 0

    choice = input("Please Choose Your Pizza Number:")
    while choice not in ["1", "2", "3", "4", "5"]:
        choice = input("You Chose Wrong Number:")

    order = menu_dict[int(choice)]()
    cost_1 = order.get_cost()

    while choice != "0":
        choice = input("Please Choose Your Extra Ingredients (If You Don't Want Anything Else Please Press 0):")
        if choice in ["11", "12", "13", "14", "15", "16"]:
            order = menu_dict[int(choice)](choice)
            cost_2 = order.get_cost()

    total_cost = cost_1 + cost_2
    print(f"Your total is {total_cost} ₺")
    cost_l = str(total_cost) + "₺"
    # siparis bilgi

    name = input("Please write your name-surname: ")
    id_number = input("Please write your ID number: ")
    if len(id_number) != 11:
        id_number = input("Invalid entry. ID number must be 11 digits: ")
    credit_no = input("Please write your credit card number: ")
    if len(credit_no) != 16:
        credit_no = input("Invalid entry. Credit card number must be 16 digits: ")
    credit_psw = input("Please write your credit card password: ")
    if len(credit_psw) != 4:
        credit_psw = input("Invalid entry. Password must be 4 digits.")
    address = input("Please write your delivery address: ")
    phone = input("Please write your phone number: ")
    time = datetime.datetime.now()

    with open("Orders_Database.csv", "a") as orders:
        orders = csv.writer(orders, delimiter =",")
        orders.writerow([name, id_number, credit_no, credit_psw, address, phone, cost_l, time ])
        print("Your order has been confirmed.")

if __name__ == '__main__':
    main()