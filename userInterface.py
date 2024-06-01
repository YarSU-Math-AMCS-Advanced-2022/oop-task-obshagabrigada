from client import Client
from app import App
def UserInterface(user:Client,app:App):
    while(True):
        print('Выберите нужный пункт: ')
        print('1: Посмотреть каталог')
        print('2: Добавить товар в корзину')
        print('3: Удалить товар из корзины')
        print('4: Посмотреть корзину')
        print('5: Сделать заказ')
        print('6: Изменить адресс доставки')
        print('7: Удалить корзину')
        print('8: Увидеть статус заказа')
        print('9: Вывести отзывы о зведении')
        print('-'*20)
        n = int(input())
        print('-'*20)
        match n:
            case 1:
                app.CatalogFacility()
            case 2:
                user.choose_facility(app.listFacility)
            case 3:
                user.cart.pop_product()
            case 4:
                user.cart.printCart()
            case 5:
                app.CreateOrder(user)
            case 6:
                address = input('Введите адресс пользователя: ')
                user.changeAdress(address)
            case 7:
                user.cart.clear_cart()  
            case 8:
                print (f'1)Найти по ID 2) Найти по имени пользователя')
                n = int(input())
                if(n == 1):
                    id = input('Введите айди заказа')
                    app.printOrderStatusID(id)
                else:
                    app.printOrderStatusName(user.name)
            case 9:
                facility = app.FindFacility()
                if facility != None:
                    facility.printReview()
            case _:
                return
        print('-'*20)