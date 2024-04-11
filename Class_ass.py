class Shop:
    def __init__(self, name, brand, quantity):
        self.name = name
        self.brand = brand
        self.quantity = quantity

    def sell(self):
        print(f'We sell {self.brand}, and we have {self.quantity} left.')

    def buy(self):
        amount = int(input('How many do you want to buy? '))
        if amount > self.quantity:
            print(f'Sorry, we only have {self.quantity} {self.brand} left.')
        else:
            self.quantity -= amount
            print(f'You bought {amount} {self.brand}. Now we have {self.quantity} left.')


class Mall:
    def __init__(self):
        self.pepsi = Shop('Escanor Drinks', 'Pepsi', 30)
        self.mirinda = Shop('Escanor Drinks', 'Mirinda', 40)
        self.fanta = Shop('Escanor Drinks', 'Fanta', 40)
        self.cocacola = Shop('Escanor Drinks', 'Cocacola',60)


mall_instance = Mall()

print("Selling Pepsi:")
mall_instance.pepsi.sell()
mall_instance.pepsi.buy()

print("\nSelling Mirinda:")
mall_instance.mirinda.sell()
mall_instance.mirinda.buy()

print("\nSelling Fanta:")
mall_instance.fanta.sell()
mall_instance.fanta.buy()

print("\nSelling Cocacola:")
mall_instance.cocacola.sell()
mall_instance.cocacola.buy()
