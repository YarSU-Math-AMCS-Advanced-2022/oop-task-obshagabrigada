from Patterns import Singleton

class Payment(Singleton):
    def __init__(self):
        self.payment_methods = ['nalom', 'analom', 'Банковской картой']
        self.payment_amount = 0
        self.bonus = 0
    
    def make_payment(self):
        print('Выберете способ оплаты')
        for method in self.payment_methods:
            print(method)
        choose_method = input()
        for method in self.payment_methods:
            if choose_method == method:
                if self.get_payment_confirm(method):
                    print('Оплата прошла успешно')
                    return True
                else:
                    print('Во время оплаты произошла ошибка')
                    return False
        print('Такого способа оплаты не существует')
        return False
    
    def get_payment_confirm(self, method):
        if method == 'analom':
            print('Welcome to the club, body.')
        return True