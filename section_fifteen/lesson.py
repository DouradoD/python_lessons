import sys
from enum import Enum

class ErrorMessages(str, Enum):
    INGREDIENT_NOT_ENOUGH = "Sorry there is not enough {ingredient}.”"
    INVALID_DRINK = "Drink not founded!"
    INVALID_INGREDIENT = "Invalid ingredient! This,{ingredient},ingredient is not supported by this Machine"
    TRY_ANOTHER_DRINK = "Try choosing another drink!"
    MONEY_NOT_ENOUGH = "Sorry that's not enough money. Money refunded."

class IngNames(str, Enum):
    MILK = "milk"
    WATER = "water"
    COFFEE = "coffee"

class DrinksNames(str, Enum):
    ESPRESSO = "espresso"
    CAPPUCCINO = "cappuccino"
    LATTE = "latte"

class Drinks:
    def __init__(self, name, price, **ingredients):
        self.name = name
        self.price = price
        self.ingredients = ingredients

class Resources:
    def __init__(self, name, measure, quantity):
        self.name = name
        self.measure = measure
        self.quantity = quantity

    def reduce_quantity(self, qty):
        self.quantity-= qty
class Price:
    def __init__(self, quarters = 0.0, dimes = 0.0, nickles = 0.0, pennies = 0.0):
        self.quarters = quarters
        self.dimes = dimes
        self.nickles = nickles
        self.pennies = pennies
        self.total = self.get_total_after_sum()

    def get_total_after_sum(self):
        self.sum_all()
        return self.total

    def sum_all(self):
        self.total = 0.25 * self.quarters + 0.1 * self.dimes + 0.05 * self.nickles + 0.01 * self.pennies

class CoffeeMachine:
    def __init__(self):
        self.machine_resources = {}
        self.orders = []
        self.drinks = ()
        self.status = False
        self.inserted_coins = {}
        self.get_drinks_info()
        self.get_machine_resources()

    def get_drinks_info(self):
        espresso = Drinks(DrinksNames.ESPRESSO,2.5, **{IngNames.MILK: 100, IngNames.WATER: 50, IngNames.COFFEE: 24})
        cappuccino = Drinks(DrinksNames.CAPPUCCINO, 2.75, **{IngNames.MILK: 150, IngNames.WATER: 50, IngNames.COFFEE: 50})
        latte = Drinks(DrinksNames.LATTE, 1.5, **{IngNames.MILK: 150, IngNames.WATER: 50, IngNames.COFFEE: 50})
        self.drinks = (espresso,cappuccino,latte)

    def turn_on(self):
        print('Turning ON the Coffee Machine ...')
        self.status = True

    def get_machine_resources(self):
        if not self.machine_resources:
            self.machine_resources = [Resources(IngNames.MILK, "ml", 500),
                                      Resources(IngNames.WATER, "ml", 500),
                                      Resources(IngNames.COFFEE, "g", 100)]

    def display_the_machine_resources(self):
        print('Coffee Machine resources:')
        for resource in self.machine_resources:
            print(f' - {resource.name} = {resource.quantity} {resource.measure}')
        print(f' - Price total = {self.get_total_value()}')

    def turn_off(self):
        print('Turning OFF the Coffee Machine ...')
        self.status = False

    def are_there_sufficient_resource(self, drink_input):
        ingredient_not_enough = []
        status = True
        current_drink = [drink for drink in self.drinks if drink.name == drink_input]
        if not current_drink:
            return print(ErrorMessages.INVALID_DRINK.value)
        ingredients = current_drink[0].ingredients
        for ingredient in ingredients:
            resource = [res for res in self.machine_resources if res.name == ingredient.value]
            if not resource:
                return print(ErrorMessages.INVALID_INGREDIENT.value.format(ingredient))

            if not ingredients.get(ingredient) <= resource[0].quantity:
                ingredient_not_enough.append(ingredient.name)
        if ingredient_not_enough:
            print(f'{ErrorMessages.INGREDIENT_NOT_ENOUGH.value.format(ingredient=ingredient_not_enough)}\n')
            return False
        return status

    def are_there_sufficient_money(self, drink_input):
        status = True
        current_drink = [drink for drink in self.drinks if drink.name == drink_input]
        machine_drink_price = current_drink[0].price
        if not current_drink:
            return print(ErrorMessages.INVALID_DRINK.value)
        total = Price(quarters = self.inserted_coins['quarters'],
                      dimes = self.inserted_coins['dimes'],
                      nickles = self.inserted_coins['nickles'],
                      pennies = self.inserted_coins['pennies']).total
        if total < machine_drink_price:
            print(ErrorMessages.MONEY_NOT_ENOUGH.value)
            return False
        refund_value = total - machine_drink_price
        print(f'Here is ${refund_value} dollars in change.')
        return status

    def create_the_drink(self, drink_input):
        if not self.are_there_sufficient_money(drink_input):
            return
        if not self.are_there_sufficient_resource(drink_input):
            return
        print(f'Doing the {drink_input} ...')
        print('.......')
        current_drink = [drink for drink in self.drinks if drink.name == drink_input]
        if not current_drink:
            return print(ErrorMessages.INVALID_DRINK.value)
        for ingredient_name in current_drink[0].ingredients:
            for resource in self.machine_resources:
                if resource.name == ingredient_name:
                    resource.quantity -= current_drink[0].ingredients.get(ingredient_name)
        self.orders.append(drink_input)
        print('Your drink is done!')

    def get_total_value(self):
        total_value = 0.0
        tup_orders = tuple(self.orders)
        for order in tup_orders:
            order_qty = self.orders.count(order)
            drink_value = [drink for drink in self.drinks if drink.name == order][0].price
            total_value += drink_value * order_qty
        return total_value



coffee_machine = CoffeeMachine()
coffee_machine.turn_on()
while coffee_machine.status:
    choose_item = input("What would you like? (espresso/latte/cappuccino):")
    if choose_item == "off":
        coffee_machine.turn_off()
    elif choose_item == "report":
        coffee_machine.display_the_machine_resources()
    else:
        while coffee_machine.status:
            print("Could you insert the coins?"
                  "quarters = $0.25, dimes = $0.10, nickles = $0.05, pennies = $0.01")
            coins_list = ['quarters', 'dimes', 'nickles', 'pennies']
            try:
                for coin in coins_list:
                    coffee_machine.inserted_coins[coin] = int(input(f'Insert a quantity of {coin} in unit":'))
            except ValueError:
                print('Invalid value, try again!')
                break
            coffee_machine.create_the_drink(choose_item)
            break

