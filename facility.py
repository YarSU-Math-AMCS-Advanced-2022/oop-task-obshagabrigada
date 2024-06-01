from product import Product
from order import Order, Status
from cooker import Cooker
from courier import Courier
from worker import WorkerStatus
from Review_and_Stock import Review
import random
Facilities = []

class Facility:

    list_cookers: list[Cooker]
    list_orders: list[Order]
    listReview:list[Review]
    menu: list[Product]

    def __init__(self, name=''):
        self.listReview = list()
        self.name = name
        self.list_orders = []
        self.menu=[]
        self.list_cookers=[]
        self.position = tuple((random.uniform(-10000, 10000), random.randint(-10000, 10000)))

    def add_dish(self):
        dish_name=input('Введите название блюда: ')
        dish_price=int(input('Введите цену блюда: '))
        dish_ingridients = list(map(str, input('Введите ингридиенты через пробел: ').split(' ')))
        dish_additional=[]
        dish_energy=input('Введите энергетическую ценность блюда: ')
        count_of_aditional=int(input('Сколько допов для блюда? '))
        for i in range(count_of_aditional):
            a=input('Введите название допа: ')
            b=int(input('Введите цену допа: '))
            dish_additional.append([a,b])
        dish_time=int(input('Введите время приготовления: '))
        new_dish=Product(dish_name,dish_price,dish_ingridients, dish_additional,dish_energy,dish_time)
        self.menu.append(new_dish)

    def add_order(self, new_order :Order):
        new_order.status=Status.ACCEPTED
        self.list_orders.append(new_order)
        
    def add_cooker(self):
        new_cooker=Cooker(6)
        new_cooker.get_shift(0)
        self.list_cookers.append(new_cooker)

    def cooking_process(self):
        for order in self.list_orders:
            if order.status==Status.ACCEPTED:
                for cook in self.list_cookers:
                    if cook.workerStatus==WorkerStatus.FREE:
                        cook.give_order(order)
                        break
        for cook in self.list_cookers:
            if cook.workerStatus==WorkerStatus.INPROGRESSWORK:
                cook.order_assembly()
    
    def give_order(self, list_couriers :list[Courier]):
        for order in self.list_orders:
            if order.status==Status.INSTOCK:
                for courier in list_couriers:
                    if courier.workerStatus==WorkerStatus.FREE:
                        courier.give_order(order)
                        self.list_orders.remove(order)
                        break
    
    def printReview(self):
        for review in self.listReview:
            review.print_review()
            print(f'Следущий отзыв или нет y/n')
            otv = input()
            if(otv == 'n'):
                return
        print('Отзывы закончились')

def add_facility(start_time=(0, 0), end_time=(23, 59), name=''):
    Facilities.append(Facility(start_time, end_time, name))