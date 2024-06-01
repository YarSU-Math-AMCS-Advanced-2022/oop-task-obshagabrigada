from order import Order,Status
from client import Client
from Review_and_Stock import Stock
from courier import Courier
from facility import Facility
from worker import WorkerStatus

class App:
    appName: str
    listFacility: list[Facility]
    clientList: list[Client]
    orederList: list[Order]
    courierList: list[Courier]
    saleList:list[Stock]

    def __init__(self,name) -> None:
        self.clientList = list()
        self.listFacility = list()
        self.orederList = list()
        self.courierList = list()
        self.saleList = list()
        self.appName = name

    def createNewClient(self):
        name = input('Введите имя пользователя :')
        adress = input('Введите адрес пользователя :')
        phone = input('Введите телефон пользователя :')
        newUser = Client(name,adress,phone)
        self.clientList.append(newUser)
        return newUser
    
    def CreateOrder(self,client:Client):
        cost = client.cart.count_cost_cart()
        for sale in self.saleList:
            cost -= sale.stock_using(client.cart)
        facility = client.cart.facility.name
        lstProduct = client.cart.list_products.copy()
        if client.get_payment(cost):
            newOrder = Order(client.name,facility,Status.PROCESSING,lstProduct,client.adress)
            self.orederList.append(newOrder)
        else:
            print(f'У вас не хватает руб')

    def addFacility(self):
        name = input('Введите название: ')
        newFacilty = Facility(name)
        self.listFacility.append(newFacilty)
        return newFacilty
    
    def printOrderStatusID(self,orderID:str):
        for order in self.orederList:
            if orderID == order.orderId:
                order.printOrder()
                return
    
    def printOrderStatusName(self,orderName:str):
        for order in self.orederList:
            if (order.clientName == orderName):
                order.printOrder()

    def addSale(self):
        facilityName = input('Введите название заведения: ')
        productName = input('Введите название продукта: ')
        while True:
            try:
                discount = int(input('Введите размер скидки: '))
                break
            except Exception:
                print('Некорректный ввод данных. Повторите ввод, пожалуйста.')        
        print('условие может быть 1) сумма 2) количество')
        while True:
            try:
                n = int(input())
                break
            except Exception:
                print('Некорректный ввод данных. Повторите ввод, пожалуйста.')
        if (n == 1):
            sum = int(input('Введите сумму для применения акции '))
            condition = lambda cart : True if cart.count_cost_cart() >= sum else False
        else:
            count = int(input('Введите количество для применения акции'))
        #condition = input()
        description = input('Введите описание скидки: ')
        for facility in self.listFacility:
            if(facility.name == facilityName):
                for product in facility.menu:
                    if productName == product.name:
                        condition = lambda cart: True if cart.returnCountofProduct(product) >= count else False
                        newSale = Stock(facility,product,discount,description,condition)
                        self.saleList.append(newSale)
                    break
                break

    def giveOrderToFacility(self):
        for order in self.orederList:
            for facility in self.listFacility:
                if(facility.name == order.facilityName):
                    facility.add_order(order)

    def clearRecieveOrder(self):
        for order in self.orederList:
            if order.status == Status.RECEIVED:
                print(f'заказ с ID:{order.orderId} был получен пользователем')
                print(f'oставьте отзыв о заведении: ')
                for client in self.clientList:
                    if order.clientName == client.name:
                        review = client.make_rate()
                for facility in self.listFacility:
                    if(order.facilityName == facility.name):
                        facility.listReview.append(review)
                self.orederList.remove(order)
            elif order.status == Status.CANCEL:
                print(f'заказ с ID:{order.orderId} был отменен')
                self.orederList.remove(order)

    def CatalogFacility(self):
        for facility in self.listFacility:
            print("Название ресторана:", facility.name)
            for product in facility.menu:
                product.printProduct()
            

    def FindFacility(self):
        facilityName = input('Введите название заведения: ')
        for facility in self.listFacility:
            if facility.name == facilityName:
                return facility
        print('Такого заведения не существует')
        return None    
    
    def SetCouirerToWork(self):
        for courie in self.courierList:
            if(courie.workerStatus == WorkerStatus.NOTWORKING):
                courie.get_shift()
            

    def AddCourie(self):
        print('Курьер был добавлен')
        newCourie = Courier(6)
        self.courierList.append(newCourie)
    pass
