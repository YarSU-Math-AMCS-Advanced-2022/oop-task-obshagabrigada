from app import App
#from client import Client
from userInterface import UserInterface
from facility import Facility
def AppInterface(app:App):
    while(True):
        print('-'*20)
        print('Выберите нужный пункт: ')
        print('1: Добавить нового пользователя и выбрать как активного')
        print('2: Добавить новое заведение и настроить его')
        print('3: Добавить курьера')
        print('4: Добавить скидку')
        print('5: Работа приложения')
        print('-'*20)
        n = int(input())
        print('-'*20)
        match n:
            case 1:
                user = app.createNewClient()
                UserInterface(user,app)
            case 2:
                facility = app.addFacility()
                FacilityInterface(facility)
            case 3:
                app.AddCourie()
            case 4:
                app.addSale()
            case 5:
                Update(app)
            case _:
                return
        print('-'*20)


def FacilityInterface(facility:Facility):
    while(True):
        print('Выберите нужный пункт: ')
        print('1: Добавить новое блюдо')
        print('2: Добавить повара')
        print('-'*20)
        n = int(input())
        print('-'*20)
        match n:
            case 1:
                facility.add_dish()
            case 2:
                facility.add_cooker()
            case _:
                return
        print('-'*20)


def Update(app:App):
    app.giveOrderToFacility()
    app.SetCouirerToWork()
    for facility in app.listFacility:
        facility.cooking_process()
        facility.give_order(app.courierList)
    for couirer in app.courierList: 
        if(couirer.currentWork != None):
                couirer.take_order() 
    for order in app.orederList:
        for user in app.clientList:
            if(user.name == order.clientName):
                user.TakeOrder(order)
                break

    app.clearRecieveOrder()      
    

    