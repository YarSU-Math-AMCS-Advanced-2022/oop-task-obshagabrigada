from datetime import datetime, date, time

class Product:
    def __init__(self):
        self.price = 0
        self.name = "YetAnotherProduct"
        self.ingredients = []
        self.energy_value = None
        self.cooking_time = 10 ** 12
        self.additional = [('Ничего', 10 ** 12), ('negr', 0)]
    
    def get_something(self):
        print('get_something')

class Cart:
    def __init__(self):
        self.facility = None
        self.list_products = []
        self.cost = 0
        
    def add_to_cart(self, product):
        self.list_products.append(product)
    
    def clear_cart(self):
        self.list_products = []
    
    def pop_product(self, product):
        print('pop_product')
        
    def confirm_cart(self):
        return self

Facilities = []
Clients = []
Products = []


class Facility:
    def __init__(self, start_time=(0, 0), 
                 end_time=(23, 59), name="YetAnotherFacility"):
        self.name = name
        self.list_orders = []
        self.workig_hours = (start_time, end_time)
    
    def add_order(self):
        print(self.name, 'add_order')
    
    def cooking_process(self):
        print(self.name, 'cooking_process')
    
    def give_order(self):
        print(self.name, 'give_order')
    
    def get_info(self):
        print('list_orders:', self.list_orders)
        print('working_hours:', self.working_hours)
        print('facility_name:', self.name)
    
class Payment:
    def __init__(self):
        self.payment_methods = ['nalom', 'analom', 'bank_card']
        self.payment_amount = 0
        self.bonus = 0
    
    def make_payment(self):
        print('Выберете способ оплаты')
        for method in payment_methods:
            print(method)
        choose_method = input()
        for method in payment_methods:
            if choose_method == method:
                if self.get_payment_confirm(method):
                    print('Оплата прошла успешно')
                else:
                    print('Во время оплаты произошла ошибка')
        print('Такого способа оплаты не существует')
    
    def get_payment_confirm(self, method):
        if method == 'analom':
            print('Welcome to the club, body.')
        return True
    
class Client:
    def __init__(self, name="Noname", phone_number=0, \
                 cart=Cart(), bonus=0):
        self.name = name
        self.phone_number = phone_number
        self.cart = cart
        self.bonus = bonus
        self.payment = Payment()
    
    def choose_facility(self):
        print('Выберете ресторан: ')
        for facility in Facilities:
            print(facility.name)
        self.cart = Cart()
        name_of_facility = input()
        for facility in Facilities:
            if facility.name == name_of_facility:
                self.cart.facility = facility
                return
        print('Ресторана с таким названием не существует')
        
    def choose_product(self):
        if self.cart.facility == None:
            print('Сначала выберете ресторан')
            return
        print('Добавьте продукт в корзину')
        for product in Products:
            print(product.name)
        name_of_product = input()
        for product in Products:
            if product.name == name_of_product:
                cart_product = product
                self.add_additional(cart_product)
                return
        print('Такого продукта не существует')
    
    def add_additonal(self, product):
        while True:
            print('Выберете дополнение к основному продукту')
            for addition in product.additional:
                print(addition[0], addition[1])
            additional_product = input()
            for addition in product.additional:
                if addition[0] == additional_product:
                    print('Дополнение добавлено в корзину.')
                    return 
            print('Такого дополнения к этому продукту не существует')
        
    def get_payment(self):
        if self.cart.facility == None:
            print('Сначала выберете ресторан')
            return 
        print('Ресторан:', self.cart.facility.name)
        for product in self.cart.list_products:
            print(product.name)
        print('Счет:', self.cart.cost)
        self.payment.make_payment()
        
        
    def call_delivery_boy(self):
        print('call_delivery_boy')
    
    def cancel_order(self):
        print('Вы отменили заказ. Корзина пуста.')
        self.cart = Cart
        
    def make_rate(self):
        print('make_rate')
    
    def __str__(self):
        return "name: {}, phone_number: {}, bonus: {}".format( \
            self.name, self.phone_number, self.bonus)

client = Client(phone_number=89218294671)
print(client)