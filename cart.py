from facility import Facility


# класс корзина
class Cart:
    is_confirmed: bool = False  # подтверждена ли корзина
    order_amount: float = 0  # сумма заказа корзины

    def __init__(self):
        self.facility = None
        self.list_products = []  # название продукта и его кол-во
        self.additional_dict = dict()

    def add_to_cart(self, product):  # добавить в корзину
        self.list_products.append([product, 1])

    def add_addition(self, product, additional):  # дополнение к продукту
        if product.name not in self.additional_dict:
            self.additional_dict[product.name] = []
        self.additional_dict[product.name].append(additional)

    def set_product_count(self, product, count_product):  # установить кол-во продуктов
        if count_product >= 0:
            for i in range(len(self.list_products)):
                if self.list_products[i][0] == product:
                    self.list_products[i][1] = count_product

    def clear_cart(self):  # очистить корзину
        self.list_products = []
        self.additional_dict = {}

    def pop_product(self):  # удалить продукт из корзины
        print('Введите название товара, который хотите убрать из корзины: ',
              end="")
        product_name = input()
        if product_name not in self.list_products:
            print('Такого продукта в корзине нет')
            return
        for i in range(len(self.list_products)):
            if self.list_products[i] == product_name:
                self.list_products.pop(i)
                break
        self.additional_dict.pop(product_name)
        print('Продукт успешно удален из корзины')

    def count_cost_cart(self):  # подсчитать стоимость корзины
        for i in range(len(self.list_products)):
            self.order_amount += self.list_products[i][0].price * self.list_products[i][1]

        for product_name in self.additional_dict.keys():
            for dop in self.additional_dict[product_name]:
                self.order_amount += dop[1]

        return self.order_amount

    def printCart(self):
        if (self.facility != None):
            print(f'Заведение {self.facility.name}')
            for product in self.list_products:
                print(f'Продукт {product[0].name}, количество {product[1]}')
                if product[0].name in self.additional_dict:
                    print('Допы:')
                    for add in self.additional_dict[product[0].name]:
                        print('Название: {}'.format(add))

    def confirm_cart(self):  # подтвердить
        self.is_confirmed = True

    def returnCountofProduct(self, product):
        for products in self.list_products:
            if (products[0].name == product.name):
                return products[1]